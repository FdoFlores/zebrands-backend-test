from django.urls import path
from .views import IndexView

urlpatterns = [
    # Home page URL
    path('', IndexView.as_view(), name='index'),
]