from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse

from app_news.models import App_New
from testimonials.models import Testimonial



def home(request):
    if request.method == 'GET':
        news = App_New.objects.filter(is_active=True).order_by('-date_news')
        testimonials = Testimonial.objects.filter(is_active=True)
        context = {'news': news, 'testimonials': testimonials}
        return render(request, 'home/home.html', context=context) 
    return redirect('home')

def about(request):
    if request.method == 'GET':
        return render(request, 'home/about.html') 
    return redirect('home')

def feed(request):
    if request.method == 'GET':
        news = App_New.objects.filter(is_active=True).order_by('-date_news')
        page_range = 12
        page = request.GET.get('page',1)
        paginator = Paginator(news, page_range)
        more_range = 15
        more_page = request.GET.get('page')
        more_paginator = Paginator(news, more_range)    
        more_obj = more_paginator.get_page(more_page)    
        try:
            numbers = paginator.page(page)
        except PageNotAnInteger:
            numbers = paginator.page(1)
        except EmptyPage:
            numbers = paginator.page(paginator.num_pages)
        context = {'numbers': numbers, 'more_obj': more_obj}
        return render(request, 'home/feed.html', context=context) 
    return redirect('home')
    

def testimonials(request):
    if request.method == 'GET':
        testimonials = Testimonial.objects.filter(is_active=True)
        context = {'testimonials': testimonials}
        return render(request, 'home/testimonials.html', context=context) 
    return redirect('home')

def terms(request):
    if request.method == 'GET':
        return render(request, 'home/terms.html') 
    return redirect('home')

def privacy(request):
    if request.method == 'GET':
        return render(request, 'home/privacy.html') 
    return redirect('home')