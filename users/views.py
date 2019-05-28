from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import auth

from .models import UserProfile

# Create your views here.
def index(request):
	return render(request, 'index.html')


class LoginView(View):
	def get(self, request):
		return render(request, "login.html")

	def post(self, request):
		user_name = request.POST.get("username")
		pass_word = request.POST.get("password")
		user = UserProfile.objects.get(username=user_name)
		user = auth.authenticate(username=user_name, password=check_password(pass_word, user.password))
		if user is not None:
			login(request, user)
			print("user{} login!", user.get_username())
			return render(request, "index.html")
		else:
			return render(request, "index.html")


class RegisterView(View):
	def get(self, request):
		return render(request, 'register.html')

	def post(self, request):
		user_name = request.POST.get("username")
		pass_word = request.POST.get("password")
		user = UserProfile.objects.create(username=user_name, password=make_password(pass_word))
		print(user is None)
		login(request, user)
		return render(request, 'index.html')