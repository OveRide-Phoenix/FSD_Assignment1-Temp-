
from django.shortcuts import render
import math

def index(request):
    n1 = 5
    square = n1 ** 2
    factorial = math.factorial(n1)
    return render(request, 'app1/index.html', {
        'square': square,
        'factorial': factorial
    })
