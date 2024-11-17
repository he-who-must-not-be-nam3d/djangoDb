from django import forms

from sacco.models import Customer

GENDER_CHOICES = {'Male': "Male", 'Female': "Female"}
class CustomerForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name','email', 'gender', 'dob', 'weight']
        widgets = {
            'dob' : forms.DateInput(attrs={'class': 'datepicker', 'type': 'date'})
        }