from homework.models import Student
from django.db import IntegrityError
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


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))


class RegistrationView(View):
    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        group_id = request.POST['group_id']

        # Ensure password matches confirmation
        password = request.POST['password']
        confirmation = request.POST['confirm-password']
        if password != confirmation:
            return render(request, 'homework/register.html', {
                'error': 'Passwords must match.'
            })

        # Attempt to create new user
        try:
            user = Student.objects.create_user(
                username, email, password,
                first_name=first_name,
                last_name=last_name,
                group_id=group_id
            )
            user.save()
        except IntegrityError:
            return render(request, 'homework/register.html', {
                'error': 'Username already taken.'
            })
        login(request, user)
        return HttpResponseRedirect(reverse('index'))

    def get(self, request):
        return render(request, 'homework/register.html')
