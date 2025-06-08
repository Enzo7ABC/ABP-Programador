# Importamos modulos

from Config_DB import *

mydb = creacion_db()
cursor = mydb.cursor()

def crear_cliente():

    razon_social = input("Ingrese razon social: ")
    cuit = input("Ingrese cuit: ")
    email = input("Ingrese email: ")

    cliente = [razon_social, cuit, email]

    return cliente

def insercion_cliente(cliente):
    mydb = creacion_db()
    cursor = mydb.cursor()

    sql = "INSERT INTO clientes (razon_social, cuit, email) VALUES (%s, %s, %s)"
    val = (cliente[0], cliente[1], cliente[2])
    cursor.execute(sql, val)

    mydb.commit()

def mostrar_cliente():
    mydb = creacion_db()
    cursor = mydb.cursor()

    cursor.execute("SELECT razon_social, cuit, email FROM clientes")
    resultado = cursor.fetchall()

    for i in resultado:
        print(i)

def modificar_cliente():
    mydb = creacion_db()
    cursor = mydb.cursor()

    mostrar_cliente()
    mod = input("ingrese razon social del cliente que desea modificar: ")

    sql = (f"SELECT * FROM clientes WHERE razon_social = '{mod}'")

    cursor.execute(sql)
    resultado = cursor.fetchall()

    for i in resultado:
        print(f"Registro a modificar {i}.")
        cliente = crear_cliente()

        rs = (f"UPDATE clientes SET razon_social = '{cliente[0]}' WHERE razon_social = '{i[1]}'")
        ct = (f"UPDATE clientes SET cuit = '{cliente[1]}' WHERE cuit = '{i[2]}'")
        em = (f"UPDATE clientes SET email = '{cliente[2]}' WHERE email = '{i[3]}'")

        cursor.execute(rs)
        cursor.execute(ct)
        cursor.execute(em)

        mydb.commit()


def eliminar_cliente():
    mydb = creacion_db()
    cursor = mydb.cursor()

    cliente = input("Ingrese la razon social del cliente a eliminar: ")

    sql = (f"DELETE FROM clientes WHERE razon_social = '{cliente}'")

    cursor.execute(sql)

    mydb.commit()

    print(f"El registro del cliente: {cliente} ha sido eliminado.")

cursor.close()