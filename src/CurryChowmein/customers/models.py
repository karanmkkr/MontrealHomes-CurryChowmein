from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
	user = models.ForeignKey(User, unique=True)
	# first_name = models.CharField(max_length=120)
	# last_name = models.CharField(max_length=120)
	city = models.CharField(max_length=120)
	stripe_customer_id = models.CharField(max_length = 100, blank = True, null = True)

	def __unicode__(self):
		return self.user.username