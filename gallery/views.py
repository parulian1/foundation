from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from gallery.models import Gallery, Video

# Create your views here.

def gallery(request):
	galleries = Gallery.objects.filter(show=True).order_by('-modified')
	videos = Video.objects.filter(show=True).order_by('-modified')
	return render_to_response('gallery/index.html', {
		'galleries': galleries,
		'videos': videos,
		}, context_instance=RequestContext(request))


def view_video(request, video_id):
	video = Video.objects.get(id=video_id, show=True)
	return render_to_response('gallery/view_video.html', {
		'video': video,
		}, context_instance=RequestContext(request))
