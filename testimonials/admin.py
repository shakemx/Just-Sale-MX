from django.contrib import admin

from testimonials.models import Testimonial

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('headline', 'lead', 'body', 'url_video', 'is_active')
   

admin.site.register(Testimonial, TestimonialAdmin)


