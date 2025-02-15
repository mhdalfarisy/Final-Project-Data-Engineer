from airflow import DAG
from airflow.operators.python_operator import PythonOperator, BranchPythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago
from airflow.utils.trigger_rule import TriggerRule
import pandas as pd
from airflow.providers.postgres.hooks.postgres import PostgresHook

SOURCE_PATH = "/opt/airflow/resources/source_data/data_sample.csv"
TRANSFORMED_PATH = "/opt/airflow/resources/staging/data_sample_tranform.csv"

default_args = {
    "owner": "faris",
}

with DAG(
    dag_id="6_full_etl_test",
    default_args=default_args,
    description="ETL Pipeline untuk extract, transform, load data",
    schedule_interval="@daily",
    start_date=days_ago(1),
    catchup=False,
    params={"source_type": "csv"},
) as dag:

    def pilih_source(**kwargs):
        source_type = kwargs.get("params").get("source_type", "csv")
        print(f"Selected source type: {source_type}")

        if source_type == "csv":
            return "extract_csv"
        else:
            raise ValueError("source_type harus 'csv'")

    branch_task = BranchPythonOperator(
        task_id="choose_source",
        python_callable=pilih_source,
        provide_context=True,
    )

    def extract_csv_6():
        df = pd.read_csv(SOURCE_PATH, sep=',', engine="python")
        print(f"Extracted Data: {len(df)}")
        print(f"Example Data sucess Load : {df.head(1)}")
        print(f"Save to csv (Folder Staging. . .)")
        df.to_csv(TRANSFORMED_PATH,index=False)

    extract_csv_task_new = PythonOperator(
        task_id="extract_csv",
        python_callable=extract_csv_6,
    )

    def tranform_csv ():
        df_transform = pd.read_csv(TRANSFORMED_PATH,sep=',', engine="python")
        if 'sub_coll_IDs' in df_transform.columns : 
            df_transform['sub_coll_IDs'] = df_transform['sub_coll_IDs'].astype(str).str.replace(",","|")
        df_transform.to_csv(TRANSFORMED_PATH, index=False)        
        print("Data Done Tranformation . . . ")
        
    tranform_csv_task = PythonOperator(
        task_id="tranform_csv",
        python_callable=tranform_csv,
    )


    def load_to_postgres():

        hook = PostgresHook(postgres_conn_id="docker_postgres")
        
        df = pd.read_csv(TRANSFORMED_PATH, engine="python")
        
        engine = hook.get_sqlalchemy_engine()
        df.to_sql("for_da", con=engine, if_exists="replace", index=False)
        print("Data berhasil dimasukkan ke PostgreSQL!")

    load_to_postgres_task = PythonOperator(
        task_id="load_to_postgres",
        python_callable=load_to_postgres,
        trigger_rule=TriggerRule.ONE_SUCCESS,
    )

    start_task = DummyOperator(task_id="start")
    end_task = DummyOperator(task_id="end")

    start_task >> branch_task
    branch_task >> extract_csv_task_new
    extract_csv_task_new >> tranform_csv_task
    tranform_csv_task >> load_to_postgres_task
    load_to_postgres_task >> end_task
