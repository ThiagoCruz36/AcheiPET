import psycopg2
from psycopg2 import sql
from achei_pet.settings import DBNAME, USER, PASSWORD, HOST, PORT

# Database connection parameters
db_params = {
    "dbname":  DBNAME,
    "user": USER,
    "password": PASSWORD,
    "host": HOST,
    "port": PORT
}
print(db_params)

def create_database():
    # Connect to the default 'postgres' database to create a new database
    conn = psycopg2.connect(dbname="postgres", **{k: v for k, v in db_params.items() if k != "dbname"})
    conn.autocommit = True
    cur = conn.cursor()
    
    # Create the new database
    cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_params["dbname"])))
    
    cur.close()
    conn.close()

def create_table():
    # Connect to the new database
    conn = psycopg2.connect(**db_params)
    cur = conn.cursor()
    # Create the table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            email VARCHAR(255) UNIQUE NOT NULL,
            name VARCHAR(255) NOT NULL
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS pets (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            color VARCHAR(255) NOT NULL,
            latitude NUMERIC NOT NULL,
            longitude NUMERIC NOT NULL,
            image_filename VARCHAR(255) NOT NULL,
            status VARCHAR(255) NOT NULL,
            telefone VARCHAR(255) NOT NULL
        );
    """)
    
    conn.commit()
    cur.close()
    conn.close()


create_database()
create_table()

