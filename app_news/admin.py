from django.contrib import admin

from app_news.models import App_New

class App_NewAdmin(admin.ModelAdmin):
    list_display = ('source', 'title', 'subtitle', 'date_news', 'author','is_active')
    list_filter = ('is_active', 'date_news', 'source')
    search_fields = ('title', 'source')
    ordering = ('-date_news',)    

admin.site.register(App_New, App_NewAdmin)
