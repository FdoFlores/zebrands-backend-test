from typing import Optional
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from ..api.models import Product, Brand, Buyout
from django.contrib.auth.models import Group
import requests
from .forms import *


# Create your views here.
class DashboardAdmin(ListView):
    model = Product
    template_name = "frontend/index_admin.html"
    context_object_name = 'products'
    paginate_by = 10

class IndexViewAnon(ListView):
    model = Product
    template_name = "frontend/index_anon.html"
    context_object_name = 'products'
    paginate_by = 10

class LogoutViewCustom(LogoutView):
    def get_next_page(self):
        next_page = reverse_lazy('login')
        return next_page

class LoginViewCustom(LoginView):
    template_name = 'frontend/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        try:
            admins = Group.objects.get(name='Admin')
        except Group.DoesNotExist:
            return None
        admins = admins.user_set.all()
        if self.request.user in admins:
            return reverse_lazy('index_admin')
        else:
            return reverse_lazy('index_anon')
        
def CreateBrandView(request):
    if request.method == 'POST':
        form = CreateBrandForm(request.POST)
        if form.is_valid():
            data = {
                'brand': form.cleaned_data['brand'],
            }

            response = requests.post('http://127.0.0.1:8000/api/create_brand/', data=data)

            if response.status_code == 201:
                return redirect('create_brand_front')
            else:
                return redirect('index_admin')
    else:
        form = CreateBrandForm()
    brands = Brand.objects.all().order_by('id')
    context = {
        'form': form,
        'brands': brands
    }
    return render(request, 'Brands/create.html', context)


def DeleteBrandView(request, pk):
    if request.method == 'POST':
        response = requests.delete(f'http://127.0.0.1:8000/api/delete_brand/{pk}')

        if response.status_code == 204:
            return redirect('create_brand_front')
        else:
            print(response.text)
            return redirect('index_admin')

    return render(request, 'Brands/delete.html', {'pk': pk})


def UpdateBrandView(request, pk):
    # Get the brand object based on the brand_id
    brand = Brand.objects.get(pk=pk)

    if request.method == 'POST':
        form = UpdateBrandForm(request.POST, instance=brand)
        if form.is_valid():
            data = {
                'brand': form.cleaned_data['brand'],
            }

            response = requests.put(f'http://127.0.0.1:8000/api/update_brand/{pk}', data=data)

            if response.status_code == 200:
                return redirect('create_brand_front')
            else:
                print(response.text)
                return redirect('index_admin')
    else:
        form = UpdateBrandForm(instance=brand)

    brands = Brand.objects.all()
    context = {
        'form': form,
        'brands': brands
    }
    return render(request, 'Brands/update.html', context)

def CreateProductView(request):
    if request.method == 'POST':
        form = CreateProductForm(request.POST)
        if form.is_valid():
            data = {
                'sku': form.cleaned_data['sku'],
                'name': form.cleaned_data['name'],
                'price': form.cleaned_data['price'],
                'brand': form.cleaned_data['brand'].id,
            }

            response = requests.post('http://127.0.0.1:8000/api/create_product/', data=data)

            if response.status_code == 201:
                return redirect('create_product_front')
            else:
                return redirect('index_admin')
    else:
        form = CreateProductForm()

    products = Product.objects.all().order_by('id')
    context = {
        'form': form,
        'products': products
    }
    return render(request, 'Products/create.html', context)

def DeleteProductView(request, pk):
    if request.method == 'POST':
        response = requests.delete(f'http://127.0.0.1:8000/api/delete_product/{pk}')

        if response.status_code == 204:
            return redirect('create_product_front')
        else:
            print(response.text)
            return redirect('index_admin')

    return render(request, 'Products/delete.html', {'pk': pk})

def UpdateProductView(request, pk):
    # Get the product object based on the pk
    product = Product.objects.get(pk=pk)

    if request.method == 'POST':
        form = CreateProductForm(request.POST, instance=product)
        if form.is_valid():
            data = {
                'sku': form.cleaned_data['sku'],
                'name': form.cleaned_data['name'],
                'price': form.cleaned_data['price'],
                'brand': form.cleaned_data['brand'].id,
            }

            response = requests.put(f'http://127.0.0.1:8000/api/update_product/{pk}/', data=data)

            if response.status_code == 200:
                return redirect('create_product_front')
            else:
                print(response.text)
                return redirect('index_admin')
    else:
        form = CreateProductForm(instance=product)

    products = Product.objects.all().order_by('id')
    context = {
        'form': form,
        'brands': products
    }
    return render(request, 'Products/update.html', context)

def CreateUserView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            data = {
                'username': form.cleaned_data['username'],
                'email': form.cleaned_data['email'],
                'password': form.cleaned_data['password'],
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
            }

            response = requests.post('http://127.0.0.1:8000/api/create_user/', data=data)

            if response.status_code == 201:
                return redirect('create_user_front')
            else:
                return redirect('index_admin')
    else:
        form = UserCreationForm()

    users = User.objects.filter(deleted=None).order_by('id')
    context = {
        'form': form,
        'users': users
    }
    return render(request, 'Users/create.html', context)

def DeleteUserView(request, pk):
    if request.method == 'POST':
        response = requests.delete(f'http://127.0.0.1:8000/api/delete_user/{pk}')

        if response.status_code == 204:
            return redirect('create_user_front')
        else:
            print(response.text)
            return redirect('index_admin')

    return render(request, 'Users/delete.html', {'pk': pk})

def UpdateUserView(request, pk):
    # Get the user object based on the pk
    user = User.objects.get(pk=pk)

    if request.method == 'POST':
        form = UserCreationForm(request.POST, instance=user)
        if form.is_valid():
            data = {
                'username': form.cleaned_data['username'],
                'email': form.cleaned_data['email'],
                'password': form.cleaned_data['password'],
            }

            response = requests.put(f'http://127.0.0.1:8000/api/update_user/{pk}', data=data)

            if response.status_code == 200:
                return redirect('create_user_front')
            else:
                print(response.text)
                return redirect('index_admin')
    else:
        form = UserCreationForm(instance=user)

    users = User.objects.all().order_by('id')
    context = {
        'form': form,
        'users': users
    }
    return render(request, 'Users/update.html', context)

def CreateBuyoutView(request):
    buyouts = Buyout.objects.filter(deleted=None).order_by('id')
    context = {
        'buyouts': buyouts
    }
    return render(request, 'Buyouts/create.html', context)

def CreateBuyoutAnonView(request):
    if request.method == 'POST':
        form = BuyoutForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('index_anon')
    else:
        form = BuyoutForm(request.user)

    buyouts = Buyout.objects.filter(deleted=None).order_by('id')
    context = {
        'form': form,
        'buyouts': buyouts
    }
    return render(request, 'frontend/create_buyout.html', context)