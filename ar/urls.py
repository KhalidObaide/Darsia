from django.urls import path
from . import views as ar_views

urlpatterns = [
    # darsia.com/ar/
    path('', ar_views.index, name='index'),

    # darsia.com/ar/signup
    path('signup/', ar_views.signup, name='signup'),

    # darsia.com/ar/<username>/
    path('<int:userid>/', ar_views.user, name='user'),

    # darsia.com/ar/fladjsidjfasdklfjas
    path('<str:code>/', ar_views.confirm, name='index'),
]