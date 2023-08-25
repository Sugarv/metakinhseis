from django.urls import path
from .views import login_request, logout_user

urlpatterns = [
  path("login/", login_request, name="login"),
  path('logout/', logout_user, name='logout_user')
]