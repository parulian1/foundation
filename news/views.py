from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from news.models import News, Career

# Create your views here.
def news(request):
	news = News.objects.filter(hide=False)
	return render_to_response('news/index.html', {
		'news': news,
		}, context_instance=RequestContext(request))

def blogs(request):
	blogs = News.objects.filter(news_category__name__icontains='blog', hide=False)
	return render_to_response('news/blog_index.html', {
		'active': 3,
		'blogs': blogs,
		}, context_instance=RequestContext(request))


def press(request):
	news_press = News.objects.filter(news_category__name__icontains='press', hide=False)
	return render_to_response('news/press.html', {
		'active': 4,
		'news_press': news_press, 
		}, context_instance=RequestContext(request))


def career(request):
	career_list = Career.objects.filter(show=True)
	return render_to_response('news/career_list.html', {
		'career_list': career_list, 
		}, context_instance=RequestContext(request))