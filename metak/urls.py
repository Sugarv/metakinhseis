from django.urls import path
from .views import MetakinhshCreateView, MetakinhshUpdateView, MetakinhshListView
from . import views

urlpatterns = [
    path('list/', MetakinhshListView.as_view(), name='metakinhsh_list'),
    path('add/', MetakinhshCreateView.as_view(), name='metakinhsh_add'),
    path('edit/<int:pk>/', MetakinhshUpdateView.as_view(), name='metakinhsh_edit'),
    path('', views.index, name='home'),
]