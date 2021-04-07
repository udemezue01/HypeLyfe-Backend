# Create your models here.
from django.db import models

from django.conf import settings


class Wallet(models.Model):

	user 			= models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)


	amount			= models.IntegerField(default = 0, blank = True)

	def __str__(self):

		return return f'{self.user.full_name} - Wallet'


STATUS = (

	('P', 'Pending'),

	('A', 'Approved'),

	('D', 'Decline'),

	)




class Payout(models.Model):

	user 			= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

	wallet 			= models.ForeignKey(Wallet, on_delete = models.CASCADE)

	status			= models.CharField(max_length = 3000, choices = STATUS, default = "P", blank = True, null = True)

	amount 			= models.IntegerField(default = 0, blank = True, null = True)

	created_at 		= models.DateTimeField(auto_now = False, auto_now_add = True)

	def __str__(self):

		return return f'{self.user.full_name} - Payout'


