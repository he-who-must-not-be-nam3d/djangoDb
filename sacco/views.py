from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect

from sacco.app_forms import CustomerForm, LoginForm
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


def customers(request):
    # data = Customer.objects.all() #ORM select * customers
    customer_list = Customer.objects.all().order_by('id')
    paginator = Paginator(customer_list, 25)  # Show 10 customers per page

    page = request.GET.get('page')
    data = paginator.get_page(page)
    return render(request, 'customers.html', {"customers": data})

def delete_customer(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    customer.delete()
    return redirect('customers')


def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers')
    else:
        form = CustomerForm()
    return render(request, 'customer_form.html', {'form': form})

# pip install django-crispy-forms
# pip install crispy-bootstrap5
def login_user(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login_form.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('customers')


def logout_user(request):
    logout(request)
    return redirect('login')