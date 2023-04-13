from django.contrib import admin

from promotions.models import Promotion

class PromotionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image_portada', 'url_video', 'date_deactivate', 'is_active')
    list_filter = ('is_active', 'date_deactivate')
    search_fields = ('title', 'description')
    date_hierarchy = 'date_deactivate'
    ordering = ('-date_deactivate',)    

admin.site.register(Promotion, PromotionAdmin)


