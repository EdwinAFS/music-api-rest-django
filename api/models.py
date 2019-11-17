from django.db import models
from django_countries.fields import CountryField
from languages.fields import LanguageField

""" **************************************************************************************************************** """

class Album(models.Model):
    id = models.AutoField(primary_key = True)
    descripcion = models.CharField (max_length = 50) 

    def __str__ (self): 
            return self.descripcion
        
    class Meta:
        ordering = ['descripcion']
        verbose_name = 'Album'
        verbose_name_plural = 'Albumnes'

""" **************************************************************************************************************** """

class Genero(models.Model):
    id = models.AutoField(primary_key = True)
    codigo = models.CharField (max_length = 6, unique=True) 
    descripcion = models.CharField (max_length = 50) 

    def __str__ (self): 
            return self.descripcion
        
    class Meta:
        ordering = ['descripcion']
        verbose_name = 'Genero'
        verbose_name_plural = 'Generos'

""" **************************************************************************************************************** """

class Artista(models.Model): 

    GENEROS = (
        ('M', 'Masculino'),
        ('F', 'Femenino')
    )

    id = models.AutoField(primary_key = True)
    nombre = models.CharField (max_length = 60) 
    genero = models.CharField (max_length = 2, choices=GENEROS)
    fecha_nacimiento = models.DateField(auto_now=False, auto_now_add=False)
    pais_nacimiento = CountryField()
    nacionalidad = CountryField()
    generos = models.ManyToManyField(Genero, related_name="lista_generos", blank=False)

    def __str__ (self): 
        return self.nombre

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Artista'
        verbose_name_plural = 'Artistas'

""" **************************************************************************************************************** """

class Cancion(models.Model):

    CLASIFICACION = (
        ('CLA', 'Clásica'),
        ('MOD', 'Moderna'),
        ('CUL', 'Culta'),
        ('TRA', 'Tradicional'),
        ('ELE', 'Electrónica'),
        ('INS', 'Instrumental')
    )

    id = models.AutoField(primary_key = True)
    nombre = models.CharField (max_length = 60) 
    fecha_lanzamiento = models.DateField(auto_now=True)
    sello_discografico = models.CharField (max_length = 60)
    ranking = models.SmallIntegerField()
    imagen = models.URLField( max_length=200 )
    idioma = models.CharField(max_length=3)
    clasificacion = models.CharField(max_length=3, choices=CLASIFICACION)
    video = models.URLField(max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT)
    idioma = LanguageField()
    artista = models.ForeignKey(Artista, on_delete=models.PROTECT)
 
    def __str__ (self): 
        return self.nombre

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Cancion'
        verbose_name_plural = 'Canciones'
    
""" **************************************************************************************************************** """

class Usuario(models.Model): 

    id = models.AutoField(primary_key = True)
    nombres =  models.CharField (max_length = 50) 
    apellidos =  models.CharField (max_length = 50) 
    username = models.CharField (max_length = 50, unique=True) 
    password = models.CharField (max_length = 100)

    def __str__ (self): 
        return self.username

    class Meta:
        ordering = ['apellidos']
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

""" **************************************************************************************************************** """

class ListaReproduccion(models.Model): 

    id = models.AutoField(primary_key = True)
    descripcion = models.CharField (max_length = 50) 
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    canciones = models.ManyToManyField(Cancion, related_name="lista_canciones", blank=False)

    def __str__ (self): 
        return self.descripcion

    class Meta:
        ordering = ['descripcion']
        verbose_name = 'Lista de Reproduccion'
        verbose_name_plural = 'Listas de Reproducciones'

""" **************************************************************************************************************** """
