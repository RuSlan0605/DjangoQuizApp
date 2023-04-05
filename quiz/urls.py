from django.urls import path
from .views import page_list

urlpatterns = [
    path('', page_list, name='page_list'),
]