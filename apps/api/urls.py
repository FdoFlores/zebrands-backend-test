from django.urls import path
from . import views

urlpatterns = [
    # BRANDS URLS
    path('create_brand/', views.BrandCreateView.as_view(), name='create_brand'),
    path('update_brand/<int:pk>', views.BrandUpdateView.as_view(), name='update_brand'),
    path('get_brands/', views.BrandListView.as_view(), name='get_brands'),
    path('delete_brand/<int:pk>', views.BrandDeleteView.as_view(), name='delete_brand'),

    path('create_product/', views.ProductCreateView.as_view(), name='create_brand'),
    path('update_product/<int:pk>', views.ProductUpdateView.as_view(), name='update_brand'),
    path('get_products/', views.ProductListView.as_view(), name='get_brands'),
    path('delete_product/<int:pk>', views.ProductDeleteView.as_view(), name='delete_brand'),

    # USERS URLS
    path('create_user/', views.UserCreateView.as_view(), name='create_user'),
    path('update_user/<int:pk>', views.UserUpdateView.as_view(), name='update_user'),
    path('get_users/', views.UserListView.as_view(), name='get_user'),
    path('delete_user/<int:pk>', views.UserDeleteView.as_view(), name='delete_user'),
]