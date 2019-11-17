from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns = [
    path( 'albumnes/', AlbumView.as_view({'get': 'get', 'post':'post'}) ),
    path( 'albumnes/top', AlbumView.as_view({'get': 'topAlbumnes'}) ),
    path( 'albumnes/<int:pk>', AlbumView.as_view({'get': 'get','put':'put','delete':'delete'}) ),
    path( 'albumnes/<int:pk>/canciones', AlbumView.as_view({'get': 'canciones'}) ),
    
    path('artistas/<int:pk>', ArtistaView.as_view()),
    path('artistas/', ArtistaView.as_view()),
    
    path('canciones/<int:pk>', CancionView.as_view()),
    path('canciones/', CancionView.as_view()),
    
    path('lista-reproduccion/<int:pk>', ListaReproduccionView.as_view()),
    path('lista-reproduccion/', ListaReproduccionView.as_view()),
    
    path('generos/', GeneroView.as_view()),
    
    path('utilidades/generos', UtilidadesView.as_view({'get': 'generos'})),
    path('utilidades/clasificaciones', UtilidadesView.as_view({'get': 'clasificaciones'})),
    path('utilidades/ciudades', UtilidadesView.as_view({'get': 'ciudades'})),
    path('utilidades/lenguajes', UtilidadesView.as_view({'get': 'lenguajes'})),
    
    path('usuarios/', UsuarioView.as_view()),
    path('usuarios/<int:pk>', UsuarioView.as_view()),
    path('usuario/registration', UsuarioRegistrationView.as_view({'post': 'registration'})),
    path('usuario/logout', UsuarioLogoutView.as_view({'get': 'logout'})),

]
