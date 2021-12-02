from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('apple', views.apple, name='apple'),
    path('papper', views.papper, name='papper'),
    path('lemon', views.lemon, name='lemon'),
    path('carrot', views.carrot, name='carrot'),
]