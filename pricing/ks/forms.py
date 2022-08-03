from django import forms


class KsCalc(forms.Form):
    route_date = forms.DateField(help_text="Дата поездки")
    vehicle_class = [('0', 'Микроавтобус эконом 17-18 мест'),
                     ('1', 'Микроавтобус комфорт 19-20 мест'),
                     ('2', 'Микроавтобус представительский 19-20 мест'),
                     ('3', 'Аврора 29-35 мест'),
                     ('4', 'Ютонг или Хайгер 35-40 мест'),
                     ('5', 'Ютонг или Хайгер 41-45 мест'),
                     ('6', "Ютонг или Хайгер 47 - 51 мест"),
                     ('7', 'Хайгер 55 мест'),
                     ]
    bus_class = forms.ChoiceField(choices=vehicle_class, help_text="Класс ТС")
    is_saturday = forms.BooleanField(help_text="Суббота", required=True)




