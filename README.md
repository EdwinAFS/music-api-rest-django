# Catalogo

## Python 3.8.0

* Instale las dependencias usando **pip install -r requerimientos.txt**
* Migrar la base de datos sqlite3 **python manage.py migrate**
* Iniciar el servidor **python manage.py runserver**

## Administracion

* En consola ingrese el comando **python manage.py createsuperuser** y a continuacion cree un usuario
* Ingrese a la ruta **localhost:port/admin** y realice el login con el usuario que acabo de crear
* Puede navegar y realizar cualquier cambio ya que usted es admin

## Token de autenticacion
Para realizar una peticion en cualquier url a excepcion del login, se debe tener agregado en un header Authorization : Token *AquiTokenGeneradoEnLogin*

## Rutas

* Albumnes
    * api/albumnes/
    * api/albumnes/top
    * api/albumnes/<int:pk>
    * api/albumnes/<int:pk>/canciones

* Artistas
    * api/artistas/<int:pk>
    * api/artistas/

* Canciones
    * api/canciones/<int:pk>
    * api/canciones/

* Lista de reproduccion
    * api/lista-reproduccion/<int:pk>
    * api/lista-reproduccion/

* Generos
    * api/generos/

* herramientas como informacion de los combos
    * api/utilidades/generos
    * api/utilidades/clasificaciones
    * api/utilidades/ciudades
    * api/utilidades/lenguajes

* control de la autenticacion
    * api/usuario/registration
    * api/usuario/logout
    * login/


