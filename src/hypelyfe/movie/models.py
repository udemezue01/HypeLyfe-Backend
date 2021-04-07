from django.db import models

from django.conf import settings



class Genre(models.Model):

	pass




class Cast(models.Model):

	pass

class Review(models.Model):

	pass


	

class Movie(models.Model):

	user 				= 	models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

	pass

