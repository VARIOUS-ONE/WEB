from django.urls import path
from base.views import black_views as views

urlpatterns = [
    path('', views.getBlackUsers, name='users'),
]