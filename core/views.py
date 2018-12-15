from django.http import HttpResponse
from django.shortcuts import render


def hopla(request):
    return HttpResponse("Hopla, Seppi bring a Wurschtsalat avec un amer!")
