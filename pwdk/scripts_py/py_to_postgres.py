import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Memuat file .env untuk mendapatkan variabel koneksi
load_dotenv()

# Membaca URL koneksi dari .env
db_url = os.getenv('AIRFLOW__DATABASE__SQL_ALCHEMY_CONN')  # Koneksi dari .env, misalnya: postgresql+psycopg2://airflow:airflow@postgres/airflow

# Membuat engine koneksi menggunakan sqlalchemy
engine = create_engine(db_url)

# Membaca data dari PostgreSQL menggunakan pandas
def read_data_from_postgres():
    # Query untuk membaca data
    query = "SELECT * FROM performance_and_attrition;"  # Ganti dengan nama tabel yang ingin dibaca
    
    # Membaca data ke dalam DataFrame pandas
    data = pd.read_sql(query, engine)
    
    # Menampilkan preview data
    print(data.head())

# Memanggil fungsi untuk membaca data
read_data_from_postgres()
