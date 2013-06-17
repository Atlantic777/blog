# Create your views here.
from django.shortcuts import render_to_response, redirect

def home(request):
	return redirect('/blog/')
