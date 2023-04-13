from django.db import models

from basemodel.models import BaseModel

class Promotion(BaseModel):
    title = models.CharField('Titulo de la promocion', max_length=100,blank=False, null=False)
    description = models.TextField('Descripcion de la promocion', blank=False, null=False)
    image_portada = models.ImageField('Imagen Modal', blank=False, null=False)
    url_video = models.URLField('Youtube URL', blank=True, null=True)
    date_deactivate = models.DateField('Fecha de Vencimiento', blank=False, null=False)
    is_active = models.BooleanField('Activa', default=True)

    class Meta:
        verbose_name = 'Promocion'
        verbose_name_plural = 'Promociones'

    def __str__(self):
        return (self.title + ' vence el ' + self.date_deactivate.strftime('%d/%m/%Y'))


