from django.urls import path
from base.views import board_views as views

urlpatterns = [
    path('list/', views.board_list),
]