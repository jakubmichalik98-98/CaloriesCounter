from django.shortcuts import render
from .forms import UserRegisterForm
from django.contrib import messages
from django.http import HttpResponseRedirect


def register(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}")
            return HttpResponseRedirect('/')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
