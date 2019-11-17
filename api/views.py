from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from django.db.models import Avg
from django_countries.data import COUNTRIES
from languages.languages import LANGUAGES

#authentication
from rest_framework.permissions import IsAuthenticated, AllowAny 
from django.contrib.auth import login,logout,authenticate

from .models import *
from .serializers import *
from django.contrib.auth.models import User


""" **************************************************************************************************************** """

class AlbumView( viewsets.ModelViewSet):
    
    def get( self , request, pk=0):
        if pk != 0:
            album = get_object_or_404(Album, pk=pk)
            return Response({ "albumn" : AlbumSerializer(album).data})
        else:
            albumnes = Album.objects.all()
            return Response({ "albumnes" : AlbumSerializer(albumnes, many=True).data})

    def post(self, request):
        album = request.data
        serializer = AlbumSerializer(data=album)

        if serializer.is_valid(raise_exception=True):
            album_saved = serializer.save()
        return Response({"success": "Album '{}' creado con éxito".format(album_saved.descripcion)}, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        saved_album = get_object_or_404(Album, pk=pk)
        data = request.data
        serializer = AlbumSerializer(instance=saved_album, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            album_saved = serializer.save()
        return Response({"success": "Album '{}' actualizado con éxito".format(album_saved.descripcion)}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        album = get_object_or_404(Album, pk=pk)
        album.delete()
        return Response({"message": "Album `{}` fue eliminado con éxito.".format(album.descripcion)},status=status.HTTP_204_NO_CONTENT)

    def topAlbumnes(self, request):
        raking = Cancion.objects.values('album').order_by('ranking').annotate(ranking=Avg('ranking'))[:5]
        list_album = []

        for item in raking:
            list_album.append( item['album'] )

        albumnes = Album.objects.filter(id__in=list_album)
        return Response({ "albumnes" : AlbumSerializer(albumnes, many=True).data})

    def canciones(self, request, pk):
        canciones = Cancion.objects.filter(album=pk)
        return Response({ "canciones" : CancionSerializer(canciones, many=True).data})

""" **************************************************************************************************************** """

class GeneroView( APIView ):
     def get( self , request ):
        generos = Genero.objects.all()
        return Response({ "generos" : GeneroSerializer(generos, many=True).data})

""" **************************************************************************************************************** """

class ArtistaView( APIView ):
    def get( self , request, pk=0):
        if pk != 0:
            artista = get_object_or_404( Artista, pk=pk )
            return Response({ "artista" : ArtistaSerializer(artista).data})
        else:
            if request.query_params.get('nombre'):
                artistas = Artista.objects.filter(nombre__contains = request.query_params.get('nombre'))
            else:
                artistas = Artista.objects.all()

            return Response({ "artistas" : ArtistaSerializer(artistas, many=True).data})

    def post(self, request):
        serializer = ArtistaSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            artista_saved = serializer.save()

        return Response({"success": "Artista '{}' creado con éxito".format(artista_saved.nombre)}, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        saved_artista = get_object_or_404(Artista,pk=pk)

        serializer = ArtistaSerializer(instance=saved_artista, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            artista_saved = serializer.save()
        return Response({"success": "Artista '{}' actualizado con éxito".format(artista_saved.nombre)}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        artista = get_object_or_404(Artista,pk=pk)
        artista.delete()
        return Response({"message": "Artista `{}` fue eliminado con éxito.".format(artista.nombre)},status=status.HTTP_204_NO_CONTENT)

""" **************************************************************************************************************** """

class CancionView( APIView ):
    def get( self , request, pk=0):
        if pk != 0:
            cancion = get_object_or_404(Cancion,pk=pk) 
            return Response({ "cancion" : CancionSerializer(cancion).data})
        else:
            if request.query_params.get('nombre'):
                canciones = Cancion.objects.filter(nombre__contains = request.query_params.get('nombre'))
            elif request.query_params.get('genero'):
                canciones = Cancion.objects.select_related('genero').filter(genero__descripcion__contains = request.query_params.get('genero'))
            elif request.query_params.get('artista'):
                canciones = Cancion.objects.select_related('artista').filter(artista__nombre__contains = request.query_params.get('artista'))
            else:
                canciones = Cancion.objects.all()
                
            return Response({ "canciones" : CancionSerializer(canciones, many=True).data})

    def post(self, request):
        serializer = CancionSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):

            """ Validacion de la existencia del usuario con la cancion """
            validacion = Cancion.objects.filter( nombre=request.data.get('nombre'), artista=request.data.get('artista') ).exists() 

            if validacion:
                return Response({ 'Fail': "La cancion '{}' ya se encuentra registrada".format(request.data.get('nombre')) })

            cancion_saved = serializer.save()

        return Response({"success": "Cancion '{}' creado con éxito".format(cancion_saved.nombre)}, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        saved_cancion = get_object_or_404(Cancion,pk=pk)

        serializer = CancionSerializer(instance=saved_cancion, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            cancion_saved = serializer.save()
        return Response({"success": "Cancion '{}' actualizado con éxito".format(cancion_saved.nombre)}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        cancion = get_object_or_404(Cancion,pk=pk)
        cancion.delete()
        return Response({"message": "Cancion `{}` fue eliminado con éxito.".format(cancion.nombre)},status=status.HTTP_204_NO_CONTENT)

""" **************************************************************************************************************** """

class UsuarioRegistrationView( viewsets.ModelViewSet ):
    permission_classes = (AllowAny,)
    serializer_class = UsuarioSerializer

    def registration(self, request):        
        usuario = request.data
        serializer = UsuarioSerializer(data=usuario)

        if serializer.is_valid(raise_exception=True):
            usuario_saved = serializer.save()
        return Response({"success": "Usuario '{}' creado con éxito".format(usuario_saved.username)}, status=status.HTTP_201_CREATED)

class UsuarioLogoutView( viewsets.ModelViewSet ):
    serializer_class = UsuarioSerializer

    def logout(self, request):
        request.user.auth_token.delete()
        logout(request)
        return Response(status = status.HTTP_200_OK)

class UsuarioView( APIView ):
    permission_classes = (AllowAny,)
    serializer_class = UsuarioSerializer
    
    def get( self , request, pk=0 ):
        if pk != 0:
            usuario = get_object_or_404(User,id=pk)
            return Response({ "usuario" : UsuarioSerializer(usuario).data})
        else:
            usuarios = User.objects.all()
            return Response({ "usuarios" : UsuarioSerializer(usuarios, many=True).data})

""" **************************************************************************************************************** """

class ListaReproduccionView( APIView ):
    def get( self , request, pk=0):
        if pk != 0:
            listaReproduccion = get_object_or_404(ListaReproduccion,pk=pk)
            return Response({ "listaReproduccion" : ListaReproduccionSerializer(listaReproduccion).data})
        else:
            listasReproduccion = ListaReproduccion.objects.all()
            return Response({ "listasReproduccion" : ListaReproduccionSerializer(listasReproduccion, many=True).data})

    def post(self, request):
        serializer = ListaReproduccionSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            artista_saved = serializer.save()

        return Response({"success": "Lista de reproduccion '{}' creado con éxito".format(artista_saved.descripcion)}, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        saved_artista = get_object_or_404(ListaReproduccion,pk=pk)

        serializer = ListaReproduccionSerializer(instance=saved_artista, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            artista_saved = serializer.save()
        return Response({"success": "Lista de reproduccion '{}' actualizado con éxito".format(artista_saved.descripcion)}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        listaReproduccion = get_object_or_404(ListaReproduccion,pk=pk)
        listaReproduccion.delete()
        return Response({"message": "Lista de reproduccion `{}` fue eliminado con éxito.".format(listaReproduccion.descripcion)},status=status.HTTP_204_NO_CONTENT)

""" **************************************************************************************************************** """

class UtilidadesView( viewsets.ModelViewSet):

    def generos(self, request):
        return  Response({'generos': Artista().GENEROS})
    
    def clasificaciones(self, request):
        return  Response({'clasificaciones': Cancion().CLASIFICACION})
    
    def ciudades(self, request):
        return  Response({'ciudades': COUNTRIES.items()})
    
    def lenguajes(self, request):
        return  Response({'lenguajes': LANGUAGES})
         

