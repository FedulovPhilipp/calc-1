from django import forms


class PriceCalc(forms.Form):
    route_date = forms.DateField(help_text="Enter a date")