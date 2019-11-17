from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

""" **************************************************************************************************************** """

class AlbumSerializer (serializers.HyperlinkedModelSerializer): 
    
    class Meta: 
        model = Album
        fields = ('id', 'descripcion')

    def create(self, validated_data):
        return Album.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)
        instance.id = validated_data.get('id', instance.id)

        instance.save()
        return instance

""" **************************************************************************************************************** """

class ArtistaSerializer (serializers.HyperlinkedModelSerializer): 
    
    generos = serializers.PrimaryKeyRelatedField(many=True, queryset=Genero.objects.all())

    class Meta: 
        model = Artista
        fields = ('id','nombre','genero','fecha_nacimiento','pais_nacimiento','nacionalidad','generos')
        
    def create(self, validated_data):
        instance = Artista()
        instance.nombre = validated_data.get('nombre')
        instance.genero = validated_data.get('genero')    
        instance.fecha_nacimiento = validated_data.get('fecha_nacimiento')
        instance.pais_nacimiento = validated_data.get('pais_nacimiento')
        instance.nacionalidad = validated_data.get('nacionalidad')

        instance.save()

        instance.generos.set( validated_data.get('generos') )

        return instance

    def update(self, instance, validated_data):
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.genero = validated_data.get('genero', instance.genero)
        instance.fecha_nacimiento = validated_data.get('fecha_nacimiento', instance.fecha_nacimiento)
        instance.pais_nacimiento = validated_data.get('pais_nacimiento', instance.pais_nacimiento)
        instance.nacionalidad = validated_data.get('nacionalidad', instance.nacionalidad)
        instance.generos.set( validated_data.get('generos') )

        instance.id = validated_data.get('id', instance.id)
        instance.save()


        return instance

""" **************************************************************************************************************** """

class GeneroSerializer (serializers.HyperlinkedModelSerializer): 

    class Meta: 
        model = Genero 
        fields = ('id','codigo', 'descripcion')

""" **************************************************************************************************************** """

class CancionSerializer (serializers.HyperlinkedModelSerializer): 

    genero = serializers.PrimaryKeyRelatedField(queryset=Genero.objects.all())
    album = serializers.PrimaryKeyRelatedField(queryset=Album.objects.all())
    artista = serializers.PrimaryKeyRelatedField(queryset=Artista.objects.all())

    class Meta: 
        model = Cancion
        fields = ('id','nombre','fecha_lanzamiento','sello_discografico','ranking','imagen','idioma','clasificacion','video','album','genero','idioma','artista')

    def create(self, validated_data):
        return Cancion.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.fecha_lanzamiento = validated_data.get('fecha_lanzamiento', instance.fecha_lanzamiento)
        instance.sello_discografico = validated_data.get('sello_discografico', instance.sello_discografico)
        instance.ranking = validated_data.get('ranking', instance.ranking)
        instance.imagen = validated_data.get('imagen', instance.imagen)
        instance.idioma = validated_data.get('idioma', instance.idioma)
        instance.clasificacion = validated_data.get('clasificacion', instance.clasificacion)
        instance.video = validated_data.get('video', instance.video)
        instance.idioma = validated_data.get('idioma', instance.idioma)
        instance.genero = validated_data.get('genero', instance.genero)
        instance.album = validated_data.get('album', instance.album)
        instance.artista = validated_data.get('artista', instance.artista)

        instance.id = validated_data.get('id', instance.id)

        instance.save()
        return instance

""" **************************************************************************************************************** """

class UsuarioSerializer (serializers.ModelSerializer): 
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name')

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username']
        )
        user.set_password( validated_data['password'] )

        user.save()
        
        return user

""" **************************************************************************************************************** """

class ListaReproduccionSerializer (serializers.HyperlinkedModelSerializer): 
    
    canciones = serializers.PrimaryKeyRelatedField(many=True, required=False, queryset=Cancion.objects.all())
    usuario = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())

    class Meta: 
        model = ListaReproduccion
        fields = ('id','descripcion','usuario','canciones')

    def create(self, validated_data):
        instance = ListaReproduccion()
        instance.descripcion = validated_data.get('descripcion')
        instance.usuario = validated_data.get('usuario')

        instance.save()

        instance.canciones.set( validated_data.get('canciones') )

        return instance

    def update(self, instance, validated_data):
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)
        instance.canciones.set( validated_data.get('canciones') )
        instance.usuario = validated_data.get('usuario', instance.usuario)

        instance.id = validated_data.get('id', instance.id)

        instance.save()
        return instance