# Django
1. Create a new Django project
Open your terminal or command prompt.

Navigate to the directory where you want to create your project.

#Run the following command to create a new Django project:
django-admin startproject HelloWorldProject
Navigate into your project directory:
cd HelloWorldProject
2. Create a new app within the project
#Run the following command to create a new app within your project:

#python manage.py startapp HelloWorldApp
3. Create the 'Hello World' view
Open HelloWorldApp/views.py and write the following code:

from django.http import JsonResponse
def hello_world(request):
    return JsonResponse({"Message": "Hello World!"})
4. Set up the URL for your view
In the HelloWorldProject directory, open urls.py and modify it as follows:

from django.contrib import admin
from django.urls import path
from HelloWorldApp.views import hello_world

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_world),
]
5. Test Your App Locally
#Run the following command:

python manage.py runserver
Open your web browser and go to http://127.0.0.1:8000/hello/ to see your JSON response.
