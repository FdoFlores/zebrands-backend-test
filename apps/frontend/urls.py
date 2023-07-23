from django.urls import path
from .views import IndexView, LoginViewCustom, LogoutView

urlpatterns = [
    # Home page URL
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginViewCustom.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]