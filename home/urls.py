from django.urls import path

from home.views import home, about, feed, testimonials


urlpatterns = [
    path('', home, name='home'),
    path('nosotros', about, name='about'),
    path('mundo_just', feed, name='feed'), 
    path('historias_exito', testimonials, name='testimonials'),     
]
