from django.contrib import admin
from .models import (Album)
from .models import (Genero)
from .models import (Artista)
from .models import (Cancion)
from .models import (Usuario)
from .models import (ListaReproduccion)

admin.site.register(Album)
admin.site.register(Genero)
admin.site.register(Artista)
admin.site.register(Cancion)
admin.site.register(Usuario)
admin.site.register(ListaReproduccion)