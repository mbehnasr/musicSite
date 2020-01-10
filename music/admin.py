from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered

# Register ysalam
from .models import Album ,Song

admin.site.register(Album)
admin.site.register(Song)


# when change my models we migration must do
# but for example def __self__ don't change database and don't need migration
# so when change def without atribiout don't  neccesarry change database and do migration
