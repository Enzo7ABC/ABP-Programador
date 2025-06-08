# importamos libreria mysql-connector (instalar en terminal: pip install mysql-connector-python)

import mysql.connector

def creacion_db():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="skyroute" # una vez creada la base de datos colocamos su nombre acá para crear las tablas
    )

    return mydb

# creacion de base de datos y tablas

#cursor.execute("CREATE DATABASE skyroute")

# creacion de tablas

#cursor.execute("CREATE TABLE clientes (id INT AUTO_INCREMENT PRIMARY KEY, razon_social VARCHAR(255), cuit VARCHAR(255), email VARCHAR(255))")
#cursor.execute("CREATE TABLE destinos (id INT AUTO_INCREMENT PRIMARY KEY, ciudad VARCHAR(255), pais VARCHAR(255), costo VARCHAR(255))")
#cursor.execute("CREATE TABLE ventas (id INT AUTO_INCREMENT PRIMARY KEY, cliente VARCHAR(255), destino VARCHAR(255), fecha DATE, costo VARCHAR(255), estado VARCHAR(255))")

# con .commit guardamos los cambios
# mydb.commit()

# cerramos la base de datos
# cursor.close()