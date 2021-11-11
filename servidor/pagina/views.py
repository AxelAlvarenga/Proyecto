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

def listar_producto(request):
    return 

def buscar(request):
  
         listatabla=producto.objects.all()
         return render(request, "table-datatable.html",
     
         {"nombre_completo":request.session.get("nombre_completo_usuario"),"listatabla":listatabla})
  



