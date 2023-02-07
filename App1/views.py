from django.shortcuts import render
from django.http import HttpResponse
import datetime, random 
from App1.models import *
from App1.forms import *
def inicio(request):
    
    return render(request, "App1/inicio.html")

def tiempo(request):
    
    now = datetime.datetime.now()
    
    return HttpResponse(f"El tiempo actual es: {now}")

def nuevo_cliente(request):
    
    client = Cliente(nombre = "Abel",apellido ="Leder", direccion = "Entre Rios 1191",localidad="Bella Vista",provincia="Buenos Aires",pais="Argentina")
    
    client.save()
    
    return render(request, "App1/nuevo_cliente.html")
    

def nuevo_stockpropio(request):
    
    soyus = StockPropio()
    
    soyus.save()
    
    return render(request, "App1/nuevo_stock_propio.html")
    pass    

 
def cliente_formulario(request):
    
    if request.method == "POST":
        
        formulario1 = Cliente_Formulario(request.POST)
        
        if formulario1.is_valid():
            
            info = formulario1.cleaned_data
            
            cliente = Cliente_Formulario(nombre=info["nombre"],apellido=info["apellido"],email=info["email"],direccion=info["direccion"],localidad=info["localidad"],provincia=info["provincia"],pais=info["pais"])            
            
            cliente.save()
            return render(request,"App1/inicio.html")
    else:
    
        formulario1= Cliente_Formulario()
    
    return render(request,"App1/cliente_formulario.html",{"form1":formulario1})

def reparacion(request):
     
    if request.method == "POST":
        
        formula1 = Reparacion_Formulario(request.POST)
        
        if formula1.is_valid():
            
            info = formula1.cleaned_data
            
            reparacion = Reparacion_Formulario(nombre=info["modelo"],efecto=info["efecto"],fabricante=info["fabricante"],volts=info["volts"],origen=info["origen"],cliente=info["cliente"],presupuesto=info["presupuesto"],envio=info["envio"])            
            reparacion.save()
            return render(request,"App1/inicio.html")
    else:
    
         formula1= Reparacion_Formulario()
    
     
         return render (request,"App1/reparacion_formulario.html",{"form2":formula1})
     
     
def busqueda_stock(request):
    
    return (request,"App1/busqueda_stock.html")

def mostrar_resultados(request):
    
    return HttpResponse(f"En stock estan: ")