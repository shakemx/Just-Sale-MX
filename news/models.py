from django.db import models

from basemodel.models import BaseModel

class News(BaseModel):
    Espanol = 'es'
    Ingles = 'en'
    Frances = 'fr'
    Italiano = 'it'
    Japones = 'ja'
    IDIOMA_CHOICES = [
        ('', 'Todos'),
        (Espanol, 'Español'),
        (Ingles, 'Ingles'),
        (Frances, 'Frances'),
        (Italiano, 'Italiano'),
        (Japones, 'Japones'),
    ]
    México = 'mx'
    Estados_Unidos = 'us'
    España = 'es'
    Francia = 'fr'
    Reino_Unido = 'gb'
    Italia = 'it'
    Japón = 'jp'
    PAIS_CHOICES = [
        ('', 'Todos'),
        (México, 'México'),
        (Estados_Unidos, 'Estados Unidos'),
        (España, 'España'),
        (Francia, 'Francia'),
        (Reino_Unido, 'Reino Unido'),
        (Italia, 'Italia'),
        (Japón, 'Japón'),
    ]
    Noticias = 'news'
    Deportes = 'sport'
    Tecnologia = 'tech'
    Mundo = 'world'
    Finanzas = 'finance'
    Politica = 'politics'
    Negocios = 'business'
    Economia = 'economics'
    Entretenimiento = 'entertainment'
    Belleza = 'beauty'
    Travel = 'travel'
    Viajes = 'travel'
    Musica = 'music'
    Comida = 'food'
    Ciencia = 'science'
    Videojuegos = 'gaming'
    Energia = 'energy'
    TOPICOS_CHOICES = [
        ('', 'Todos'),
        (Noticias, 'Noticias'),
        (Deportes, 'Deportes'),
        (Tecnologia, 'Tecnologia'),
        (Mundo, 'Mundo'),
        (Finanzas, 'Finanzas'),
        (Politica, 'Politica'),
        (Negocios, 'Negocios'),
        (Economia, 'Economia'),
        (Entretenimiento, 'Entretenimiento'),
        (Belleza, 'Belleza'),
        (Travel, 'Travel'),
        (Viajes, 'Viajes'),
        (Musica, 'Musica'),
        (Comida, 'Comida'),
        (Ciencia, 'Ciencia'),
        (Videojuegos, 'Videojuegos'),
        (Energia, 'Energia'),
    ]

    url = models.URLField('URL', blank=False, null=False)
    q = models.CharField('Parámetros de Busqueda', max_length=100,blank=False, null=False)
    lang = models.CharField('Idioma de Noticias', choices=IDIOMA_CHOICES, max_length=2)
    country = models.CharField('País de Noticias', choices=PAIS_CHOICES, max_length=2)
    category = models.CharField('Tópicos de Noticias', choices=TOPICOS_CHOICES,max_length=20)
    sources = models.CharField('Fuentes de Noticias', max_length=100, blank=True, null=True)
    pageSize = models.IntegerField('Articulos por Pagina', blank=False, null=False)

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'

    def __str__(self):
        return (self.url + ' ' + self.q + ' ' + self.lang + ' ' + self.country + ' ' + self.category + ' ' + str(self.pageSize))
    



