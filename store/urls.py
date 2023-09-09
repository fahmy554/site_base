from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name=''),
    # path('', views.index, name=''),
    path('test/', views.tgarba, name=''),
    path('<slug:slug>/', views.single_store, name='single_store'),
    # path('<slug:slug>', views.index, name=''),
]