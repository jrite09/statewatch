from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse

# GET and POST constants because I'm lazy
CONSTPOST = "POST"
CONSTGET = "GET"

# Create your views here.
def create_acc(request):
    if request.method == CONSTPOST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("tracker:index")
    else:
        form = UserCreationForm()
    
    return render(request, "authentication/createacc.html", {'form': form})


def login_view(request):
    if request.method == CONSTPOST:
        form = AuthenticationForm(data=request.POST)
        # left off here, form is not passing is_valid check
        if form.is_valid():
            # print('form is valid')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                # print('authenticated user')
                login(request, user)
                return redirect("tracker:index")
            else:
                # print("user not authenticated")
                form.add_error(None, ValidationError(_('Unable to authenticate'), code="invalid authentication"))
                return render(request, "authentication/login.html", {'form': form})
        else:
            print("not validated")
            return render(request, "authentication/login.html", {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, "authentication/login.html", {'form': form})



def logout_view(request):
    logout(request)
    return redirect("tracker:index")