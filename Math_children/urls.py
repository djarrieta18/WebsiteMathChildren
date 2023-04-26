"""Math_children URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from Math_children.views import Index, Insertar_usuario, VistaUsuario,Ingreso,Logout,Download
from Math_children.views import ListadoUsuario,RegistrarUsuario,ActualizarUsuario

urlpatterns = [
    path('', Index,name='index'),
    path('Index/', Index,name='index'),
    path('Download/', Download,name='Download'),
    path('RegistrarUsuario/', RegistrarUsuario.as_view(),name='RegistrarUsuario'),
    path('ListadoUsuario/', ListadoUsuario.as_view(),name='ListadoUsuario'),
    path('ActualizarUsuario/', ActualizarUsuario.as_view(),name='ActualizarUsuario'),
    path('Ingreso/',Ingreso,name='Ingreso'),
    path('Logout/',Logout,name='Logout'),
    # path('logout/',LogoutView.as_view(template_name='index.html'), name='logout'),
    

]
