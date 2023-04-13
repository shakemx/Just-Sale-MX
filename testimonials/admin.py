from django.contrib import admin

from testimonials.models import Testimonials

class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('headline', 'lead', 'body', 'url_video', 'is_active')
   

admin.site.register(Testimonials, TestimonialsAdmin)


