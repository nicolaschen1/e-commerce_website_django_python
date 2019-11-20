from django.http import Http404
class Article():
	Articles = [{'id':1,'titre':'Premier Article','Commentaire':'Télephone Iphone'},
		        {'id':2,'titre':'deuxième Article','Commentaire':'Téléphone Samsung '},
		        {'id':3,'titre':'troisième Article','Commentaire':'Téléphone HTC'},
		        {'id':4,'titre':'quatrième Article','Commentaire':'Téléviseur SONY'},
		        {'id':5,'titre':'cinquième Article','Commentaire':'Ecouteur Radio'},
	]



	@classmethod 
	def all(cls):
	    	return cls.Articles

	@classmethod
	def find(cls, id):
		try:
	    	 return cls.Articles[int(id) - 1]
		except:
			raise Http404('Page not found erreur 404')

