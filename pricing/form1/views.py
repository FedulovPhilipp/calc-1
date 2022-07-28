from django.shortcuts import render
from .forms import PriceCalc


def show_form(request):
    if request.method == "POST":
        route_date = request.POST.get('route_date')
        bus_class = request.POST.get('bus_class')
        distance = request.POST.get('distance')
        rate = request.POST.get('rate')
        price = int(rate)*int(distance)*2
        data = {"route_date": route_date, 'bus_class': bus_class, 'distance': distance, 'rate': rate, 'price': price}
        return render(request, 'form2.html', context=data)
    form = PriceCalc()
    return render(request, 'form1.html', {'form': form})
