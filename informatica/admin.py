from django.contrib import admin
from .models import Secretaria, Computadores



class ComputadoresInline(admin.StackedInline, ):
    model = Computadores
    extra = 0     
                
@admin.register(Secretaria)    
class SecretariaAdmin(admin.ModelAdmin):
    model = Secretaria
    date_hierarchy = 'data_de_cadastro'
    inlines = [ComputadoresInline]
