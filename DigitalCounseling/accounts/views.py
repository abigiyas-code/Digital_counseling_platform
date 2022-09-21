from django.shortcuts import render, redirect
from .forms import UserSignUpForm

def index(response):
    return HttpResponse("<h1> Welcome to Be Happy Here! </h1>")
    
def register(request):
    form = UserSignUpForm()
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'form':form
    }
    return render(request, 'accounts/register.html', context)
