from django.urls import path
from . import views

urlpatterns = [
    path('', views.stores, name='stores'),
    # path('', views.index, name=''),
    path('test/', views.tgarba, name='tgarba'),
    path('<str:slug>/', views.single_store, name='single_store'),
    # path('(?P<slug>[-\w]+)/', views.single_store, name='single_store'),
    # path('<slug:slug>', views.index, name=''),
]