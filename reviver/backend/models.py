from django.db import models
from django.contrib.auth.models import User

#class models.User:
	# user = models.OneToOneField(user)
	# picture = models.ImageField(upload_to='profile_images', blank = True)
	# user_praise = models.OneToOneField(Praise)
	# def _unicode_(self):
	# 	return self.user

class Praise(models.Model):
	user = models.ForeignKey(User)
	content = models.TextField()
	#date_created = models.DateTimeField('Date published')

	def __unicode__(self):
		return self.content
	



