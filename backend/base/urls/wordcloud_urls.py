from django.urls import path
from base.views import wordcloud_views as views

urlpatterns = [
    path('', views.visualization_wordcloud, name='visualization_wordcloud'),
]
