from django.urls import path
from . import views

app_name = 'car'
urlpatterns = [
    path('', views.add, name='add'),
    path('list/', views.list, name='list'),
    path('delete/', views.delete, name='delete')
]
