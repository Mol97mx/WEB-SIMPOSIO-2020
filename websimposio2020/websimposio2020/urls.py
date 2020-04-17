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
from core import views

urlpatterns = [
    path('',views.home,name="Home"),
    path('informacion/',views.informacion,name="Informacion"),
    path('inscripcion/',views.inscripcion,name="Inscripcion"),
    path('resumenes/',views.resumenes,name="Resumenes"),
    path('talleres/',views.talleres,name="Talleres"),
    path('panel/',views.panel,name="Panel"),
    path('semblanzaGPA/',views.semblanzaGPA,name="SemblanzaGPA"),
    path('semblanzaCCM/',views.semblanzaCCM,name="SemblanzaCCM"),
    path('semblanzaVMHM/',views.semblanzaVMHM,name="SemblanzaVMHM"),
    path('semblanzaOPV/',views.semblanzaOPV,name="SemblanzaOPV"),
    path('semblanzaNFL/',views.semblanzaNFL,name="SemblanzaNFL"),
    path('charge/',views.charge,name="charge"),
    path('success/<str:args>',views.success,name="success"),
    path('admin/', admin.site.urls),
]
