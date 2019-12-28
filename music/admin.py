from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered

# Register ysalam
from .models import Album

admin.site.register(Album)


