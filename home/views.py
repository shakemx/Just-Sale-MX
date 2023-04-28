from django.shortcuts import render, redirect

from app_news.models import App_New
from testimonials.models import Testimonial



def home(request):
    if request.method == 'GET':
        news = App_New.objects.filter(is_active=True)
        testimonials = Testimonial.objects.filter(is_active=True)
        context = {'news': news, 'testimonials': testimonials}
        return render(request, 'home/home.html', context=context) 
    return redirect('home')