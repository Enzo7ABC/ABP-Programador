# ABP-Programador
NOMBRE DEL PROYECTO: Prototipo "Sistema de Gestión de Pasajes Aéreos para SkyRoute S.R.L."
Estudiantes:
● BARILES, JULIETA BELÉN DNI 38.329.962 
● CABANA, ENZO ALAN BAIL DNI 36.048.872 
● CABRAL, LEANDRO ELÍAS DNI 43.233.136 
● DELFINI, DONATA VIRGINIA DNI 27.296.444

NOMBRE DE USUARIO DE GITHAUB: Enzo7ABC

BREVE DESCRIPCION DEL PROYECTO: El proyecto responde a la necesidad de digitalizar y automatizar la gestión de ventas de SkyRoute, 
mejorando la experiencia de usuario y asegurando el cumplimiento de normativas legales sobre cancelación de compras.

-----------------------------------------------------------------------------------------------------------------
COMO EJECUTAR EL PROYECTO "Skyroute":
Para ejecutar el proyecto, sigue estos pasos básicos:

1. **Tener prendido MySQL** en tu máquina, y que exista la base de datos `skyroute` con sus tablas.  
   Para crearla usar los comandos comentados en Config_DB.py desde un cliente MySQL.

2. **Instalar las dependencias** necesarias ejecutando en la terminal:
```
pip install mysql-connector-python
```

3. **Ejecutar el archivo principal** del proyecto desde la terminal:
```
python Main.py
```

Esto iniciará el menú principal del sistema y podrás comenzar a usar la aplicación.


------------------------------------------------------------------------------------------------------------


### Archivos principales del proyecto ABP

#### 1. Main.py
- **Propósito:** Es el archivo principal del sistema de gestión de pasajes "SkyRoute S.R.L.".
- **Funcionalidad:**  
  - Menú principal con opciones para gestionar clientes, destinos, ventas y el "botón de arrepentimiento".
  - Utiliza funciones de los módulos `Funciones_cliente` y `Funciones_destino`.
  - Controla el flujo del programa y la interacción con el usuario.

#### 2. Config_DB.py
- **Propósito:** Configuración y conexión a la base de datos MySQL.
- **Funcionalidad:**  
  - Define la función `creacion_db` para conectar a la base de datos `skyroute` con usuario `root` y contraseña `admin`.
  - Incluye ejemplos comentados para crear la base de datos y las tablas necesarias (`clientes`, `destinos`, `ventas`).

#### 3. Funciones_cliente.py
- **Propósito:** Gestión de clientes.
- **Funcionalidad:**  
  - Crear, insertar, mostrar, modificar y eliminar clientes en la base de datos.
  - Utiliza la función de conexión de `Config_DB`.

#### 4. Funciones_destino.py
- **Propósito:** Gestión de destinos.
- **Funcionalidad:**  
  - Crear, insertar, mostrar, modificar y eliminar destinos en la base de datos.
  - Utiliza la función de conexión de `Config_DB`.
 
------------------------------------------------------------------------------

### Estructura general y relaciones

- El sistema está orientado a la gestión de una agencia de viajes, permitiendo:
  - Registrar y administrar clientes.
  - Registrar y administrar destinos.
  - Registrar ventas de pasajes asociando clientes y destinos.
  - Visualizar ventas y anularlas ("botón de arrepentimiento").
- Toda la información se almacena en una base de datos MySQL llamada `skyroute`.
- La conexión a la base de datos está centralizada en `Config_DB.py`.
- Las operaciones CRUD (crear, leer, actualizar, eliminar) para clientes y destinos están separadas en módulos específicos.

------------------------------------------------------------------------------
### Resumen de tablas de la base de datos

- **clientes:**  
  - id, razon_social, cuit, email

- **destinos:**  
  - id, ciudad, pais, costo

- **ventas:**  
  - id, cliente, destino, fecha, costo, estado

---

### Observaciones

- El sistema está pensado para ejecutarse en consola.
- Los datos se almacenan en MySQL, no en memoria.
- El código está modularizado para facilitar el mantenimiento y la ampliación de funcionalidades.

------------------------------------------------------------------------------------------------------------------

