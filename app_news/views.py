from django.shortcuts import  render, redirect
from django.db.models.functions import Substr
from datetime import datetime 

from app_news.models import App_New
from os import environ

import requests

def news(request):
    if request.method == 'GET':
        all_news = {}
        url = "https://v3-api.newscatcherapi.com/api/search"
        search = "AMPI OR Infonavit OR cofinavit OR  gentrificacion OR interiorismo OR \"Asociación Mexicana de Profesionales Inmobiliarios\"  OR \"Green Lease Leader\" OR \"premio pritzker\" OR arquitectura OR urbanismo OR conavi OR inmobiliare.com"
        language = "es"
        country = {"mx,es"}
        sources = {'inmobiliare.com, centrourbano.com, forbes.com, maspormas.com, merca20.com, revistaad.es, losojosdehipatia.com.es, america-retail.com, archdaily.mx, expansion.mx'}
        sort_by = "relevancy"
        since = "1 day ago"
        headers = {
            "x-api-key": environ['API_KEY_NEWSCATCHER'],
            "Content-Type" : 'application/json; charset=utf8'
            }
        querystring = {"q":search,"lang":[language],"countries":[country],"sources":[sources],"sort_by":sort_by, "from":since}
        print(querystring)
        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()
        news = data['articles']
        for new in news:
            news_data = App_New(
                title = new['title'],
                subtitle = new['excerpt'],
                body = new['summary'],
                image_news = new['media'],
                url_news = new['link'],
                source = new['clean_url'],
                author = new['author'],
                date_news = datetime.strptime(new['published_date'], '%Y-%m-%d %H:%M:%S'),
            )
            news_data.save()
            all_news = App_New.objects.all()
        return render(request, 'news.html', {'all_news': all_news})
    return redirect('home')

