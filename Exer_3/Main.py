import Order
import mysql.connector
from mysql.connector import Error
import pandas as pd

def create_server_connection(host_name, user_name, user_password,db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

table_order = """
CREATE TABLE orders(
order_id INT PRIMARY KEY,
preco FLOAT NOT NULL,
quantidade iNT NOT NULL
)
"""

q1 = """
SELECT *
FROM orders;
"""

connection = create_server_connection("localhost", "root", "admin123","mydb")
#myquery = "CREATE DATABASE mydb"
#create_database(connection,myquery)
#create_database(connection,table_order)

preco = float(input("Digite o preco"))
quantidade = int(input("Digite a quantidade"))

#insert_table = "INSERT INTO orders VALUES (1,{},{})".format(preco,quantidade)
#create_database(connection,insert_table)

novo_pedido = Order.Order(preco,quantidade)
conta = novo_pedido.total()
print(conta)

results = read_query(connection, q1)

for result in results:
  print(result)