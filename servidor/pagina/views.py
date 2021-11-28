from django.shortcuts import render, redirect
from pagina.models import Usuarios
from pagina.models import producto

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

def salir(request):
    request.session.flush()
    return redirect("./")

def verproducto(request):
    return validar(request,"table-datatable.html")


def buscar(request):
  
         listatabla=producto.objects.all()
         return render(request, "table-datatable.html",
     
         {"nombre_completo":request.session.get("nombredelusuario"),"listatabla":listatabla})

def editproducto(request, producto_actual=0):
    if request.method=="GET":
        producto_actual=producto.objects.filter(codigo_productos=producto_actual).exists()
        if producto_actual:
            datos_producto=producto.objects.filter(codigo_productos=producto_actual).first()
            return render(request, 'editproducto.html',
            {"datos_act":datos_producto, "producto_actual":producto_actual, "titulo":"Editar Usuario"})
        else:
            return render(request, "editproducto.html",
            {"nombre_completo":request.session.get("nombre_completo"), "producto_actual":producto_actual, "titulo":"Cargar Usuario"})

    if request.method=="POST":
        if producto_actual==0:
            producto_nuevo=producto(producto=request.POST.get('producto'),
            codigo_productos=request.POST.get('codigo_producto'),
            preciocompra_productos=request.POST.get('preciocompra_producto'),
            precioventa_productos=request.POST.get('precioventa_producto'),
            cantidad_productos=request.POST.get('cantidad_producto'),
            categoria_productos=request.POST.get('categoria_producto'),
            nombre_productos=request.POST.get("nombre_producto"))
            
            producto_nuevo.save()
        else:
            producto_actual=producto.objects.get(codigo_productos=producto_actual)
            producto_actual.nombre_productos=request.POST.get("nombre_producto")
            producto_actual.codigo_productos=request.POST.get("codigo_producto")
            producto_actual.preciocompra_productos=request.POST.get("preciocompra_producto")
            producto_actual.cantidad_productos=request.POST.get("cantidad_producto")
            producto_actual.precioventa_productos=request.POST.get("precioventa_producto")
            producto_actual.categoria_productos=request.POST.get("categoria_producto")
            producto_actual.save()

        return redirect("../editproducto")
    
    return render(request, "editproducto.html",
            {"nombre_completo":request.session.get("nombre_completo"), "producto_actual":producto_actual, "titulo":"Cargar Usuario"})
    
    
# def editproducto(request):
    
#     return validar(request, 'editproducto.html')

def cargar_cliente(request):
  
    return render(request, "cargar_cliente.html",
    {"nombre_completo":request.session.get("nombredelusuario")})
    
  

