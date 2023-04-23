from django.urls import path

from app_news.views import news


urlpatterns = [
    path('news', news,name='news')
]