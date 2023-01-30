from sqlalchemy import create_engine as ce
import psycopg2
import pandas as pd

conn = psycopg2.connect("dbname=sahibinden user=postgres password=5645645")

pg_engine = ce("postgresql://postgres:5645645@localhost:5432/sahibinden")

data = pd.read_csv("Sahibinden_Toyota.csv")

data.to_sql('Sahibinden_Toyota.csv', pg_engine)