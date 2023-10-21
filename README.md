#Install Django:
pip install django

# helloworld.py
import sys
from django.conf import settings
from django.urls import re_path
from django.http import JsonResponse
from django.core.management import execute_from_command_line

# Django settings
settings.configure(
    DEBUG=True,
    ROOT_URLCONF=sys.modules[__name__],  # Points to this module
    INSTALLED_APPS=[],
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
    )
)

# View function
def hello_world(request):
    return JsonResponse({"Message": "Hello World!"})

# URL patterns
urlpatterns = [
    re_path(r'^hello-world/$', hello_world),
]

# Main function to execute Django's command-line utility
if __name__ == "__main__":
    execute_from_command_line(sys.argv)

# Run this command 
python  helloworld.py runserver

