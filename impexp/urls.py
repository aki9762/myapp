from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

#load the view and the api's here

from impexp.views import(
	simple_upload
	)

urlpatterns=[
	url(r'^simple_upload/$',simple_upload,name="simple_upload"),
]
