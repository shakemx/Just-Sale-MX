from django.db import models

from basemodel.models import BaseModel

class Testimonials(BaseModel):
    headline = models.CharField('Nombre', max_length=40,blank=False, null=False)
    lead = models.CharField('Frase', max_length=40,blank=False, null=False)
    body = models.TextField('Resumen', max_length=100,blank=False, null=False)
    url_video = models.URLField('Youtube URL', blank=False, null=False)
    is_active = models.BooleanField('Activa', default=True)

    class Meta:
        verbose_name = 'Testimonio'
        verbose_name_plural = 'Testimonios'

    def __str__(self):
        return (self.headline + ' ' + self.lead)
