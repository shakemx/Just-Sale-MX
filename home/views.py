from django.shortcuts import render, redirect

from app_news.models import App_New



def home(request):
    if request.method == 'GET':
        news = App_New.objects.all()
        context = {'news': news}
        return render(request, 'home/home.html', context=context) 
    return redirect('home')