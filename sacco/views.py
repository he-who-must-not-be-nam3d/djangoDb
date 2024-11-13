from django.http import HttpResponse
from django.shortcuts import render

from sacco.models import Customer, Deposits


# Create your views here.
def test(request):
    # c1 = Customer(first_name='Ali', last_name='Hassan', email='alihassan@x.com', dob='2000-02-19', gender='Male')
    # c1.save()
    # c2 = Customer(first_name='Missy', last_name='Qare', email='qaremissy@x.com', dob='2000-12-09', gender='Female')
    # c2.save()
    customer_count = Customer.objects.count()

    c1 = Customer.objects.get(id=1)
    print(c1)

    d1 = Deposits(amount=1000, status=True, customer=c1)
    d1.save()

    deposit_count = Deposits.objects.count()
    return HttpResponse(f"Ok, Done. We have {customer_count} customer(s) and {deposit_count} deposit(s)")