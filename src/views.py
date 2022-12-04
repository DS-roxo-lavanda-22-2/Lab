from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def list_users(request):
  return render(request, 'list_users/index.html')
