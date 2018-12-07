from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

def signup(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            return redirect('home')

    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})

# def pass_change(request):
        # return render(request, 'registration/pass_change.html')

# def pass_reset(request):
        # return render(request, 'registration/pass_reset.html')
