from django.conf.urls import include,url
from django.contrib import admin

from .views import(
		post_list,
		post_create,
	)

urlpatterns = [
	url(r'^$',post_list),
	url(r'^create/$',post_create,name="create"),
]