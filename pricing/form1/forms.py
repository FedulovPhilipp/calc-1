from django import forms


class PriceCalc(forms.Form):
    route_date = forms.DateField(help_text="Дата поездки")
    description = forms.CharField(help_text="Заказ")
    distance = forms.IntegerField(help_text="Расстояние до конечной точки в км", required=False, initial=0)
    duration = forms.IntegerField(help_text="Продолжительность работы в часах", required=False, initial=0)
    delivery = forms.IntegerField(help_text='Подача к месту заказа в часах', required=False, initial=0)

    vehicle_class = [('0', 'Микроавтобус эконом 17-18 мест'),
                     ('1', 'Микроавтобус комфорт 19-20 мест'),
                     ('2', 'Микроавтобус представительский 19-20 мест'),
                     ('3', 'Аврора 29-35 мест'),
                     ('4', 'Ютонг или Хайгер 35-40 мест'),
                     ('5', 'Ютонг или Хайгер 41-45 мест'),
                     ('6', 'Ютонг или Хайгер 47 - 51 мест'),
                     ('7', 'Хайгер 55 мест'),
                     ]

    bus_class = forms.ChoiceField(choices=vehicle_class, help_text="Класс ТС")
    accomodation = forms.IntegerField(help_text="Проживание водителей в рублях", required=False, initial=0)
    drivers_fee = forms.IntegerField(help_text="Командировочные водителей в рублях", required=False, initial=0)
    extra = forms.IntegerField(help_text="Наценка в процентах (если скидка, со знаком -)", required=False, initial=0)



