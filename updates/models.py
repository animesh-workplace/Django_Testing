from django.conf import	settings
from django.db import models

# Create your models here.
def upload_update_image(instance, filename):
	return "updates/{user}/{filename}".format(user = inastance.user, filename = filename)

class Update(models.Model):
	user		= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
	content		= models.TextField(blank = True, null = True)
	image		= models.ImageField(upload_to = upload_update_image, blank = True, null = True)
	updated 	= models.DateTimeField(auto_now = True)
	timestamp 	= models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.content or ''