from Config_DB import *

mydb = creacion_db()
cursor = mydb.cursor()

def crear_destino():

    ciudad = input("Ingrese ciudad: ")
    pais = input("Ingrese pais: ")
    costo = input("Ingrese costo: ")

    destino = [ciudad, pais, costo]

    return destino

def insercion_destino(destino):
    mydb = creacion_db()
    cursor = mydb.cursor()

    sql = "INSERT INTO destinos (ciudad, pais, costo) VALUES (%s, %s, %s)"
    val = (destino[0], destino[1], destino[2])
    cursor.execute(sql, val)

    mydb.commit()

    print("Datos guardados con exito.")

def mostrar_destino():
    mydb = creacion_db()
    cursor = mydb.cursor()

    cursor.execute("SELECT ciudad, pais, costo FROM destinos")
    resultado = cursor.fetchall()

    for i in resultado:
        print(i)

def modificar_destino():
    mydb = creacion_db()
    cursor = mydb.cursor()

    mostrar_destino()
    mod = input("ingrese ciudad del destino que desea modificar: ")

    sql = (f"SELECT * FROM destinos WHERE ciudad = '{mod}'")

    cursor.execute(sql)
    resultado = cursor.fetchall()

    for i in resultado:
        print(f"Registro a modificar {i}.")
        destino = crear_destino()

        cd = (f"UPDATE destinos SET ciudad = '{destino[0]}' WHERE ciudad = '{i[1]}'")
        ps = (f"UPDATE destinos SET pais = '{destino[1]}' WHERE pais = '{i[2]}'")
        ct = (f"UPDATE destinos SET costo = '{destino[2]}' WHERE costo = '{i[3]}'")

        cursor.execute(cd)
        cursor.execute(ps)
        cursor.execute(ct)

        mydb.commit()

        print("Archivo modificado con exito")


def eliminar_destino():
    mydb = creacion_db()
    cursor = mydb.cursor()

    destino = input("Ingrese la ciudad del destino a eliminar: ")

    sql = (f"DELETE FROM destinos WHERE ciudad = '{destino}'")

    cursor.execute(sql)

    mydb.commit()

    print(f"El registro del destino: {destino} ha sido eliminado.")

cursor.close()