import random
import string

from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'generator/home.html')


def password(request):
    allowed_symbols = list(string.ascii_lowercase)

    if request.GET.get('uppercase'):
        allowed_symbols.extend(list(string.ascii_uppercase))
    if request.GET.get('numbers'):
        allowed_symbols.extend(list(string.digits))
    if request.GET.get('special'):
        allowed_symbols.extend(list('!@#$%^&*()'))

    password_length = int(request.GET.get('length'))

    password = ''
    for _ in range(password_length):
        password += random.choice(allowed_symbols)

    return render(request, 'generator/password.html', {'password': password})


def about_author(request):
    return render(request, 'generator/about_author.html')
