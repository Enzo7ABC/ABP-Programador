# ABP-Programador


#Archivos principales del proyecto ABP
1. Main.py
Propósito: Es el archivo principal del sistema de gestión de pasajes "SkyRoute S.R.L.".
Funcionalidad:
Menú principal con opciones para gestionar clientes, destinos, ventas y el "botón de arrepentimiento".
Utiliza funciones de los módulos Funciones_cliente y Funciones_destino.
Controla el flujo del programa y la interacción con el usuario.
2. Config_DB.py
Propósito: Configuración y conexión a la base de datos MySQL.
Funcionalidad:
Define la función creacion_db para conectar a la base de datos skyroute con usuario root y contraseña admin.
Incluye ejemplos comentados para crear la base de datos y las tablas necesarias (clientes, destinos, ventas).
3. Funciones_cliente.py
Propósito: Gestión de clientes.
Funcionalidad:
Crear, insertar, mostrar, modificar y eliminar clientes en la base de datos.
Utiliza la función de conexión de Config_DB.
4. Funciones_destino.py
Propósito: Gestión de destinos.
Funcionalidad:
Crear, insertar, mostrar, modificar y eliminar destinos en la base de datos.
Utiliza la función de conexión de Config_DB.
Estructura general y relaciones
El sistema está orientado a la gestión de una agencia de viajes, permitiendo:
Registrar y administrar clientes.
Registrar y administrar destinos.
Registrar ventas de pasajes asociando clientes y destinos.
Visualizar ventas y anularlas ("botón de arrepentimiento").
Toda la información se almacena en una base de datos MySQL llamada skyroute.
La conexión a la base de datos está centralizada en Config_DB.py.
Las operaciones CRUD (crear, leer, actualizar, eliminar) para clientes y destinos están separadas en módulos específicos.
Resumen de tablas de la base de datos
clientes:

id, razon_social, cuit, email
destinos:

id, ciudad, pais, costo
ventas:

id, cliente, destino, fecha, costo, estado
Observaciones
El sistema está pensado para ejecutarse en consola.
Los datos se almacenan en MySQL, no en memoria.
El código está modularizado para facilitar el mantenimiento y la ampliación de funcionalidades.#
