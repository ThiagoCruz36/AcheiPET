import streamlit as st
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os
import bcrypt
from achei_pet.configs.settings import DBNAME, USER, PASSWORD, HOST, PORT

# Database connection parameters
db_params = {
    "dbname":  DBNAME,
    "user": USER,
    "password": PASSWORD,
    "host": HOST,
    "port": PORT
}

def verify_duplicate_user(email):
    conn = psycopg2.connect(**db_params)
    cur = conn.cursor()
    
    cur.execute("SELECT COUNT(*) FROM users WHERE email = %s", (email,))
    count = cur.fetchone()[0]
    
    cur.close()
    conn.close()
    
    return count > 0


def authenticate_user(email, password):
    conn = psycopg2.connect(**db_params)
    cur = conn.cursor()
    
    # Retrieve the stored hashed password for the user
    cur.execute("SELECT hash_password FROM users WHERE email = %s", (email,))
    stored_hashed_password = cur.fetchone()
    
    cur.close()
    conn.close()

    # Check if a user with the given email was found
    if stored_hashed_password is None:
        return False
    
    stored_hashed_password = stored_hashed_password[0]  # Extract the hash from the tuple

    # Compare the provided password with the stored hashed password
    return bcrypt.checkpw(password.encode(), stored_hashed_password.encode())

    

def save_user(email, password, name):
    conn = psycopg2.connect(**db_params)
    cur = conn.cursor()
    
    # Hash the password before saving
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode('utf-8')
    
    # Base columns and values
    columns = ['email', 'hash_password', 'name']
    values = [email, hashed_password, name]
    
    # Dynamically build the SQL query
    columns_str = ', '.join(columns)
    placeholders = ', '.join(['%s'] * len(values))
    
    query = sql.SQL("INSERT INTO users ({}) VALUES ({})").format(
        sql.SQL(columns_str),
        sql.SQL(placeholders)
    )
    
    # Execute the query
    cur.execute(query, values)

    conn.commit()
    cur.close()
    conn.close()
    

def get_users():
    conn = psycopg2.connect(**db_params)
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return users


def save_pet(name, color, status, latitude, longitude, filename, telefone):
    conn = psycopg2.connect(**db_params)
    cur = conn.cursor()

    # Base columns and values
    columns = ['name', 'color', 'status', 'latitude', 'longitude', 'image_filename', 'telefone']
    values = [name, color, status, latitude, longitude, filename, telefone]
    
    # Dynamically build the SQL query
    columns_str = ', '.join(columns)
    placeholders = ', '.join(['%s'] * len(values))
    
    query = sql.SQL("INSERT INTO pets ({}) VALUES ({})").format(
        sql.SQL(columns_str),
        sql.SQL(placeholders)
    )
    
    # Execute the query
    cur.execute(query, values)

    conn.commit()
    cur.close()
    conn.close()

def get_pets_perdidos():
    conn = psycopg2.connect(**db_params)
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM pets WHERE status = 'Perdido'")
    pets = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return pets

def get_pets_abandonados():
    conn = psycopg2.connect(**db_params)
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM pets WHERE status = 'Abandonado'")
    pets = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return pets