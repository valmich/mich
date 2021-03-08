from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
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
        ("Coord. de Terras", "Coord. de Terras"),
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

AQUISICAO = (
        ("Patrimônio", "Patrimônio"),
        ("Contrato", "Contrato"),
        ("Sem Patrimônio", "Sem Patrimônio"),
)

CONFIGURACAO_PROCESSADOR = (
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
    )

CONFIGURACAO_HDD_SSD = (
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
    )

CONFIGURACAO_MEMORIA_RAM =(
        ("1 GB", "1 GB"),
        ("2 GB", "2 GB"),
        ("3 GB", "3 GB"),
        ("4 GB", "4 GB"),
        ("6 GB", "6 GB"),
        ("8 GB", "8 GB"),
        ("12 GB", "12 GB"),
        ("16 GB", "16 GB"),
        ("32 GB", "32 GB"),
    )

CONFIGURACAO_PLACA_GRAFICA =(
        ("Classe A", "Classe A"),
        ("Classe B", "Classe B"),
        ("Classe C", "Classe C"),
        ("Não", "Não"),
    )

IMPRESSORA_AQUISICAO = (
        ("Patrimônio", "Patrimônio"),
        ("Contrato", "Contrato"),
        ("Sem Patrimônio", "Sem Patrimônio"),

    )

# IMPRESSORA_MULTIFUNCIONAIS_FAX = (
#         ("Com Fax", "Com Fax"),
#         ("Sem Fax", "Sem Fax"),
#     )

# IMPRESSORA_MULTIFUNCIONAIS_SCANNER = (
#         ("Com Scanner", "Com Scanner"),
#         ("Sem Scanner", "Sem Scanner"),
#     )

IMPRESSORA_MARCAS= (
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
    )

IMPRESSORA_TIPO =(
        ("Jato de Tinta", "Jato de Tinta"),
        ("Laser", "Laser"),
        ("Pagewide", "Pagewide"),
        ("Plotter", "Plotter"),
        ("Térmica", "Térmica"),
        ("Matricial", "Matricial"),
        ("Portátil", "Portátil"),
        ("Fotográfica", "Fotográfica"),
    )

IMPRESSORA_IMPRESSAO=(
        ("Monocromático", "Monocromático"),
        ("Colorido", "Colorido"),
    )

NOBREAK=(
        ("400VA", "400VA"),
        ("500VA", "500VA"),
        ("600VA", "600VA"),
        ("700VA", "700VA"),
        ("800VA", "800VA"),
        ("1000VA", "1000VA"),
        ("1200VA", "1200VA"),
        ("1300VA", "1300VA"),
        ("1400VA", "1400VA"),
        ("1600VA", "1600VA"),
        ("1800VA", "1800VA"),
        ("2400VA", "2400VA"),

    )

MONITORES=(
        ("14 Polegadas", "14 Polegadas"),
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
    )

SOFTWARES_OS = (
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
)
SOFTWARES_GRATUITOS=(
        ("7zip", "7zip"),
        ("Bizagi Modeler Free ", "Bizagi Modeler Free"),
        ("Chrome", "Chrome"),
        ("Adobe Reader DC ", "Adobe Reader DC"),
        ("CutePDF Write Free", "CutePDF Write Free"),
        ("doPDF", "doPDF"),
        ("Firefox", "Firefox"),
        ("Foxit Reader 7", "Foxit Reader 7"),
        ("Google Earth", "Google Earth"),
        ("Internet Explorer", "Internet Explorer"),
        ("Java Run Time", "Java Run Time"),
        ("K-Lite Codec Pack", "K-Lite Codec Pack"),
        ("LibreOffice", "LibreOffice"),
        ("Microsoft Power BI Desktop", "Microsoft Power BI Desktop"),
        ("Modulo de segurança Bancário", "Modulo de segurança Bancário"),
        ("QGIS", "QGIS"),
        ("VLC–Player", "VLC–Player"),
        ("Winrar", "Winrar"),
    )

SOFTWARES_LICENCIADOS=(
       ("Adobe Acrobat DC", "Adobe Acrobat DC"),
       ("Adobe Creative Cloud", "Adobe Creative Cloud"),
       ("ArcGIS", "ArcGIS"),
       ("AutoCAD", "AutoCAD"),
       ("CorelDRAW", "CorelDRAW"),
       ("Kaspersky Endpoint Security", "Kaspersky Endpoint Security"),
       ("Microsoft Windows Office 2007 Professional", "Microsoft Windows Office 2007 Professional"),
       ("Microsoft Windows Office 2010 Professional", "Microsoft Windows Office 2010 Professional"),
       ("Microsoft Windows Office 2013 Professional", "Microsoft Windows Office 2013 Professional"),
       ("Microsoft Windows Office 2016 Professional", "Microsoft Windows Office 2016 Professional"),
    )

SOFTWARES_ADMINISTRATIVOS =(
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
       ("SIM-Serviço de Inspeção Municipal","SIM-Serviço de Inspeção Municipal"),
       ("SISGEM-Escola de Música","SISGEM-Escola de Música"),
       ("SISPPAR-Sistema de Parcerias","SISPPAR-Sistema de Parcerias"),
       ("SisBOAT ","SisBOAT "),
       ("SisMulher ","SisMulher"),
       ("SisProtocolo","SisProtocolo"),
       ("Social","Social"),
       ("Transparência RH","Transparência RH"),
       ("WebVISA ","WebVISA"),

)


class Secretaria(models.Model):
    data_de_cadastro = models.DateTimeField(auto_now_add=True, null=True)
    secretaria = models.CharField('SECRETARIA', max_length= 50, choices=SECRETARIA_CHOICES, null=True, blank=True)
    departamento = models.CharField('DEPARTAMENTO', max_length= 60, null=True, blank=True)
    endereco = models.CharField('ENDEREÇO', max_length= 60, null=True, blank=True)
    responsavel= models.CharField('RESPONSÁVEL', max_length= 60, null=True, blank=True)

    class Meta:
        verbose_name = _("Secretaria")
        verbose_name_plural = _("Secretarias")
    
    def __str__(self):
        return self.secretaria

    def save(self, *args, **kwargs):
        return super(Secretaria, self).save(*args, **kwargs)

class Computador(models.Model):
    cadastro = models.ForeignKey(Secretaria, on_delete= models.CASCADE, null=True)

    aquisicao_equipamento = models.CharField(_("TIPO DE AQUISIÇÃO"),choices= AQUISICAO, max_length= 50, null=True, blank=True)
    patrimonio_pc = models.CharField(_("PATRIMÔNIO PC"), max_length=50, null=True, blank=True)
    
    processador = models.CharField(_("PROCESSADOR"), choices= CONFIGURACAO_PROCESSADOR, max_length= 50, null=True, blank=True)
    hdd_ssd = models.CharField(_("HDD/SSD"), choices= CONFIGURACAO_HDD_SSD, max_length= 50, null=True, blank=True)
    memoria_ram = models.CharField(_("MEMORIA RAM"), choices= CONFIGURACAO_MEMORIA_RAM, max_length= 50, null=True, blank=True)
    placa_grafica = models.CharField(_("PLACA GRÁFICA"), choices= CONFIGURACAO_PLACA_GRAFICA, max_length= 50, null=True, blank=True)

    class Meta:
        verbose_name = _("Computador")
        verbose_name_plural = _("Computadores")

class Monitor(models.Model):
    cadastro = models.ForeignKey(Secretaria, on_delete= models.CASCADE, null=True)
    
    aquisicao_equipamento = models.CharField(_("TIPO DE AQUISIÇÃO"),choices= AQUISICAO, max_length= 50, null=True, blank=True)
    patrimonio_monitor = models.CharField(_("PATRIMÔNIO MONITOR"), max_length=50, null=True, blank=True)

    tamanho = models.CharField(_("TAMANHO"),choices= MONITORES, max_length= 50, null=True, blank=True)

    class Meta:
        verbose_name = _("Monitor")
        verbose_name_plural = _("Monitores")

class Impressora(models.Model):
    cadastro = models.ForeignKey(Secretaria, on_delete= models.CASCADE, null=True)
    
    aquisicao_equipamento = models.CharField(_("TIPO DE AQUISIÇÃO"),choices = IMPRESSORA_AQUISICAO, max_length= 50, null=True, blank=True)
    patrimonio_impressora = models.CharField(_("PATRIMÔNIO IMPRESSORA"), max_length=50, null = True, blank=True)

    impressora_multi_fax = models.BooleanField(_("POSSUI FAX?"), max_length= 50 , blank=True)
    impressora_multi_scanner = models.BooleanField(_("POSSUI SCANNER?"), max_length= 50, blank=True)
    impressora_marca = models.CharField(_("MARCA"),choices = IMPRESSORA_MARCAS, max_length= 50, null=True, blank=True)
    impressora_tipo = models.CharField(_("TIPO"),choices = IMPRESSORA_TIPO, max_length= 50, null=True, blank=True)
    impressora_impressao = models.CharField(_("IMPRESSÃO"),choices = IMPRESSORA_IMPRESSAO, max_length= 50, null=True, blank=True)

    class Meta:
        verbose_name = _("Impressora")
        verbose_name_plural = _("Impressoras")

class Nobreak(models.Model):
    cadastro = models.ForeignKey(Secretaria, on_delete= models.CASCADE, null=True)
    
    aquisicao_equipamento = models.CharField(_("TIPO DE AQUISIÇÃO"),choices = AQUISICAO, max_length= 50, null=True, blank=True)
    patrimonio_nobreak = models.CharField(_("PATRIMÔNIO NOBREAK"), max_length=50, null = True, blank=True)

    nobreak = models.CharField(_("TENSÃO"),choices = NOBREAK, max_length= 50, null=True, blank=True)

    class Meta:
        verbose_name = _("Nobreak")
        verbose_name_plural = _("Nobreaks")

class SoftwareOs(models.Model):
    cadastro = models.ForeignKey(Secretaria, on_delete= models.CASCADE, null=True)

    sistema_operacional = MultiSelectField(_("SISTEMA OPERACIONAL"), choices= SOFTWARES_OS, max_length= 50, max_choices=3, null=True, blank=True)
    
    class Meta:
        verbose_name = _("Sistema Operacional")
        verbose_name_plural = _("Sistemas Operacionais")

class SoftwareOutro(models.Model):
    cadastro = models.ForeignKey(Secretaria, on_delete= models.CASCADE, null=True)

    software_gratuito = MultiSelectField(_("SOFTWARE GRATUITOS"),choices = SOFTWARES_GRATUITOS, max_choices=20, max_length= 200, null=True, blank=True)
    software_licenciado = MultiSelectField(_("SOFTWARES LICENCIADOS"),choices = SOFTWARES_LICENCIADOS, max_choices=10, max_length= 200, null=True, blank=True)
    licenca = models.CharField(_("Nº DA LICENÇA"), max_length=50, null = True, blank=True)
    software_adminstrativo = MultiSelectField(_("SOFTWARES ADMINISTRATIVOS"),choices = SOFTWARES_ADMINISTRATIVOS, max_choices=30, max_length= 200, null=True, blank=True)

    class Meta:
        verbose_name = _("Outro Software")
        verbose_name_plural = _("Outros Softwares")

