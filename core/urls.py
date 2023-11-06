from django.urls import path
from django.contrib.auth import views as authviews

from . import views
from transaction import views as transaction_view
from .forms import LoginForm


app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.Signup, name='signup'),
    path('login/', authviews.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', authviews.LogoutView.as_view(), name='logout'),
]