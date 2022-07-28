from django.shortcuts import render
from .forms import PriceCalc


def show_form(request):
    return render(request, 'form1.html', {'form': PriceCalc})
