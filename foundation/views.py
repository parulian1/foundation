import os
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from gallery.models import Gallery, Video
from program.models import ProgramCategory, Program


def home(request):
	MAIN_IMAGE_LIMIT = getattr(settings, 'INDEX_IMAGE_SLIDER_LIMIT', 4)
	PROGRAM_LIMIT = getattr(settings, 'INDEX_PROGRAMS_LIMIT', 3)

	main_images = Gallery.objects.filter(show_to_index=True, 
					show=True).order_by('-created')
	programs = Program.objects.filter(hide=False)
	videos = Video.objects.filter(show=True)
	program_list = []
	for p_category in ProgramCategory.objects.all().order_by('-created')[:PROGRAM_LIMIT]:
		program_list.append({'category': p_category, 'programs': p_category.program_set.order_by('-created')})
	
	return render_to_response('index.html',{ 
		'images': main_images[:MAIN_IMAGE_LIMIT],
		'program_list': program_list,
		'videos': videos[:2],
		},context_instance=RequestContext(request))

def pillar_education(request):
	return render_to_response('pillars/education.html',{
		}, context_instance=RequestContext(request))

def pillar_health(request):
	return render_to_response('pillars/health.html',{
		}, context_instance=RequestContext(request))

def impact(request):
	return render_to_response('impact.html',{
		}, context_instance=RequestContext(request))

def story(request):
	return render_to_response('story.html', 
    	{'active': 1}, 
    	context_instance=RequestContext(request))

def support_us(request):
	return render_to_response('support_us.html', 
    	{'active': 5}, 
    	context_instance=RequestContext(request))