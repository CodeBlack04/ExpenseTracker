from django.urls import path

from . import views

app_name = 'transaction'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('new/', views.new, name='new'),
    path('list/', views.list, name='list'),
    path('incomes/', views.incomes, name='incomes'),
    path('expenses/', views.expenses, name='expenses'),
]