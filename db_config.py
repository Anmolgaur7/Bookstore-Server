import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Cristiano@7",
        database="bookstore_db"
    )
    return connection