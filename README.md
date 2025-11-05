# ProyectoClubDeFutbol
Simulo un club de futbol utilizando lenguajes como python, html, css entre otros.

LINK VIDEO: https://youtu.be/XMwx_H3ByIs

Para ejecutar el siguiente proyecto hay que seguir los siguientes pasos:

1. Abrir una terminar en tu computadora y clonar el repositorio desde el siguente link tipo SSH: 
        git@github.com:mateocaputo/ProyectoClubDeFutbol.git con el comendo git clone <link>
2. Luego posicionandonos sobre el directorio ingresar el comando:
        code . (nos va a abrir el visual studio code)
3. En caso de que no esté creado el entorno virtual hay que ingresar el comando:
        python -m venv entorno_virtual
    Si está creado simplemente accedemos al mismo con:
        nombre_entorno/Scripts/activate
4. Una vez hecho esto, hay que instalar los requirements
        pip install -r requirements.txt (para que funcione con las versiones que utilizó el dev)
5. Luego ya podemos crear en caso de que no esté, la DB.
        Primero el comando: python manage.py makemigrations
        Luego el comando  : python manage.py migrate
6. Y listo, con eso ya estamos listos para correr el proyecto con el comando:
        python manage.py runserver

-----------------------------------------------------------------------------------------------------
En la parte de views.py va a estar toda la lógica, en models.py cada uno de los modelos que cree Jugadores, Patrocinadores y Mobiliario que luego va a formar parte de mi DB. En url.py de la carpeta club van a estar todas las urls que utilicé por ahora y entemplates van a estar todos los html.

En forms va a estar toda la estructura de cada formulario que armé para cada uno de los modelos.
