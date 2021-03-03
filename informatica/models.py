from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import re
from multiselectfield import MultiSelectField


SECRETARIA_CHOICES = (
    ('SECRETARIAS',(
        ("Assis. Social", "Assis. Social"),
        ("Administração", "Administração"),
        ("Cultura", "Cultura"),
        ("Desenvolvimento", "Desenvolvimento"),
        ("Esporte & Lazer", "Esporte & Lazer"),
        ("Educação", "Educação"),
        ("Fazenda", "Fazenda"),
        ("Gabinete", "Gabinete"),
        ("Habitação", "Habitação"),
        ("Mulher", "Mulher"),
        ("Meio ambiente", "Meio ambiente"),
        ("Mineração, energia, ciência e tecnologia", "Mineração, energia, ciência e tecnologia"),
        ("Produção Rural", "Produção Rural"),
        ("Saúde", "Saúde"),
        ("Secretaria de Obras", "Secretaria de Obras"),
        ("Segurança e Defesa do Cidadão", "Segurança e Defesa do Cidadão"),
        ("Turismo", "Turismo"),
        ("Urbanismo","Urbanismo"),
        ("Sec. Especial de Governo", "Sec. Especial de Governo"),
        ("Sec. Juventude", "Sec. Juventude"),
    )),
    
    ('COODENADORIAS',(
        ("Recursos Humanos", "Recursos Humanos"),
        ("Coordenadoria de Terras", "Coordenadoria de Terras"),
        ("Tec. Informação e Tecnologia", "Tec. Informação e Tecnologia"),
        ("Defesa Civil", "Defesa Civil"),
        ("Polo Moveleiro", "Polo Moveleiro"),
        ("Licitações e Contratos", "Licitações e Contratos"),

    )),

    ('OUTRAS',(
        ("Assessoria de comunicação", "Assessoria de comunicação"),
        ("Trânsito e Transporte", "Trânsito e Transporte"),
        ("Relações com a Comunidade", "Relações com a Comunidade"),
        ("Procuradoria Geral", "Procuradoria Geral"),
        ("PROCON", "PROCON"),
        ("Departamento de arrecadação", "Departamento de arrecadação"),
        ("Controladoria Geral" ,"Controladoria Geral"),
    )),
)

PERIFERICOS = (

    ('NOBREAK',(
        ("1000VA", "1000VA"),
        ("1200VA", "1200VA"),
        ("1300VA", "1300VA"),
        ("1400VA", "1400VA"),
        ("1600VA", "1600VA"),
        ("1800VA", "1800VA"),
        ("2400VA", "2400VA"),
        ("400VA", "400VA"),
        ("500VA", "500VA"),
        ("600VA", "600VA"),
        ("700VA", "700VA"),
        ("800VA", "800VA"),
    )),

    ('MONITORES',(
        ("15.6 Polegadas", "15.6 Polegadas"),
        ("17 Polegadas", "17 Polegadas"),
        ("18.5 Polegadas", "18.5 Polegadas"),
        ("19 Polegadas", "19 Polegadas"),
        ("20 Polegadas", "20 Polegadas"),
        ("21.5 Polegadas", "21.5 Polegadas"),
        ("24 Polegadas" ,"24 Polegadas"),
        ("25 Polegadass" ,"25 Polegadas"),
        ("27 Polegadas" ,"27 Polegadas"),
        ("28 Polegadas" ,"28 Polegadas"),
        ("31,5 Polegadas" ,"31,5 Polegadas"),
    )),
)


AQUISICAO = (
        ("Patrimônio", "Patrimônio"),
        ("Contrato", "Contrato"),
        ("Sem Patrimônio", "Sem Patrimônio"),
)

CONFIGURACAO = (
    ("PROCESSADOR",(
        ("AMD A", "AMD A"),
        ("AMD Athlon/Sempron", "AMD Athlon/Sempron"),
        ("AMD FX", "AMD FX"),
        ("AMD Phenom", "AMD Phenom"),
        ("AMD Ryzen 3", "AMD Ryzen 3"),
        ("AMD Ryzen 5", "AMD Ryzen 5"),
        ("AMD Ryzen 7", "AMD Ryzen 7"),
        ("INTEL Atom", "INTEL Atom"),
        ("INTEL Celeron", "INTEL Celeron"),
        ("INTEL Pentium", "INTEL Pentium"),
        ("INTEL Core i3", "INTEL Core i3"),
        ("INTEL Core i5", "INTEL Core i5"),
        ("INTEL Core i7", "INTEL Core i7"),
    )),

    ("HDD/SSD",(
        ("80 GB","80 GB"),
        ("100 GB","100 GB"),
        ("120 GB","120 GB"),
        ("160 GB","160 GB"),
        ("200 GB","200 GB"),
        ("250 GB","250 GB"),
        ("500 GB","500 GB"),
        ("1 TB","1 TB"),
        ("2 TB","2 TB"),
        ("3 TB","3 TB"),
        ("4 TB","4 TB"),
    )),

    ("MEMÓRIA RAM",(
        ("1 GB", "1 GB"),
        ("2 GB", "2 GB"),
        ("4 GB", "4 GB"),
        ("6 GB", "6 GB"),
        ("8 GB", "8 GB"),
        ("12 GB", "12 GB"),
        ("32 GB", "32 GB"),
    )),
        ("PLACA DE VÍDEO",(
        ("1 GB", "1 GB"),
        ("2 GB", "2 GB"),
        ("4 GB", "4 GB"),
        ("6 GB", "6 GB"),
        ("8 GB", "8 GB"),
    )),
)

IMPRESSORA = (
    ("AQUISIÇÃO",(
        ("Patrimônio", "Patrimônio"),
        ("Contrato", "Contrato"),
        ("Sem Patrimônio", "Sem Patrimônio"),
        ("Não Possui", "Não Possui"),
    )),

    ("MULTIFUNCIONAIS",(
        ("Com Fax", "Com Fax"),
        ("Sem Fax", "Sem Fax"),
    )),

    ("MARCAS",(
        ("Brother", "Brother"),
        ("Ricoh", "Ricoh"),
        ("Canon", "Canon"),
        ("Samsung", "Samsung"),
        ("Elgin", "Elgin"),
        ("Epson", "Epson"),
        ("Hp", "Hp"),
        ("Kyocera", "Kyocera"),
        ("Lexmark", "Lexmark"),
        ("Xerox", "Xerox"),
        ("MITSUSHIBA", "MITSUSHIBA"),
        ("Maxprint", "Maxprint"),
        ("PCYes", "PCYes"),
    )),

    ("TIPO",(
        ("Jato de Tinta", "Jato de Tinta"),
        ("Laser", "Laser"),
        ("Pagewide", "Pagewide"),
        ("Plotter", "Plotter"),
        ("Térmica", "Térmica"),
        ("Matricial", "Matricial"),
        ("Portátil", "Portátil"),
        ("Fotográfica", "Fotográfica"),
    )),

    ("IMPRESSÃO",(
        ("Monocromático", "Monocromático"),
        ("Colorido", "Colorido"),
    )),
)

SOFTWARES = (
    ("SISTEMA OPERACIONAL TIPO WINDOWS",(
        ("Windows 7", "Windows 7"),
        ("Windows 8", "Windows 8"),
        ("Windows 10", "Windows 10"),
        ("Windows XP", "Windows XP"),
        ("Windows Vista", "Windows Vista"),
    )),

    ("SISTEMA OPERACIONAL TIPO UNIX",(
        ("Debin", "Debian"),
        ("Mint", "Mint"),
        ("Fedora", "Fedora"),
        ("Ubuntu", "Ubuntu"),
    )),

    ("OUTRO",(
        ("DUAL BOOT", "DUAL BOOT"),
    )),

    ("SOFTWARES GRATUITOS",(
        ("7zip", "7zip"),
        ("Adobe Reader DC ", "Adobe Reader DC "),
        ("Bizagi Modeler Free ", "Bizagi Modeler Free "),
        ("Chrome", "Chrome"),
        ("CutePDF Write Free ", "CutePDF Write Free"),
        ("doPDF", "doPDF"),
        ("Firefox ", "Firefox "),
        ("Foxit Reader 7", "Foxit Reader 7"),
        ("Google Earth", "Google Earth"),
        ("Internet Explorer", "Internet Explorer"),
        ("Java Run Time", "Java Run Time"),
        ("K-Lite Codec Pack", "K-Lite Codec Pack"),
        ("LibreOffice", "LibreOffice"),
        ("Microsoft Power BI Desktop", "Microsoft Power BI Desktop"),
        ("Modulo de segurança Bancário", "Modulo de segurança Bancário"),
        ("QGIS", "QGIS"),
        ("VLC – Player", "VLC – Player"),
        ("Winrar", "Winrar"),
    )),

    ("SOFTWARES LICENCIADOS",(
       ("Adobe Acrobat DC", "Adobe Acrobat DC"),
       ("Adobe Creative Cloud", "Adobe Creative Cloud"),
       ("ArcGIS", "ArcGIS"),
       ("AutoCAD", "AutoCAD"),
       ("CorelDRAW", "CorelDRAW"),
       ("Kaspersky Endpoint Security", "Kaspersky Endpoint Security"),
       ("Microsoft Windows Office 2007 Professional", "Microsoft Windows Office 2007 Professional"),
       ("Microsoft Windows Office 2010 Professional", "Microsoft Windows Office 2010 Professional"),
       ("Microsoft Windows Office 2013 Professional", "Microsoft Windows Office 2013 Professional"),
    )),
    ("SOFTWARES ADMINISTRATIVOS",(
       ("AdmCGM", "AdmCGM"),
       ("AdmConvenio", "AdmConvenio"),
       ("AdmPFiscal", "AdmPFiscal"),
       ("AdmSEHAB", "AdmSEHAB"),
       ("AdmSEMSA", "AdmSEMSA"),
       ("AdmSEPLAN", "AdmSEPLAN"),
       ("CPL Processos", "CPL Processos"),
       ("CRCPL","CRCPL"),
       ("CplCGM ","CplCGM "),
       ("Desenvolve Parauapebas","Desenvolve Parauapebas"),
       ("NewBOAT","NewBOAT"),
       ("PGM Processos","PGM Processos"),
       ("PLAT - Registro de Atividades","PLAT - Registro de Atividades"),
       ("PatioController","PatioController"),
       ("Planeja Municipio","Planeja Municipio"),
       ("Processo Administrativo","Processo Administrativo"),
       ("Projeto Base","Projeto Base"),
       ("Prorural","Prorural"),
       ("SIM - Serviço de Inspeção Municipal","SIM - Serviço de Inspeção Municipal"),
       ("SISGEM - Escola de Música","SISGEM - Escola de Música"),
       ("SISPPAR - Sistema de Parcerias","SISPPAR - Sistema de Parcerias"),
       ("SisBOAT ","SisBOAT "),
       ("SisMulher ","SisMulher"),
       ("SisProtocolo","SisProtocolo"),
       ("Social","Social"),
       ("Transparência RH","Transparência RH"),
       ("WebVISA ","WebVISA"),

    )),
)


class Secretaria(models.Model):
    data_de_cadastro = models.DateTimeField(auto_now_add=True, null=True)
    secretaria = models.CharField('SECRETARIA', max_length= 50, choices=SECRETARIA_CHOICES, null=True, blank=True)
    departamento = models.CharField('DEPARTAMENTO', max_length= 60, null=True, blank=True)
    endereco = models.CharField('ENDEREÇO', max_length= 60, null=True, blank=True)
    responsalvel= models.CharField('RESPONSÁVEL', max_length= 60, null=True, blank=True)

    class Meta:
        verbose_name = _("Secretaria")
        verbose_name_plural = _("Secretarias")
    
    def __str__(self):
        return self.secretaria

    def save(self, *args, **kwargs):
        return super(Secretaria, self).save(*args, **kwargs)

class Computadores(models.Model):
    cadastro = models.ForeignKey(Secretaria, on_delete= models.CASCADE, null=True)

    aquisição_equipamento = MultiSelectField(_("TIPO DE AQUISIÇÃO"),choices= AQUISICAO, max_length= 200, max_choices=1, null=True, blank=True)
    patrimonio_pc = models.CharField(_("PATRIMÔNIO PC"), max_length=200, null=True, blank=True)
    usuario = models.CharField(_("USUÁRIO"), max_length=200, null=True, blank=True)
    configuracao_geral = MultiSelectField(_("CONFIGURAÇÃO GERAL"),choices= CONFIGURACAO, max_length= 200, max_choices=10, null=True, blank=True)
    impressora_scanner = MultiSelectField(_("IMPRESSORA/SCANNER"), choices= IMPRESSORA, max_length= 200, max_choices=10, null=True, blank=True)
    patrimonio_impressora = models.CharField(_("PATRIMÔNIO IMPRESSORA"), max_length=50, null=True, blank=True)
    perifericos = MultiSelectField(_("PERIFERICOS"), choices= PERIFERICOS, max_length= 50, max_choices=20, null=True, blank=True)
    patrimonio_nobreak = models.CharField(_("PATRIMÔNIO NOBREAK"), max_length=50, null=True, blank=True)
    patrimonio_monitor = models.CharField(_("PATRIMÔNIO MONITOR"), max_length=50, null=True, blank=True)
    softwares = MultiSelectField(_("SOFTWARE"),choices= SOFTWARES, max_length= 200, max_choices=15, null=True, blank=True)
    observacao = models.TextField("OBSERVAÇÃO", max_length=300, null=True, blank=True)

    

    class Meta:
        verbose_name = _("Computador")
        verbose_name_plural = _("Computadores")