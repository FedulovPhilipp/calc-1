from django import forms


class PriceCalc(forms.Form):
    route_date = forms.DateField(help_text="Дата поездки")
    bus_class = forms.CharField(help_text="Класс ТС")
    distance = forms.IntegerField(help_text="Расстояние до конечной точки")
    rate = forms.IntegerField(help_text="Тариф")
