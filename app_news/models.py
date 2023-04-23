from django.db import models

from basemodel.models import BaseModel

class App_New(BaseModel):
    title = models.CharField('Titular', max_length=200,blank=False, null=False)
    subtitle = models.TextField('Resumen', max_length=200, blank=False, null=False)
    body = models.TextField('Cuerpo', blank=False, null=False)
    image_news = models.ImageField('Imagen Noticia', max_length=400,blank=False, null=False)
    url_news = models.URLField('URL Noticia',max_length=400, blank=False, null=False)
    source = models.CharField('Fuente', max_length=100, blank=False, null=False)
    author = models.CharField('Autor', max_length=100, default='Agencias')
    date_news = models.DateField('Fecha de Publicación', blank=False, null=False)
    is_active = models.BooleanField('Activa', default=True)

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'

    def __str__(self):
        return (self.title + ' ' + self.source)
