from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import ExtendsUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def profil(request):
    return render(request, "users/profil.html")

def register(request):
    if request.method == 'POST':
        form = ExtendsUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Votre compte a ete cree {username}')
            return redirect('home')
    else:
        form = ExtendsUserCreationForm()
    context = {'form': form}
    return render(request, "users/register.html", context)

