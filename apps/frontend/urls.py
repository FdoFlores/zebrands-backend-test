from django.urls import path
from .views import *

urlpatterns = [
    # Home page URL
    path('index/', IndexViewAnon.as_view(), name='index_anon'),
    path('dashboard/', DashboardAdmin.as_view(), name='index_admin'),

    # BRANDS
    path('create_brand/', CreateBrandView, name='create_brand_front'),
    path('delete_brand/<int:pk>', DeleteBrandView, name='delete_brand_front'),
    path('update_brand/<int:pk>', UpdateBrandView, name='update_brand_front'),

    # Products
    path('create_product/', CreateProductView, name='create_product_front'),
    path('delete_product/<int:pk>/', DeleteProductView, name='delete_product_front'),
    path('update_product/<int:pk>/', UpdateProductView, name='update_product_front'),

    #Users
    path('create_user/', CreateUserView, name='create_user_front'),
    path('delete_user/<int:pk>/', DeleteUserView, name='delete_user_front'),
    path('update_user/<int:pk>/', UpdateUserView, name='update_user_front'),

    # Buyout
    path('create_buyout/', CreateBuyoutView, name='create_buyout_front'),
    path('create_buyout_anon/', CreateBuyoutAnonView, name='create_buyout_anon'),


    #LOGIN
    path('', LoginViewCustom.as_view(), name='login'),
    path('login/', LoginViewCustom.as_view(), name='login'),
    path('logout/', LogoutViewCustom.as_view(), name='logout'),

]