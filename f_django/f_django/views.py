"""from django.http import HttpResponse 
def home(request):
	return HttpResponse('<h2>Hello World!</h2>')"""
from django.shortcuts import render 

def home(request):
	return render(request,'home.html')
def contacts(request):
	return render(request,'pages/contacts.html')
def descriptions(request):
	return render(request,'pages/descriptions.html')
def handler404(request):
	return render(request, 'errors/404.html', {}, status=404)
def handler500(request):
	return render(request, 'errors/500.html', {}, status=500)


	
