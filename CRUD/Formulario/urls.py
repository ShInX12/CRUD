from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

app_name = 'persona'
urlpatterns = [
    # Vistas def
    # path('', views.lista_personas, name='lista_personas'),
    # path('editar/<int:cc>', views.editar_persona, name='editar_persona'),
    # path('eliminar/<int:cc>', views.eliminar_persona, name='eliminar_persona'),
    # path('nuevo', views.crear_persona, name='crear_persona'),

    # Vistas class
    # path('', LoginView.as_view(template_name='CRUD/Formulario/index.html'), name="login"),
    path('', views.ListaPersonas.as_view(), name='lista_personas'),
    path('personas/nuevo', views.CrearPersona.as_view(), name='crear_persona'),
    path('personas/editar/<pk>', views.EditarPersona.as_view(), name='editar_persona'),
    path('personas/eliminar/<pk>', views.EliminarPersona.as_view(), name='eliminar_persona'),

    path('mascotas', views.ListaMascotas.as_view(), name='lista_mascotas'),
    path('mascotas/nuevo', views.CrearMascota.as_view(), name='crear_mascota'),
    path('mascotas/editar/<pk>', views.EditarMascota.as_view(), name='editar_mascota'),
    path('mascotas/eliminar/<pk>', views.EliminarMascota.as_view(), name='eliminar_mascota'),

]
