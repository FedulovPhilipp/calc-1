from django.shortcuts import render
from .forms import KsCalc


def show_ks(request):
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
        is_saturday = request.POST.get('is_saturday')
        ks = .3
        data = {"route_date": route_date, 'ks': ks}
        return render(request, 'form_ks.html', context=data)
    form = KsCalc()
    return render(request, 'ks.html', {'form': form})
