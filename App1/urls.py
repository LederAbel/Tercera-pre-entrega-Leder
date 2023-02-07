from django.urls import path
from App1.views import *

urlpatterns = [
    
    path("",inicio, name="Inicio"),
    path("nvo_cliente/", nuevo_cliente, name="NuevoCliente"),
    path("nvo_stockprop/", nuevo_stockpropio, name="StockPropio"),
    path("cliente_formulario/",cliente_formulario, name="FormularioCliente"),
    path("reparacion_formulario/", reparacion, name="FormularioReparacion"),
    path("buscar_stock/", busqueda_stock, name="Busqueda"),
    path("resultados_stock/", mostrar_resultados ,name="Resultados"),
]