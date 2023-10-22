from django.http import JsonResponse

def hello_world(request):
    return JsonResponse({"Message": "Hello World!"})
