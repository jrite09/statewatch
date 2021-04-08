from django.urls import path
from . import views
from django.contrib.auth import views as stock_views

# necessary for template tagging
app_name = 'authentication'

urlpatterns = [
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("create", views.create_acc, name="create_account")
]