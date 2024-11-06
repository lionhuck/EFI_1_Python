# LEPAGO

LEPAGO es una aplicación creada por León, Pablo y Gonzalo, que permite crear y editar (aunque aún no eliminar) elementos en una base de datos en localhost.

## Instalación

  
1. Hacer un git clone del repositorio en tu computadora local:
```bash
  git clone https://github.com/lionhuck/EFI_1_Python
```
2. Crear un entorno virtual en tu computadora usando:
```bash
  python3 -m venv nombre_del_entorno
  # Recomendación: Usar `env` o `venv` como nombre del entorno.
```
3. Activar el entorno virtual:
```bash
  source nombre_del_entorno/bin/activate
```
4. Instalar los requerimientos dentro del entorno usando:
```bash
  pip install -r requirements.txt
```
5. Instalar XAMPP en una terminal aparte: https://www.apachefriends.org/es/download.html.

6. Iniciar XAMPP en la terminal con:
```bash
  sudo /opt/lampp/lampp start
```
7. Ir a la página http://localhost/dashboard/ y crear en phpMyAdmin una nueva base de datos llamada `celulares`. Esto es importante porque allí se enviarán todos los datos del programa.

8. Inicializar la base de datos por consola usando:
```bash
  flask db init
```
9. Hacer el primer commit de migraciones usando:
```bash
  flask db migrate -m "Mensaje de la migración"
```
10. Correr el comando para aplicar la migración e iniciar la base de datos:
```bash
    flask db upgrade
```
11. Usando la terminal, correr el programa con:
```bash
    flask run --reload
```

# Endpoints de la API

A continuación se describen los principales endpoint de la API con ejemplos de solicitud y respuesta.

## Administrador

### Crear un usuario administrador

- Método: POST
- Endpoint: `/create_admin`
- Cuerpo de solicitud:
  ```bash
  {
    "nombre":"nombre_admin",
    "password":"password_admin"
  }
  ```
Ejemplos de respuesta:
- Si no existe:
  ```bash
  {
    "msg": "Usuario administrador creado exitosamente"
  }
  ```
- Si existe:
  ```bash
  {
    "msg": "Ya existe un usuario administrador"
  }
  ```
## Autenticación

### Obtener token de autenticación

- Método: POST
- Endpoint: `/login`
- Cuerpo de solicitud:
  ```bash
    {
      "nombre": "nombre",
      "password": "password"
    }
  ```
Ejemplo de respuesta:
  ```bash
    {
      "Token": "tu_token_de_autenticación"
    }
  ```
## Usuarios

### Obtener todos los usuarios

- Método: GET
- Endpoint: `/users`
- Cabecera de la solicitud: `Authorization: Token <tu_token_de_autorización>`

Ejemplos de respuesta:
- Si es admin:
  ```bash
    [
        {
          "id": "usuario_id",
          "is_admin": bool,
          "nombre": "nombre_usuario",
          "password": "password_hasheada"
        },
        // Otros usuarios
    ]
  ```
- Si no es admin:
  ```bash
    [
        {
          "nombre": "nombre_usuario"
        },
        // Otros objetos de usuarios
    ]
  ```
## Modelos

### Obtener todos los modelos

- Método: GET
- Endpoint: `/modelo`
- Cabecera de la solicitud: `Authorization: Token <tu_token_de_autorización>`

Ejemplos de respuesta:
- Si es admin:
  ```bash
    [
        {
          "id": "modelo_id",
          "nombre": "nombre_modelo"
        },
        // Otros objetos de modelo 
    ]
    ```
- Si no es admin:
  ```bash
    [
        {
          "nombre": "nombre_modelo"
        },
        // Otros objetos de modelo 
    ]
  ```
## Categorías

### Obtener todas las categorías

- Método: GET
- Endpoint: `/categoria`
- Cabecera de la solicitud: `Authorization: Token <tu_token_de_autorización>`

Ejemplos de respuesta:
- Si es admin:
  ```bash
    [
        {
          "id": "categoria_id",
          "nombre": "nombre_categoria"
        },
        // Otros objetos de categoria 
    ]
    ```
- Si no es admin:
  ```bash
    [
        {
          "nombre": "nombre_categoria"
        },
        // Otros objetos de categoria 
    ]
  ```
Si todo salio bien, podras disfrutar de este impresionante programa hecho, modificado y programado por: Pablo Aldo Amedey Dilena, Gonzalo Nicolas Toledo, Leon Federico Huck.

En cuanto al uso propiamente dicho del programa, la idea principal es poder llegar a la creacion de un celular habiendo antes creado elementos como, piases, fabricantes, proveedores, caracteristicas, etc.
La complejidad del mismo reside en las relaciones entre las tablas y el poder editar las mismas.

Gracias por usar y compartir!
