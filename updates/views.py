from django.core.serializers import serialize
from django.views.generic import View
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import *
from testing_api.mixins import *

# Create your views here.
def json_example_view(request):
	data = {
		"count"		: 1000,
		"content"	: "Some new content"
	}
	return JsonResponse(data)

class JsonCBV(View):
	def get(self, request, *args, **kwargs):
		data = {
			"count"		: 1000,
			"content"	: "Some new content"
		}
		return JsonResponse(data)	

class JsonCBV2(JsonResponseMixin, View):
	def get(self, request, *args, **kwargs):
		data = {
			"count"		: 1000,
			"content"	: "Some new content"
		}		
		return self.render_to_json_response(data)

class SerializedDetailView(View):
	def get(self, request, *args, **kwargs):
		obj = Update.objects.get(id = 1).serialize()	
		return HttpResponse(obj, content_type = 'application/json')

class SerializedListView(View):
	def get(self, request, *args, **kwargs):
		qs = Update.objects.all().serialize()
		return HttpResponse(qs, content_type = 'application/json')