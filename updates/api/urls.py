from django.urls import re_path
from updates.api.views import *

urlpatterns = [
    re_path(r'^$', UpdateModelListAPIView.as_view()),
    re_path(r'^(?P<id>\d+)/$', UpdateModelDetailAPIView.as_view()),
]
