from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login

# Create your views here.

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"Έχετε πραγματοποιήσει είσοδο ως {username}.")
				return redirect("home")
			else:
				messages.error(request,"Εσφαλμένος κωδικός ή όνομα χρήστη")
		else:
			messages.error(request,"Εσφαλμένος κωδικός ή όνομα χρήστη")
	form = AuthenticationForm()
	return render(request=request, template_name="registration/login.html", context={"login_form":form})


def logout_user(request):
    logout(request)
    return redirect('login')