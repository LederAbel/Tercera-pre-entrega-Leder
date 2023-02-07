from django import forms

class Cliente_Formulario(forms.Form):
    
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    direccion = forms.CharField()
    localidad = forms.CharField()
    provincia = forms.CharField()
    pais = forms.CharField()
    

class Reparacion_Formulario(forms.Form):
    modelo = forms.CharField()
    efecto = forms.CharField()
    fabricante = forms.CharField()
    volts = forms.CharField()
    origen = forms.CharField()
    cliente = forms.CharField()
    presupuesto = forms.IntegerField()
    envio = forms.CharField()