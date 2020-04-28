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
from django.conf import settings

urlpatterns = [
    path('',core_views.home,name="Home"),
    path('informacion/',core_views.informacion,name="Informacion"),
    path('inscripcion/',core_views.inscripcion,name="Inscripcion"),
    path('resumenes/',core_views.resumenes,name="Resumenes"),
    path('talleres/',core_views.talleres,name="Talleres"),
    path('panel/',core_views.panel,name="Panel"),
    path('semblanzaGPA/',core_views.semblanzaGPA,name="SemblanzaGPA"),
    path('semblanzaCCM/',core_views.semblanzaCCM,name="SemblanzaCCM"),
    path('semblanzaVMHM/',core_views.semblanzaVMHM,name="SemblanzaVMHM"),
    path('semblanzaOPV/',core_views.semblanzaOPV,name="SemblanzaOPV"),
    path('semblanzaNFL/',core_views.semblanzaNFL,name="SemblanzaNFL"),
    path('charge/',core_views.charge,name="charge"),
    path('success/<str:args>',core_views.success,name="success"),
    path('failure/<str:args>',core_views.failure,name="failure"),
    path('calendario/',core_views.calendario,name="calendario"),
    path('galeria/',galeria_views.galeria,name="Galeria"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)