from django.shortcuts import render, redirect

from news.views import news



def home(request):
    if request.method == 'GET':
        news = news()
        context = {'news': news}
        return render(request, 'home/home.html', context=context)
    return redirect('home')