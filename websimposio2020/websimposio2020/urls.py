"""websimposio2020 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from django.conf.urls import include, url
from core import views as core_views
from Galeria import views as galeria_views
from registros import views as registros_views
from django.conf import settings

urlpatterns = [
    path('',core_views.home,name="Home"),
    path('informacion/',core_views.informacion,name="Informacion"),
    path('resumenes/',core_views.resumenes,name="Resumenes"),
    path('instructores/',core_views.instructores,name="Instructores"),
    path('conferencias/',core_views.conferencias,name="Conferencias"),
    path('conferencistas/',core_views.conferencistas,name="Conferencistas"),
    path('ponencias/',core_views.ponencias,name="Ponencias"),
    path('semblanzaGPA/',core_views.semblanzaGPA,name="SemblanzaGPA"),
    path('semblanzaCCM/',core_views.semblanzaCCM,name="SemblanzaCCM"),
    path('semblanzaVMHM/',core_views.semblanzaVMHM,name="SemblanzaVMHM"),
    path('semblanzaOPV/',core_views.semblanzaOPV,name="SemblanzaOPV"),
    path('semblanzaNFL/',core_views.semblanzaNFL,name="SemblanzaNFL"),
    path('semblanzaMLL/',core_views.semblanzaMLL,name="SemblanzaMLL"),
    path('semblanzaPBL/',core_views.semblanzaPBL,name="SemblanzaPBL"),
    path('patrocinadores/',core_views.patrocinadores,name="Patrocinadores"),
    path('talleres/',core_views.talleres,name="Talleres"),
    path('contacto/',core_views.contacto,name="Contacto"),
    path('acerca/',core_views.acerca,name="Acerca"),
    path('quienes/',core_views.quienes,name="Quienes"),
    path('precios/',core_views.precios,name="Precios"),
    path('simposio/',core_views.simposio,name="Simposio"),
    path('calendario/',core_views.calendario,name="Calendario"),
    path('galeria/',galeria_views.galeria,name="Galeria"),
    path('inscripcion/',registros_views.inscripcion,name="Inscripcion"),
    path('gracias/',core_views.gracias,name="Gracias"),
    path('memorias/',core_views.memorias,name="Memorias"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)