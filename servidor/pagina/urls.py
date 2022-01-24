from django.urls import path
from pagina import views
urlpatterns = [path('', views.login ,name='login'), 
path('index.html', views.inicio ,name='inicio'),
path('login.html', views.salir ,name='salir'),
path('buscar', views.buscar ,name='buscar'),
path('verproducto/<int:producto_actual>', views.verproducto, name='verproducto'),
path('editproducto/<int:producto_actual>',views.editproducto, name='editproducto'),
path('editclientes/<int:cliente_actual>', views.editclientes ,name='editclientes'),
path('reportes_cliente/<int:cliente_actual>', views.reportescliente ,name='reportes_cliente'),
# path('editusuarios/<int:usuario_actual>', views.editusuarios ,name='editusuarios'),
path('vender', views.vender ,name='vender'),
path('borrarproducto/<int:producto_actual>', views.borrarproducto , name='borrarproducto'),
path('borrarcliente/<int:cliente_actual>', views.borrarcliente , name='borrarcliente'),
path('borrarproveedor/<int:proveedor_actual>', views.borrarproveedor , name='borrarproveedor'),
path('cargar_proveedor/<int:proveedor_actual>', views.editproveedor , name='cargar_proveedor')

]
