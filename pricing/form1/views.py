from django.shortcuts import render
from .forms import PriceCalc


def show_form(request):
    if request.method == "POST":
        rates = [('0', 1, 'Микроавтобус эконом 17-18 мест'),
                 ('1', 1.08, 'Микроавтобус комфорт 19-20 мест'),
                 ('2', 1.2, 'Микроавтобус представительский 19-20 мест'),
                 ('3', 1.3, 'Аврора 29-35 мест'),
                 ('4', 1.4, 'Ютонг или Хайгер 35-40 мест'),
                 ('5', 1.6, 'Ютонг или Хайгер 41-45 мест'),
                 ('6', 1.7, 'Ютонг или Хайгер 47 - 51 мест'),
                 ('7', 2.,  'Хайгер 55 мест'),
                 ]
        base_rate = [1200, 30]
        route_date = request.POST.get('route_date')
        bus_class = int(request.POST.get('bus_class'))
        distance = int(request.POST.get('distance'))
        duration = int(request.POST.get('duration'))
        delivery = int(request.POST.get('delivery'))
        accomodation = int(request.POST.get('accomodation'))
        drivers_fee = int(request.POST.get('drivers_fee'))
        extra = int(request.POST.get('extra'))
        vihicle_class = rates[bus_class][2]
        milage = distance * 2
        milage_cost = base_rate[1] * milage * rates[bus_class][1]
        duration_cost = base_rate[0] * duration * rates[bus_class][1]
        delivery_cost = base_rate[0] * delivery * rates[bus_class][1]
        full_cost = int((milage_cost + duration_cost + delivery_cost + accomodation + drivers_fee) * (1 + extra/100))

        data = {"route_date": route_date, 'drivers_fee': drivers_fee, 'delivery_cost': delivery_cost,
                'duration_cost': duration_cost, 'extra': extra, 'vihicle_class': vihicle_class, 'duration': duration,
                'milage_cost': milage_cost, 'accomodation': accomodation,  'milage': milage, 'full_cost': full_cost}
        return render(request, 'form2.html', context=data)
    form = PriceCalc()
    return render(request, 'form1.html', {'form': form})
