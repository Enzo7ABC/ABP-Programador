"""

 ==============================================================================
 PROTOTIPO DE SISTEMA DE GESTIÓN DE PASAJES - SKYROUTE S.R.L.
 ==============================================================================

 PROPÓSITO DEL SISTEMA:
   Gestionar la venta de pasajes, el registro de clientes, los destinos
   disponibles y la funcionalidad del "botón de arrepentimiento"
   (anulación de compra dentro de un período limitado).

 INSTALACIÓN Y EJECUCIÓN:
   1. Asegúrate de tener Python 3 instalado en tu sistema.
   2. Guarda este código en un archivo con extensión .py (ej: 'skyroute_app.py').
   3. Abre una terminal o línea de comandos.
   4. Navega hasta el directorio donde guardaste el archivo.
   5. Ejecuta el programa con el comando: python skyroute_app.py

   Notas:
      - Los datos se almacenan en memoria y se perderán al cerrar la aplicación.

 INTEGRANTES DEL GRUPO:
   - CABANA, ENZO ALAN BAIL (DNI 36.048.872)
   - CABRAL, LEANDRO ELÍAS (DNI 43.233.136)
   - BARILES, JULIETA BELÉN (DNI 38.329.962)
   - DELFINI, DONATA VIRGINIA (DNI 27.296.444)

 ==============================================================================

"""
from traceback import TracebackException

# importacion de modulos

from Funciones_cliente import *
from Funciones_destino import *

# Inicializacion de variables bandera para validaciones.
bandera_cliente = False
bandera_destino = False

# Variable verdadera para que el ciclo While se ejecute hasta oprimir 0 y cambiar su valor
op = True

# INICIO DEL MENU PRINCIPAL

while op:
    print("*" * 40,"\n"," "* 5,"| Bienvenidos a SkyRoute |"
          "\n| Sistema de Gestión de Pasajes Aereos |\n",
          "*" * 39,
          "\n 1 : Clientes."
          "\n 2 : Destinos."
          "\n 3 : Registrar Venta de Pasaje."
          "\n 4 : Vizualizar Ventas."
          "\n 5 : Boton de arrepentimiento."
          "\n 0 : Salir.")

    op = int(input("Ingrese su opcion: "))

# FIN DEL MENU PRINCIPAL

# INICIO OPCION 1

    if op == 1:
        print("\n1 - Ver Clientes."
              "\n2 - Agregar Cliente."
              "\n3 - Modificar Cliente."
              "\n4 - Eliminar Cliente"
              "\n5 - Volver al Menu.\n")
        op_cliente = int(input("Ingrese su opcion: "))

        if op_cliente == 1:
            # Implementamos un bloque try para utilizar la excepcion en caso de no haber
            # ingresado un Cliente y mostrarle al usuario que faltan cargar datos.
            try:
                mostrar_cliente()
            except:
                print("\nNo has ingresado ningun cliente.\n")

        elif op_cliente == 2:
            #Carga de datos: Cliente.
            cliente = crear_cliente()
            insercion_cliente(cliente)

            print("\nCliente registrado con exito.\n")
            # Cambio de valor de bandera_cliente que nos indica que el cliente se registro.
            bandera_cliente = True

        elif op_cliente == 3:
            if bandera_cliente: # Comprobamos que se han ingresado datos del Cliente y se ejecuta la rama verdadera para modificar los datos.
                modificar_cliente()
                print("\nCliente modificado con exito.\n")
            else:# La rama falsa nos indica que aun no se han ingresado datos de Cliente.
                print("\nNo se ha registrado cliente aun.\n")

        elif op_cliente == 4:
            # Implementamos un bloque try para utilizar la excepcion en caso de no haber
            # ingresado un Cliente y mostrarle al usuario que faltan cargar datos.
            try:
                mostrar_cliente()
                eliminar_cliente()
            except:
                print("\nNo has ingresado ningun cliente.\n")

# FIN DE OPCION 1

# INICIO OPCION 2

    elif op == 2:
        print("\n1 - Ver Destinos."
              "\n2 - Agregar Destino."
              "\n3 - Modificar Destino."
              "\n4 - Eliminar Destino"
              "\n5 - Volver al Menu.\n")
        op_destino = int(input("Ingrese su opcion: "))

        if op_destino == 1:
            # Implementamos un bloque try para utilizar la excepcion en caso de no haber
            # ingresado un Destino y mostrarle al usuario que faltan cargar datos.
            try:
                mostrar_destino()
            except:
                print("\nNo has ingresado ningun destino.\n")

        elif op_destino == 2:
            #Carga de datos: Destino.
            destino = crear_destino()
            insercion_destino(destino)

            print("\nDestino creado con exito.\n")
            # Cambio de valor de bandera_destino que nos indica que el destino se registro.
            bandera_destino = True

        elif op_destino == 3:
            if bandera_destino: # Comprobamos que se han ingresado datos de Destino y se ejecuta la rama verdadera para modificar los datos.
                modificar_destino()
                print("Destino modificado con exito.")
            else: # La rama falsa nos indica que aun no se han ingresado datos de Destino.
                print("\nNo se ha ingresado ciudad aun.\n")

        elif op_destino == 4:
            # Implementamos un bloque try para utilizar la excepcion en caso de no haber
            # ingresado un Cliente y mostrarle al usuario que faltan cargar datos.
            try:
                mostrar_destino()
                eliminar_destino()
                # Reiniciamos el valor de bandera_destino al eliminar el destino.
                bandera_destino = False
            except:
                print("\nNo has ingresado ningun destino.\n")

# FIN DE OPCION 2

# INICIO OPCION 3

    elif op == 3:
        if bandera_cliente and bandera_destino: #Utilizamos esta comprobacion para confirmar que se creo un cliente y un destino, para asociarlos.
            fecha = int(input("Ingrese fecha (formato: DDMMAA): "))
            estado = "Activa"
            print("\nVenta registrada con exito.\n")
        else: #En caso de que cliente o destino no se hayan registrado, se muestra mensaje pidiendo cargar los datos.
            print("\nDebe agregar Cliente y Destino para registrar venta.\n")

# FIN DE OPCION 3

# INICIO OPCION 4

    elif op == 4:
        try:
            # Implementamos un bloque try para utilizar la excepcion en caso de que no se
            # haya inicializado la variable "estado" la cual usamos para comprobar que se registro la venta
            # y mostrarle al usuario que faltan cargar datos.
            if estado == "Activa":
                print(f"\nCliente: {razon_social} Destino: {pais} Fecha: {fecha} Estado: {estado}\n")
            elif estado == "Anulada":
                print(f"\nCliente: {razon_social} Destino: {pais} Fecha: {fecha} Estado: {estado}\n")
            else:
                print("\nNo hay ventas registradas.\n")
        except NameError:
            print("\nNo hay ventas registradas.\n")

# fIN DE OPCION 4

# INICIO OPCION 5

    elif op == 5:
        # Implementamos un bloque try para utilizar la excepcion en caso de que no se
        # haya inicializado la variable "estado" la cual usamos para comprobar que se registro la venta
        # y mostrarle al usuario que faltan cargar datos.
        try:
            if estado == "Activa": #Comprobamos que la venta se registro.
                estado = "Anulada" #Con el boton de arrepentimiento la venta cambia su estado a "Anulada".
                print("\nLa venta ha sido anulada.\n")
            else:
                print("\nNo hay ventas registradas.\n")

        except NameError:
            print("\nNo hay ventas registradas.\n")

# FIN DE OPCION 5

# FIN DEL PROGRAMA.
