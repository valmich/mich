from django.contrib import admin
from .models import Secretaria, Computador, Monitor, Nobreak, SoftwareOs, SoftwareOutro, Impressora
from django.http import HttpResponse
#Gerador de PDF
from django.template.loader import render_to_string
from django.core.files.storage import FileSystemStorage
from weasyprint import HTML
from django_object_actions import DjangoObjectActions



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
class SecretariaAdmin(DjangoObjectActions, admin.ModelAdmin):
    model = Secretaria
    date_hierarchy = 'data_de_cadastro'
    inlines = [ComputadorInline, MonitorInline, ImpressoraInline, NobreakInline, SoftwareOsInline, SoftwareOutroInline]
    list_display = ['secretaria','departamento', 'data_de_cadastro']

    #Gerador de PDF
    def generate_pdf(self, request, obj):
        html_string = render_to_string('informatica/pdf_template.html', {'obj': obj})
        
        html = HTML(string=html_string)
        html.write_pdf(target='/tmp/{}.pdf'.format(obj))

        fs = FileSystemStorage('/tmp')
        with fs.open('{}.pdf'.format(obj)) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(obj)
            return response

        return response
    
    generate_pdf.label = 'Gerar PDF'
    generate_pdf.short_description = 'Clique para gerar o PDF deste cadastro.'

    change_actions = ('generate_pdf',)