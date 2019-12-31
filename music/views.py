from django.shortcuts import render
from .models import Album
from django.template import loader

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import loader

def index(request):
    all_album = Album.objects.all()
    # # template = loader.get_template('music/index.html')
    # context = {
    #     'all_album' :all_album ,
    # }

    context = {'all_album' :all_album }


    # return HttpResponse(template.render(context, request))
    return  render(request , 'music/index.html', context)

    # html = ''
    #
    # for album in all_album:
    # url = '/music/' + str(album.id) + '/'
    # html += '<a href="' + url + '"> ' + album.album_title + '</a><br>'

    # return HttpResponse(html)


def detail(request, album_id):
    return HttpResponse("<h2> details for Album id : " + str(album_id) + " </h2>")
