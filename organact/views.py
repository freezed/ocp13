from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world. Here's the `ocp13` homepage.")
