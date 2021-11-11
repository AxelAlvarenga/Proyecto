from django.urls import path
from pagina import views
urlpatterns = [path('', views.login ,name='login'), 
path('index.html', views.inicio ,name='inicio'),
path('login.html', views.salir ,name='salir'),
path('table-datatable.html', views.buscar ,name='buscar'),
path('verproducto/<int:codproducto>', views.verproducto, name='verproducto'),



]
