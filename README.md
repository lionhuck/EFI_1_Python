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

12. Si todo salio bien, podras disfrutar de este impresionante programa hecho, modificado y programado por: Pablo Aldo Amedey Dilena, Gonzalo Nicolas Toledo, Leon Federico Huck.

En cuanto al uso propiamente dicho del programa, la idea principal es poder llegar a la creacion de un celular habiendo antes creado elementos como, piases, fabricantes, proveedores, caracteristicas, etc.
La complejidad del mismo reside en las relaciones entre las tablas y el poder editar las mismas.



Gracias por usar y compartir!
