from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View

# Create your views here.


def index(request):
    return render(request, 'homework/index.html')


class LoginView(View):
    def post(self, request):
        # Attempt to sign user in
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        # check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, "homework/login.html", {
                "error": 'Invalid username and/or password.'
            })

    def get(self, request):
        return render(request, 'homework/login.html')


class RegistrationView(View):
    def get(self, request):
        return render(request, 'homework/register.html')
