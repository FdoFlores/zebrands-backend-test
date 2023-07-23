from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from rest_framework import generics, renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Brand, User, Product
from .serializers import BrandSerializer, UserSerializer, ProductSerializer

# Brand VIEWS
class BrandCreateView(generics.CreateAPIView):
    serializer_class = BrandSerializer

class BrandUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class BrandListView(generics.ListAPIView):
    queryset = Brand.objects.all().order_by('id')
    serializer_class = BrandSerializer

class BrandDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

# Product VIEWS
class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductSerializer

class ProductUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer

class ProductDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# User VIEWS
class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer

class UserUpdateView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

class UserDeleteView(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer