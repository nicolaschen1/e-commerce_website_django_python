from django.db import models

# Create your models here.
class ModelsTemps(models.Model):
	date_creation = models.DateTimeField(auto_now_add=True)
	date_mise_a_jour = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True 

class Articles(ModelsTemps):
	titre =  models.CharField(max_length=50)
	commentaire =  models.TextField(max_length=255)


	def __str__(self):
		return self.titre
		
class Profile(models.Model):
   name = models.CharField(max_length = 50)
   picture = models.ImageField(upload_to = 'pictures')

   class Meta:
      db_table = "profile"