from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.
#def index(request):
#	return render(request,'myapp/index.html')
import datetime

#from .dictionnaires import Article
from  .models import Articles
from django.http import Http404
from .forms import LoginForm

from django.views.generic import TemplateView


from .forms import ProfileForm
from .models import Profile 







def index(request):
   today = datetime.datetime.now().date()
   filtre = 'JOEL EST UNE LIMACE LIMACE'
   jourSem = ['Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi','Dimanche']
   return render(request, 'myapp/index.html', {'today' : today, 'filtre': filtre, 'jourSem': jourSem})

def list(request):
	Articles_var = Articles.objects.all()
	return render(request, 'myapp/list.html', {'Articles': Articles_var})

def details(request, id):
	article = get_object_or_404(Articles, pk=id)
#	try:
#		article = Articles.objects.get(pk=id)
#	except Articles.DoesNotExist:
#		raise Http404(' Page not Found erreur 404')
	return render(request, 'myapp/details.html', {'Article' : article})

class StaticView(TemplateView):
	template_name = "myapp/static.html"

def login(request):
   username = " FORMATEUR "
   if request.method == "POST":
      MyLoginForm = LoginForm(request.POST)
      if MyLoginForm.is_valid():
         username = MyLoginForm.cleaned_data['username']
         request.session['username'] = username
   else:
      MyLoginForm = LoginForm()	
   return render(request, 'myapp/loggedin.html', {"username" : username})

def SaveProfile(request):
   saved = False
   
   if request.method == "POST":
      MyProfileForm = ProfileForm(request.POST, request.FILES)
      
      if MyProfileForm.is_valid():
         profile = Profile()
         profile.name = MyProfileForm.cleaned_data["name"]
         profile.picture = MyProfileForm.cleaned_data["picture"]
         profile.save()
         saved = True
   else:
      MyProfileForm = ProfileForm()
      
   return render(request, 'myapp/saved.html', locals())

def formView(request):
   if request.session.has_key('username'):
      username = request.session['username']
      return render( request, 'myapp/loggedin.html', {"username" : username})
   else: 
      return render(request, 'myapp/login.html', {})



def logout(request):
   try:
      del request.session['username']
   except:
      pass
      return HttpResponse("<strong>You are logged out.</strong>")













