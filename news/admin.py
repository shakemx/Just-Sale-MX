from django.contrib import admin

from news.models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = [
        'url',
        'q',
        'lang',
        'country',
        'category',
        'pageSize',
    ]

admin.site.register(News, NewsAdmin)