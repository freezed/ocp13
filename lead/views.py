from django.shortcuts import render, redirect

def index(request):

    if request.user.is_anonymous:
        return redirect('login')

    return render(request, 'lead/index.html')
