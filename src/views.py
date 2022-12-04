from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import User
from .forms import UserForm
# Create your views here.

def list_users(request):
  # user = User(name="moacir",  function = "dev",
  # birthday="1997-12-21" )
  # user.save()

  return render(request, 'list_users/index.html', {"users": User.objects.all()})

def create_user(request):
  if request.method == 'POST':
    form = UserForm(request.POST)
    if form.is_valid():
      form.save()
      form.clean()
  else:
    form = UserForm()
  return render(request, 'create_user/index.html', { "form": form})