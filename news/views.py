from news.models import News

from os import environ
import requests



def news(url, search, lang, country, sources, pagesize):
    url = 'url'
    search = 'q'
    lang = 'lang'
    country = 'country'
    sources = 'sources'
    pagesize = 'pagesize'
    headers = {
        'x-api-key' : environ['API_KEY_NEWSCATCHER']
    }
    querystring = {'q' : [search], 'lang' : [lang], 'country' : [country], 'sources' : [sources], 'pagesize' : [pagesize]}
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()
    
    

