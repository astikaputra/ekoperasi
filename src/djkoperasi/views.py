from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
	my_title = "Wirasa"
	return render(request, "base.html",{"title": my_title})