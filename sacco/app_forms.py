from django import forms

from sacco.models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name','email', 'gender', 'dob', 'weight']
        widgets = {
            'dob' : forms.DateInput(attrs={'class': 'datepicker', 'type': 'date'})
        }