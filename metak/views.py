from django.shortcuts import render, redirect
from django.urls import reverse_lazy

# Create your views here.
from django.http import HttpResponse

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import Metakinhsh
from .forms import MetakinhshForm
# from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
import django_tables2 as tables
# from django_tables2 import SingleTableView
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django_filters import FilterSet, DateRangeFilter


# Table for list view (django-tables2)
class MetakinhshTable(tables.Table):
    metak_to = tables.Column(verbose_name='Προορισμός',linkify=("metakinhsh_edit", [tables.A("id")]))

    class Meta:
        model = Metakinhsh
        template_name = "django_tables2/bootstrap4.html"
        fields = ("id", 'metak_to', 'date_from','km','egkrish','pragmat')

# Filter with django-filter package
class MetakinhshFilter(FilterSet):
    date_from = DateRangeFilter()
    class Meta:
        model = Metakinhsh
        fields = {"metak_to": ["contains"], "date_from": ['exact']}

# ListView - uses LoginRequiredMixin to ensure user is authenticated
class MetakinhshListView(LoginRequiredMixin, SingleTableMixin, FilterView):
    login_url = '/metakinhseis/login'
    # do not redirect after login
    def get_redirect_field_name(self, **kwargs):
          return None
    model = Metakinhsh
    table_class = MetakinhshTable
    context_object_name = 'metakinhseis'
    filterset_class = MetakinhshFilter
    # show only current user's records
    def get_queryset(self):
        return super().get_queryset().filter(person=self.request.user.id)
    

class MetakinhshCreateView(LoginRequiredMixin, CreateView):
    login_url = '/metakinhseis/login'
    # do not redirect after login
    def get_redirect_field_name(self, **kwargs):
          return None
    model = Metakinhsh
    form_class = MetakinhshForm
    template_name = 'metak/metakinhsh_form.html'

    # Manipulate form data before saving...
    def form_valid(self, form):
        # Add logged-in user as person of metakinhsh
        form.instance.person = self.request.user
        # assign transfer handler, depending on the km
        if form.instance.km <= 50:
             form.instance.handler = 'Επόπτης'
        else:
             form.instance.handler = 'Οικονομικό'
        # Call super-class form validation behaviour
        response = super().form_valid(form)
        messages.success(self.request, 'Επιτυχής καταχώρηση!')
        return response


class MetakinhshUpdateView(LoginRequiredMixin, UpdateView, SuccessMessageMixin):
    login_url = '/metakinhseis/login'
    # do not redirect after login
    def get_redirect_field_name(self, **kwargs):
          return None
    model = Metakinhsh
    form_class = MetakinhshForm
    template_name = 'metak/metakinhsh_update_form.html'
    success_url = reverse_lazy('metakinhsh_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Επιτυχής αποθήκευση!')
        return response


def index(request):
    if request.user.is_authenticated:
        return redirect('metakinhsh_list')
    else:
        return redirect('login')


def logout_user(request):
    logout(request)
    return redirect('login')

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="metak/login.html", context={"login_form":form})