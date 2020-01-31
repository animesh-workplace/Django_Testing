from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.conf import	settings
from django.db import models
import json

# Create your models here.
def upload_update_image(instance, filename):
	return "updates/{user}/{filename}".format(user = instance.user, filename = filename)

class UpdateQuerySet(models.QuerySet):
	def serialize(self):
		qs_list = list(self.values())
		return json.dumps(qs_list, cls = DjangoJSONEncoder, indent = 4)

class UpdateManager(models.Manager):
	def get_queryset(self):
		return UpdateQuerySet(self.model, using=self.db)
		
class Update(models.Model):
	user		= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.PROTECT)
	content		= models.TextField(blank = True, null = True)
	image		= models.ImageField(upload_to = upload_update_image, blank = True, null = True)
	updated 	= models.DateTimeField(auto_now = True)
	timestamp 	= models.DateTimeField(auto_now = True)

	objects = UpdateManager()

	def __str__(self):
		return self.content or ''

	def serialize(self):
		json_data = serialize('json', [self], indent = 4)
		struct = json.loads(json_data)
		data = json.dumps(struct[0]['fields'], indent = 4)
		return data