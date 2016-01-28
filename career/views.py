from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from career.models import Career

# Create your views here.
def list(request):
	career_list = Career.objects.filter(show=True).order_by('-modified')
	return render_to_response('career/list.html', {
		'career_list': career_list, 
		}, context_instance=RequestContext(request))
