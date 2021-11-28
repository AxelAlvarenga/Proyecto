from django.urls import path
from pagina import views
urlpatterns = [path('', views.login ,name='login'), 
path('index.html', views.inicio ,name='inicio'),
path('login.html', views.salir ,name='salir'),
path('buscar', views.buscar ,name='buscar'),
path('verproducto/<int:codproducto>', views.verproducto, name='verproducto'),
path('editproducto',views.editproducto, name='editproducto'),
path('cargar_cliente', views.cargar_cliente ,name='cargar_cliente')



]
