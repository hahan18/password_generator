import random
import string

from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'generator/home.html')


def password(request):
    allowed_symbols = [letter for letter in string.ascii_lowercase]

    if request.GET.get('uppercase'):
        allowed_symbols.extend([letter for letter in string.ascii_uppercase])
    if request.GET.get('numbers'):
        allowed_symbols.extend([digit for digit in string.digits])
    if request.GET.get('special'):
        allowed_symbols.extend([special for special in '!@#$%^&*()'])

    password_length = int(request.GET.get('length'))

    password = ''
    for _ in range(password_length):
        password += random.choice(allowed_symbols)

    return render(request, 'generator/password.html', {'password': password})
