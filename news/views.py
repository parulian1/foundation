from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from news.models import Blog, Category, News, Press

# Create your views here.
def news(request):
	# news = News.objects.filter(hide=False).order_by("-modified")
	news = None
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


def view_press_by_category(request, category_id):
	category = get_object_or_404(Category, id=category_id)
	press_list = Press.objects.filter(category=category, hide=False).order_by('-modified')
	paginator = Paginator(press_list, 4)
	page = request.GET.get('page')
	try:
		news_press = paginator.page(page)
	except PageNotAnInteger:
		news_press = paginator.page(1)
	except EmptyPage:
		news_press = paginator.page(paginator.num_pages)
	return render_to_response('news/view_press_by_category.html', {
		'category': category,
		'news_press': news_press, 
		}, context_instance=RequestContext(request))


def view_press(request, press_id):
	press = get_object_or_404(Press, id=press_id)
	return render_to_response('news/view_press.html', {
		'active': 4,
		'press': press, 
		}, context_instance=RequestContext(request))

