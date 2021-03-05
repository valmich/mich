from django.contrib import admin
from .models import Secretaria, Computador, Monitor, Nobreak, SoftwareOs, SoftwareOutro, Impressora



class ComputadorInline(admin.StackedInline):
    model = Computador
    extra = 0     

class MonitorInline(admin.StackedInline):
    model = Monitor
    extra = 0 

class ImpressoraInline(admin.StackedInline):
    model = Impressora
    extra = 0  

class NobreakInline(admin.StackedInline):
    model = Nobreak
    extra = 0  

class SoftwareOsInline(admin.StackedInline):
    model = SoftwareOs
    extra = 0 

class SoftwareOutroInline(admin.StackedInline):
    model = SoftwareOutro
    extra = 0  

@admin.register(Secretaria)    
class SecretariaAdmin(admin.ModelAdmin):
    model = Secretaria
    date_hierarchy = 'data_de_cadastro'
    inlines = [ComputadorInline, MonitorInline, ImpressoraInline, NobreakInline, SoftwareOsInline, SoftwareOutroInline]
