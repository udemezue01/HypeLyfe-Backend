from django.db import models
from django.conf import settings



class Profile(models.Model):

	user 			= 	models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

	avatar 			= 	models.FileField(blank = True)
	cover_photo 	= 	models.FileField(blank = True)

	username 		= 	models.CharField(max_length = 3000, unique = True)
	bio 			= 	models.CharField(max_length = 4000, blank = True, null = True)
	location		= 	models.CharField(max_length = 4000, blank = True, null = True)

	website 		=   models.CharField(max_length = 4000, blank = True, null = True)
	facebook 		=   models.CharField(max_length = 4000, blank = True, null = True)
	instagram 		=   models.CharField(max_length = 4000, blank = True, null = True)
	twitter 		=   models.CharField(max_length = 4000, blank = True, null = True)

	def __str__(self):

		return return f'{self.user.full_name} - Profile'

		