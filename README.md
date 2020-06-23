# [Veinti](https://hardcore-mclean-eab0d9.netlify.app/)

Proyecto en producción de Veinti para el servidor.

## ¿Qué es Veinti?

Este proyecto se basa en el desarrollo de una red social desde cero, la idea inicial está inspirada en la antigua red social española “Tuenti” para ello desarrollaremos todos los servicios que corresponden con este tipo de aplicación, así como, subida de imágenes, compartir momentos con tus amigos, mensajería privada... 
El proyecto constará de dos aplicaciones, front-end y back-end, que serán desarrolladas en VueJS y Django respectivamente, usaremos una base de datos SQLite. Nuestro backend se encargará de suministrar una Api que será consumida por el cliente haciendo así una red social moderna y SPA. 
### Sólo puedes acceder a Veinti teniendo invitación ya que es una red social privada
![Imagen de inicio de Veinti](https://github.com/bmacm9/DIST-VEINTI/blob/master/static/0.png?raw=true)


### Esta red social no pretende ser una red social real, solo es un proyecto para rememorar grandes momentos

![Imagen de perfil de Veinti](https://github.com/bmacm9/DIST-VEINTI/blob/master/static/8.png?raw=true)


# Instrucciones para la instalación

1- Primero necesitaremos crear un entorno virtual con python, para ello usaremos el comando python3 –m vevn myenv esto creará un entorno virtual en el que se instalará nuestra aplicación, se nos habrá creado un directorio con el nombre myenv, en el que entraremos. 

2- Activaremos el entorno, para ello, utilizaremos el comando source bin/actívate. Aparecerá el nombre del entorno entre paréntesis, haciéndonos ver que está correcto. 

3- Después procederemos a instalar las dependencias que necesitamos a través de pip, ejecutaremos pip install djangorestframework, pip install django-corsheaders, pip install pillow. 

4- Una vez están las dependencias instaladas podremos irnos al directorio de la aplicación y ejecutar el servidor con el comando python3 manage.py runserver.
