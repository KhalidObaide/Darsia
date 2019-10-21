from django.urls import path
from . import views as ar_views

urlpatterns = [
    path('', ar_views.index, name='index'),
]