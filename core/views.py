from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import SignupForm


# Create your views here.

def Signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/')
        
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form,
        'title': 'SignUp'
    })



