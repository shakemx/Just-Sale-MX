from django.urls import path

from home.views import home, about, feed, testimonials, terms, privacy


urlpatterns = [
    path('', home, name='home'),
    path('nosotros', about, name='about'),
    path('terminos_condiciones', terms, name='terms'),
    path('aviso_privacidad', privacy, name='privacy'),
    path('mundo_just', feed, name='feed'), 
    path('historias_exito', testimonials, name='testimonials'),     
]
