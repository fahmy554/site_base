from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name=''),
    path('test/', views.tgarba, name=''),
    # path('<slug:slug>', views.index, name=''),
]