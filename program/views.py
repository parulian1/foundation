from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render_to_response, render, get_object_or_404
from django.template import RequestContext
from program.models import ProgramCategory, Program
from program.forms import ModifiedPaypalForm
from paypal.standard.forms import PayPalPaymentsForm
# Create your views here.

def programs(request):
    program_list = Program.objects.filter(hide=False).order_by('program_category', '-modified')
    paginator = Paginator(program_list, 4)
    page = request.GET.get('page')
    try:
        programs = paginator.page(page)
    except PageNotAnInteger:
        programs = paginator.page(1)
    except EmptyPage:
        programs = paginator.page(paginator.num_pages)

    return render_to_response('programs/index.html', {
        'active': 2,
    	'programs': programs,
    	}, context_instance=RequestContext(request))

def view_category(request, category_id):
    category = get_object_or_404(ProgramCategory, id=category_id)
    related_program = Program.objects.filter(program_category=category, hide=False)
    paginator = Paginator(related_program, 4)
    page = request.GET.get('page')
    try:
        programs = paginator.page(page)
    except PageNotAnInteger:
        programs = paginator.page(1)
    except EmptyPage:
        programs = paginator.page(paginator.num_pages)
    return render_to_response('programs/category.html', {
        'category': category,
        'programs': programs,
        }, context_instance=RequestContext(request))


def view_program(request, program_id):
    program = get_object_or_404(Program, id=program_id)
    return render_to_response('programs/view.html', {
        'program': program,
    }, context_instance=RequestContext(request))


def view_that_asks_for_money(request):
    programs = Program.objects.filter(hide=False)
    # What you want the button to do.
    paypal_dict = {
        "button_type": 'donate',
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": "2.00",
        "item_name": "Donasi untuk yayasan berani bhakti bangsa",
        "invoice": "unique-invoice-id",
        "notify_url": "https://www.example.com" + reverse('paypal-ipn'),
        "return_url": reverse('program:program_donate'),
        "cancel_return": reverse('program:program_donate'),
        "custom": "Upgrade all users!",  # Custom command to correlate to some function later (optional)
    }

    # Create the instance.
    form = ModifiedPaypalForm(initial=paypal_dict)
    # if form.method 
    context = {"form": form, "programs": programs,}
    return render(request, "programs/donate.html", context)


def program_help(request):
    # programs_help = Program.objects.filter(hide=False, program_category__name__icontains='help')
    programs_help = Program.objects.filter(hide=False)
    return render_to_response('programs/help.html', {
        'programs_help': programs_help,
        }, context_instance=RequestContext(request))

def program_hold(request):
    # programs_hold = Program.objects.filter(hide=False, program_category__name__icontains='hold')
    programs_hold = Program.objects.filter(hide=False)
    return render_to_response('programs/hold.html', {
        'programs_hold': programs_hold,
        }, context_instance=RequestContext(request))

def program_hope(request):
    # programs_hope = Program.objects.filter(hide=False, program_category__name__icontains='hope')
    programs_hope = Program.objects.filter(hide=False)
    return render_to_response('programs/hope.html', {
        'programs_hope': programs_hope,
        }, context_instance=RequestContext(request))

def impact(request):
    return render_to_response('programs/impact.html', {
        }, context_instance=RequestContext(request))