import os 
import psycopg2

DATABASE_URL = os.environ["DB_URL"]

connect = psycopg2.connect(DATABASE_URL, sslmode='require')