from django.http import request
from django.shortcuts import render, redirect
from pagina.models import Usuarios
from pagina.models import producto
from pagina.models import cliente
from pagina.models import proveedor
from pagina.models import categoria

def login(request):
    if request.method == "GET":
        if request.session.get("nombre_usuario"):
            return redirect("index.html")
        else: 
            return render(request, 'login.html')
    if request.method == "POST":
        nusuario = request.POST.get("usuario")
        pusuario = request.POST.get("contra")
        usuario_actual=Usuarios.objects.filter(nombre_usuario=nusuario).exists()
        if usuario_actual:
            datos_usuario=Usuarios.objects.filter(nombre_usuario=nusuario).first()
            if getattr(datos_usuario,"password_usuario")==pusuario:
                request.session["nombredelusuario"]=getattr(datos_usuario, "nombre_usuario")
                request.session["nombre_completo_usuario"]=getattr(datos_usuario, "nombre_completo_usuario")
                return redirect("index.html")
            else:
                return render(request, 'login.html', {"mensaje_error":"Contraseña ingresada es incorrecta."})
        else:
            return render(request, 'login.html', {"mensaje_error":"Usuario ingresado no existe."})
def validar(request, pageSuccess):
    if request.session.get("nombredelusuario"):
        return render(request, pageSuccess, {"nombre_completo": request.session.get("nombredelusuario")})
    else:
        return render(request, 'login.html')           
def inicio(request):
   return validar(request,"index.html")
def verproducto(request):
    return validar(request,"table-datatable.html")

def salir(request):
    request.session.flush()
    return redirect("./")




def buscar(request):
    listacategoria = categoria.objects.all()
    listatabla=producto.objects.all()
    return render(request, "table-datatable.html", {"nombre_completo":request.session.get("nombredelusuario"),"listatabla":listatabla, "listacategoria":listacategoria})

def editproducto(request, producto_actual=0):
    listacategoria = categoria.objects.all()
    if request.method=="GET":
        product_actual=producto.objects.filter(codigo_productos=producto_actual).exists()
        if product_actual:
            datos_producto=producto.objects.filter(codigo_productos=producto_actual).first()
            return render(request, 'editproducto.html',
            {"datos_act":datos_producto, "producto_actual":producto_actual, "titulo":"Editar Usuario", "listacategoria":listacategoria})
        else:
            return render(request, "editproducto.html",
            {"nombre_completo":request.session.get("nombre_completo"), "producto_actual":producto_actual, "titulo":"Cargar Usuario", "listacategoria":listacategoria})

    if request.method=="POST":
        if producto_actual==0:
            producto_nuevo=producto(codigo_productos=request.POST.get('codigo_productos'),
            preciocompra_productos=request.POST.get('preciocompra_productos'),
            precioventa_productos=request.POST.get('precioventa_productos'),
            cantidad_productos=request.POST.get('cantidad_productos'),
            categoria_productos=request.POST.get('categoria_productos'),
            nombre_productos=request.POST.get("nombre_productos"))
            
            producto_nuevo.save()
        else:
            producto_actual=producto.objects.get(codigo_productos=producto_actual)
            producto_actual.nombre_productos=request.POST.get("nombre_productos")
            producto_actual.codigo_productos=request.POST.get("codigo_productos")
            producto_actual.preciocompra_productos=request.POST.get("preciocompra_productos")
            producto_actual.cantidad_productos=request.POST.get("cantidad_productos")
            producto_actual.precioventa_productos=request.POST.get("precioventa_productos")
            producto_actual.categoria_productos=request.POST.get("categoria_productos")
            producto_actual.save()

        return redirect("../buscar")

def editclientes(request, cliente_actual=0):
    listaclientes=cliente.objects.all()
    if request.method=="GET":
        clie_actual=cliente.objects.filter(codigo_cliente=cliente_actual).exists()
        if clie_actual:
            datos_cliente=cliente.objects.filter(codigo_cliente=cliente_actual).first()
            return render(request, 'cargar_cliente.html',
            {"datos_act":datos_cliente, "cliente_actual":cliente_actual, "titulo":"Editar Usuario" , "listaclientes":listaclientes})
        else:
            return render(request, "cargar_cliente.html", {"nombre_completo":request.session.get("nombredelusuario"), "cliente_actual":cliente_actual, "titulo":"Cargar Usuario" , "listaclientes":listaclientes})

    if request.method=="POST":
        if cliente_actual==0:
            cliente_nuevo=cliente(codigo_cliente=request.POST.get('codigo_cliente'),
            nombre_cliente=request.POST.get('nombre_cliente'),
            telefono_cliente=request.POST.get('telefonos_cliente'),
            direccion_cliente=request.POST.get("direccion_cliente"))

            cliente_nuevo.save()
        else:
            cliente_actual=cliente.objects.get(codigo_cliente=cliente_actual)
            cliente_actual.nombre_cliente=request.POST.get("nombre_cliente")
            cliente_actual.codigo_cliente=request.POST.get("codigo_cliente")
            cliente_actual.direccion_cliente=request.POST.get("direccion_cliente")
            cliente_actual.telefono_cliente=request.POST.get("telefonos_cliente")

            cliente_actual.save()

           
    return redirect("../editclientes/0")

def reportescliente(request, cliente_actual=0):
    listaclientes=cliente.objects.all()
    if request.method=="GET":
        clie_actual=cliente.objects.filter(codigo_cliente=cliente_actual).exists()
        if clie_actual:
            datos_cliente=cliente.objects.filter(codigo_cliente=cliente_actual).first()
            return render(request, 'cargar_cliente.html',
            {"datos_act":datos_cliente, "cliente_actual":cliente_actual, "titulo":"Editar Usuario" , "listaclientes":listaclientes})
        else:
            return render(request, "cargar_cliente.html", {"nombre_completo":request.session.get("nombredelusuario"), "cliente_actual":cliente_actual, "titulo":"Cargar Usuario" , "listaclientes":listaclientes})

    if request.method=="POST":
        if cliente_actual==0:
            cliente_nuevo=cliente(codigo_cliente=request.POST.get('codigo_cliente'),
            nombre_cliente=request.POST.get('nombre_cliente'),
            telefono_cliente=request.POST.get('telefonos_cliente'),
            direccion_cliente=request.POST.get("direccion_cliente"))

            cliente_nuevo.save()
        else:
            cliente_actual=cliente.objects.get(codigo_cliente=cliente_actual)
            cliente_actual.nombre_cliente=request.POST.get("nombre_cliente")
            cliente_actual.codigo_cliente=request.POST.get("codigo_cliente")
            cliente_actual.direccion_cliente=request.POST.get("direccion_cliente")
            cliente_actual.telefono_cliente=request.POST.get("telefonos_cliente")

            cliente_actual.save()

           
    return redirect("../reportes_cliente")


def modusuarios(request, usuario_actual=0):
    listatabla=Usuarios.objects.all()
    if request.method=="GET":
        usu_actual=Usuarios.objects.filter(cod_usuario = usuario_actual).exists()
        if usu_actual:
            datos_usuario=Usuarios.objects.filter(cod_usuario=usuario_actual).first()
            return render(request, 'verusuario.html',
            {"datos_act":datos_usuario, "usuario_actual":usuario_actual, "titulo":"Editar Usuario", "listatabla":listatabla})
        else:
            return render(request, "verusuario.html", {"nombre_completo":request.session.get("nombredelusuario"), "usuario_actual":usuario_actual, "titulo":"Modificar Usuario" ,"listatabla":listatabla})

    if request.method=="POST":
        if usuario_actual==0:
            usuario_nuevo=Usuarios(cod_usuario=request.POST.get('cod_usuario'),
            nombre_completo=request.POST.get('nombre_completo_usuario'),
            usuario=request.POST.get('nombre_usuario'),
            clave=request.POST.get('password_usuario'))

            usuario_nuevo.save()
        else:
            usuario_actual=Usuarios.objects.get(cod_usuario=usuario_actual)
            usuario_actual.nombre_completo_usuario=request.POST.get("nombre_completo_usuario")
            usuario_actual.nombre_usuario=request.POST.get("nombre_usuario")
            usuario_actual.password_usuario=request.POST.get("password_usuario")
            usuario_actual.save() 

        return redirect ("../modusuarios/0")

def borusuario (request, usuario_actual):
    Usuarios.objects.filter(cod_usuario = usuario_actual).delete()
    return redirect ("../modusuarios/0")
      
def editproveedor(request, proveedor_actual=0):
    listaproveedor=proveedor.objects.all()
    if request.method=="GET":
        prov_actual=proveedor.objects.filter(codigo_proveedor=proveedor_actual).exists()
        if prov_actual:
            datos_proveedor=proveedor.objects.filter(codigo_proveedor=proveedor_actual).first()
            return render(request, 'cargar_proveedor.html',
            {"datos_act":datos_proveedor, "proveedor_actual":proveedor_actual, "titulo":"Editar Usuario","listaproveedor":listaproveedor})
        else:
            return render(request, "cargar_proveedor.html", {"nombre_completo":request.session.get("nombredelusuario"), "proveedor_actual":proveedor_actual, "titulo":"Cargar Usuario","listaproveedor":listaproveedor})

    if request.method=="POST":
        if proveedor_actual==0:
            proveedor_nuevo=proveedor(codigo_proveedor=request.POST.get('codigo_proveedor'),
            nombre_proveedor=request.POST.get('nombre_proveedor'),
            ruc_proveedor=request.POST.get('ruc_proveedor'),
            Telefono_proveedor=request.POST.get('Telefono_proveedor'),
            direccion_proveedor=request.POST.get("direccion_proveedor"))
            
            proveedor_nuevo.save()

        else:
            proveedor_actual=proveedor.objects.get(codigo_proveedor=proveedor_actual)
            proveedor_actual.nombre_proveedor=request.POST.get("nombre_proveedor")
            proveedor_actual.ruc_proveedor=request.POST.get("ruc_proveedor")
            proveedor_actual.Telefono_proveedor=request.POST.get("Telefono_proveedor")
            proveedor_actual.direccion_proveedor=request.POST.get("direccion_proveedor")
            proveedor_actual.save() 

        return redirect("../cargar_proveedor/0")

   

def vender(request):
  
        listatabla=producto.objects.all()
        return render(request, "punto_venta.html",
     
         {"nombre_completo":request.session.get("nombredelusuario"),"listatabla":listatabla})
     
def borrarproducto(request,producto_actual ):

    producto.objects.filter(codigo_productos= producto_actual).delete()

    return redirect("../buscar")

def borrarcliente(request,cliente_actual ):

    cliente.objects.filter(codigo_cliente= cliente_actual).delete()

    return redirect("../editclientes/0")


def borrarproveedor(request,proveedor_actual ):

    proveedor.objects.filter(codigo_proveedor= proveedor_actual).delete()

    return redirect("../cargar_proveedor/0")
    

