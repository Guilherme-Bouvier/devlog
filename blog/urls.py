from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre_nos, name='sobre_nos'),
    path('artigo/<int:id>/', views.artigo_detalhe, name='detalhe_artigo'),
    path("uc1/", views.uc1, name="uc1"),
    path("uc2/", views.uc2, name="uc2"),
    path("uc3/", views.uc3, name="uc3"),
    path("uc4/", views.uc4, name="uc4"),
    path("uc5/", views.uc5, name="uc5"),
]