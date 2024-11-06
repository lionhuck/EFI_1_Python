La aplicacion se llama LEPAGO (Leon, Pablo, Gonzalo), en la cual se va a poder crear y editar (eliminar aun no) elementos en una base de datos del local host.

Instalacion: 
1. Hacer un git clone del repositorio en tu computadora local.
2. Crearse un entorno virtual en tu computadora virtual usando el comando python3 -m venv (nombre del entorno, recomendable env o venv).
3. Una vez creado el entorno, activarlo usando source env(nombre del entorno)/bin/activate
4. Instalar los requerimientos dentro del entorno usando el comando: pip install -r requeriments.txt
5. Instalar XAMPP en una terminal aparte: https://www.apachefriends.org/es/download.html.
6. Iniciar xampp en la terminal medianto el comando: sudo /opt/lampp/lampp start.
7. Ir a la pagina: http://localhost/dashboard/ y crear en phpmyadmin una nueva base de datos llamada celulares. Esto es importante porque alli se enviaran todos los datos del programa.
8. Inicializar la base de datos por consola usando: flask db init
9. Hacer el primer commit de migraciones usando: flask db migrate -m "Mensaje de la migracion"
10. Correr el comando: flask db upgrade, para aplicar la migracion e iniciar la base de datos.
11. Usando la terminal correr el programa usando el comando: flask run --reload.

A continuación se describen los principales endpoint de la API con ejemplos de solicitud y respuesta.

Administrador

Crear un usuario administrador

Método: POST
Endpoint: /create_admin
Cuerpo de solicitud:
{
  "nombre":"nombre_admin",
  "password":"password_admin"
}

Ejemplos de respuesta:
Si no existe:
{
  "msg": "Usuario administrador creado exitosamente"
}
Si existe:
{
  "msg": "Ya existe un usuario administrador"
}


Autenticación

Obtener token de autenticación

Método: POST
Endpoint: /login
Cuerpo de solicitud:
{
  "nombre":"nombre",
  "password":"password"
}

Ejemplo de respuesta:
{
  "Token": "tu_token_de_autenticación"
}


Usuarios

Obtener todos los usuarios

Método: GET
Endpoint: /users
Cabecera de la solicitud: Authorization: Token <tu_token_de_autorización>
Ejemplos de respuesta:
Si es admin:
[
    {
      "id": "usuario_id",
      "is_admin": bool,
      "nombre":"nombre_usuario",
      "password": "password_hasheada"
    },
    // Otros usuarios
]
Si no es admin:
[
    {
      "nombre":"nombre_usuario"
    },
    // Otros objetos de usuarios
]


Modelos

Obtener todos los modelos

Método: GET
Endpoint: /modelo
Cabecera de la solicitud: Authorization: Token <tu_token_de_autorización>
Ejemplos de respuesta:
Si es admin:
[
    {
      "id": "modelo_id",
      "nombre":"nombre_modelo"
    },
    // Otros objetos de modelo 
]
Si no es admin:
[
    {
      "nombre":"nombre_modelo"
    },
    // Otros objetos de modelo 
]


Categorías

Obtener todas las categorías

Método: GET
Endpoint: /categoria
Cabecera de la solicitud: Authorization: Token <tu_token_de_autorización>
Ejemplos de respuesta:
Si es admin:
[
    {
      "id": "categoria_id",
      "nombre":"nombre_categoria"
    },
    // Otros objetos de categoria 
]
Si no es admin:
[
    {
      "nombre":"nombre_categoria"
    },
    // Otros objetos de categoria 
]

Si todo salio bien, podras disfrutar de este impresionante programa hecho, modificado y programado por: Pablo Aldo Amedey Dilena, Gonzalo Nicolas Toledo, Leon Federico Huck.

En cuanto al uso propiamente dicho del programa, la idea principal es poder llegar a la creacion de un celular habiendo antes creado elementos como, piases, fabricantes, proveedores, caracteristicas, etc.
La complejidad del mismo reside en las relaciones entre las tablas y el poder editar las mismas.

Gracias por usar y compartir!
