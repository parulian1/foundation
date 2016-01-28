from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from news.models import News, Blog, Press
from program.models import Program

# Create your views here.
def news(request):
	news = News.objects.filter(hide=False).order_by("-modified")
	if not news:
		news = []
		for press in Press.objects.filter(hide=False):
			news.append(press)
	return render_to_response('news/index.html', {
		'news': news,
		}, context_instance=RequestContext(request))

def blogs(request):
	blogs = Blog.objects.filter(hide=False).order_by('-modified')
	return render_to_response('news/blog_index.html', {
		'active': 3,
		'blogs': blogs,
		}, context_instance=RequestContext(request))


def press(request):
	press_list = Press.objects.filter(hide=False).order_by('-modified')
	paginator = Paginator(press_list, 4)
	page = request.GET.get('page')
	try:
		news_press = paginator.page(page)
	except PageNotAnInteger:
		news_press = paginator.page(1)
	except EmptyPage:
		news_press = paginator.page(paginator.num_pages)
	return render_to_response('news/press.html', {
		'active': 4,
		'news_press': news_press, 
		}, context_instance=RequestContext(request))


# def slug_list(request):
# 	news = News.objects.filter(hide=False)
# 	programs = Program.objects.filter(hide=False)

# 	slug_list = []
# 	for info in news:
# 		slugs = info.slug.split(',')
# 		for slug in slugs:
# 			if slug not in slug_list:
# 				slug_list.append(slug)
# 	for program in programs:
# 		slugs = program.slug.split(',')
# 		for slug in slugs:
# 			if slug not in slug_list:
# 				slug_list.append(slug)

# 	