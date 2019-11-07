# ejercicio3clase

INSTALACION DJANGO
------------------

1º Añadir repositorio de pip--> sudo curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
2º Instalaremos pip--> sudo python get-pip.py
3º Instalaremos django--> sudo pip install django
4º Instalaremos git para poder ejecutar comandos desde shell--> sudo git clone https://github.com/django/django.git
5º pip install -e django/
6º sudo apt-get install python3-pip
-------------------------------------------------------
1. Crea un nuevo proyecto con django

django-admin startproject (nombre_proyecto=proyectodjango)
	
2. Crea una nueva aplicacion llamada home

python manage.py startapp (nombre_aplicacion=home)

3. Modifica el fichero urls.py principal para incluir el fichero urls.py de home

Se crea un archivo en la carpeta /home con nombre urls.py y se copia contenidos. Y en urls.py del principal se añade la lineas:

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls'))
] 

Y en el /home/urls.py

from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('otra/', views.otra, name='otra'),
    path('home/<int:n>', views.detail, name='detail'),
]

4. Crea una ruta en el fichero urls.py de home que lleve a la función index de views (de home)

path('', views.index, name='index')


5. Crea una función llamada index en views.py que devuelva un código html mediante la clase HTTPResponse
   
def index(request):
   return HttpResponse("Index")

6. Comprueba que todo va bien arrancando la aplicación y accediendo desde el navegador

Poner en consola ./manage.py runserver e ir a google chrome y poner 127.0.0.1:8000 o localhost:8000

7. Crea una nueva carpeta dentro del directorio home llamada templates y dentro del directorio templates crea una nueva carpeta llamada home
   


8. Dentro de la carpeta templates/home crea un fichero llamado index.html, mete dentro de ese fichero la estructura básica de una página web (html, head, title, body) e incluye un título (h1) con un texto
  


9. Incluye la aplicación home dentro de la variable INSTALLED_APPS dentro del fichero settings.py
  




10. Modifica la función index de views (home) para que cargue la plantilla home/index.html, pasa un contexto como objeto vacío
   

11. Define una variabe llamada titulo que tenga un texto asociado y pasa esa variable a la vista dentro del contexto
   

12. Haz que el texto del título de la plantilla sea el contenido de la variable de vista titulo
   



13. Crea una nueva ruta que pase un parámetro por URL llamado numero (home/<int:numero>), asignalo a la función detail del fichero views de home y ponle el nombre 'detail'
   


14. Crea una función similar a index llamada detail en el views
   

15. Crea una nueva plantilla llamada detail.html en templates/home, copia el contenido de index.html, pero coloca un título distinto en este nuevo fichero, para que se diferencien
   


16. Modifica la plantilla que se carga desde la función detail para que cargue la plantilla home/detail.html
   

17. Comprueba que carga la plantilla correcta desde el navegador (http://localhost:8000/home/2)
   


18. Pasa la vairable numero entro del contexto de la función detail a la plantilla detail.html
   

19. Modifica la plantilla detail.html para meter la variable número dentro del texto de un título (h3) 
   


20. Comprueba que se ve correctamente el número al modificar la url de entrada (http://localhost:8000/home/2 y http://localhost:8000/home/34)
   


21. Coloca un enlace desde la página principal (index) a la página secundaria (detail) y vicecersa



