from ast import Continue, If, Return
from binascii import a2b_base64
from django.db import models
from math import sqrt
# Create your models here.

class Paciente(models.Model):
    FEMENINO= 'FEM'
    MASCULINO = 'MASC'
    GENERO = [(FEMENINO, 'Femenino'), (MASCULINO, 'Masculino')]  

    IMSS = 'IMSS'
    ISSSTE = 'ISSSTE'
    SecMarina = 'Secretaría de Marina'
    PEMEX = 'PEMEX'
    SEDENA = 'SEDENA'
    OTRO = 'Otro'
    DERECHOHABIENCIA = [(IMSS, 'IMSS'), (ISSSTE, 'ISSSTE'), (SecMarina, 'Secretaría de Marina'),
    (SEDENA, 'SEDENA'), (PEMEX, 'PEMEX'), (OTRO, 'Otro')]

    POSITIVO = 'POS'
    NEGATIVO = 'NEG' 
    REHAB = 'En Rehabilitación'
    OCACIONAL = 'Ocacional'
    SOCIAL = 'Social'
    SUSPENDIDO = 'Suspendido'
    AFIRMACION = [ (POSITIVO, 'Positivo'), (NEGATIVO, 'Negativo'), (REHAB, 'En Rehabilitación')] 
    AFIRMACION_TAB = [ (POSITIVO, 'Positivo'), (NEGATIVO, 'Negativo'), (SUSPENDIDO, 'Suspendido')] 
    AFIRMACION_SIMPLE = [ (POSITIVO, 'Positivo'), (NEGATIVO, 'Negativo')]
    AFIRMACION_ALCOHOLISMO = [ (POSITIVO, 'Positivo'), (NEGATIVO, 'Negativo'), (REHAB, 'En Rehabilitación'), 
    (OCACIONAL, 'Ocacional'), (SOCIAL, 'Social')]

    #Identificación

    name = models.CharField(max_length=100, verbose_name='Nombre')
    gender = models.CharField(max_length=4, choices=GENERO, verbose_name='Género')
    age = models.SmallIntegerField(verbose_name='Edad')
    nationality = models.CharField(max_length=50, blank=True, null=True, verbose_name='Nacionalidad')
    etnia = models.CharField(max_length=50, blank=True, null=True, verbose_name='Etnia')
    scholarship = models.CharField(max_length=50, blank=True, null=True, verbose_name='Escolaridad')
    job = models.CharField(max_length=100, blank=True, null=True, verbose_name='Empleo')
    religion = models.CharField(max_length=50, blank=True, null=True, verbose_name='Religión')
    sport = models.CharField(max_length=50, blank=True, null=True, verbose_name='Deportes')
    civil_status = models.CharField(max_length=50, blank=True, null=True, verbose_name='Estado Civil')
    adress = models.CharField(max_length=2150, blank=True, null=True, verbose_name='Domicilio')
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, verbose_name='Teléfono')
    entitlement = models.CharField(max_length=50, choices=DERECHOHABIENCIA, blank=True, null=True, verbose_name='Derechohabiencia')
    specify= models.CharField(max_length=30, verbose_name='Especifique otra derechohabiencia', blank=True, null=True)
    insurance = models.CharField(max_length=30, blank=True, null=True, verbose_name='Aseguradora')
    
    # Padeciemiento Actual

    immediate_background = models.TextField(verbose_name="Padecimiento o Situación Actual")

    #ANTECEDENTES

    smoking = models.CharField(max_length=20, choices=AFIRMACION_TAB, blank=True, null=True, verbose_name='Tabaquismo')
    alcohol = models.CharField(max_length=20,choices=AFIRMACION_ALCOHOLISMO, blank=True, null=True, verbose_name='Alcholismo')
    drugs_adictions = models.CharField(max_length=20,choices=AFIRMACION, blank=True, null=True, verbose_name='Adicciones')
    allergies = models.CharField(max_length=100,choices=AFIRMACION, blank=True, null=True, verbose_name='Alergias')
    dislipidemia = models.CharField(max_length=100,choices=AFIRMACION_SIMPLE, blank=True, null=True )
    dm = models.CharField(max_length=100,choices=AFIRMACION_SIMPLE, blank=True, null=True, verbose_name='Diabetes')
    hta = models.CharField(max_length=100,choices=AFIRMACION_SIMPLE, blank=True, null=True, verbose_name='HTA')
    inf_ang_de_pecho = models.CharField(max_length=100,choices=AFIRMACION_SIMPLE, blank=True, null=True, verbose_name='Infartos o angina de pecho')
    evc = models.CharField(max_length=100,choices=AFIRMACION_SIMPLE, blank=True, null=True, verbose_name='Eventos Cerebrovasculares')
    ivp = models.CharField(max_length=100,choices=AFIRMACION_SIMPLE, blank=True, null=True, verbose_name='Insuficiencia vascular periférica')
    EPOC = models.CharField(max_length=100,choices=AFIRMACION_SIMPLE, blank=True, null=True, verbose_name='Enfermedad Pulmonar Obstructiva Crónica')
    cancer = models.CharField(max_length=100,choices=AFIRMACION_SIMPLE, blank=True, null=True, verbose_name='Cáncer')
    
    otras_enf = models.TextField(blank=True, null=True, verbose_name='Complemento, Otros Antecedentes y Enfermedades')
    cir_previas = models.CharField(max_length=200, blank=True, null=True, verbose_name='Cirugías previas')

    dxs_antec = models.TextField(blank=True, null=True, verbose_name='Resumen de Diagnósticos por Antecedentes', help_text='No esciriba aquí: Guarde para ver Resultados')

    obs = models.TextField(blank=True, null=True, verbose_name='Observaciones, otros antecedentes y tratamientos actuales')

    # Situación actual y Exploración

    actual_situation = models.TextField(verbose_name="Situación Actual y Exploración")
    tension_sistolica = models.IntegerField(blank=True, null=True, default=1)
    tension_diastolica = models.PositiveSmallIntegerField(blank=True, null=True, default=1)
    pam = models.IntegerField(default=0, verbose_name='PAM', help_text='No esciriba aquí: Guarde para ver Resultados')
    fc = models.IntegerField(blank=True, null=True, verbose_name='FC')
    fr= models.IntegerField(blank=True, null=True, verbose_name='FR')
    temp =  models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2, verbose_name='Temp')
    saturacion = models.IntegerField(blank=True, null=True, verbose_name='Sa02')
    dextrostix = models.IntegerField(blank=True, null=True, verbose_name='Dextrostix')
    a1c = models.CharField(max_length=5, blank=True, null=True)
    peso = models.FloatField(blank=True, null=True, default=0) 
    estatura = models.FloatField(blank=True, null=True, default=1)
    imc = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name='IMC', help_text='No esciriba aquí: Guarde para ver Resultados')
    climc = models.CharField(max_length=100, blank=True, null=True, verbose_name='Clasificación Masa Corporal', help_text='No esciriba aquí: Guarde para ver Resultados')
    asc = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name='ASC', help_text='No esciriba aquí: Guarde para ver Resultados')
    per_abdominal = models.IntegerField(blank=True, null=True, verbose_name='Per. Abd en cms')

    # Paraclínicos

    Imagenología1 = models.FileField(upload_to='Paciente',help_text='formato jpg, jpge', blank=True, null=True )
    Imagenología2 = models.FileField(upload_to='Paciente', help_text='formato jpg, jpge',blank=True, null=True)
    Imagenología3 = models.FileField(upload_to='Paciente',help_text='formato jpg, jpge',blank=True, null=True)

    Labs1 = models.FileField(upload_to='Paciente', help_text='formato pdf',blank=True, null=True)
    Labs2 = models.FileField(upload_to='Paciente', help_text='formato pdf', blank=True, null=True)
    recetas = models.FileField(upload_to='Paciente', help_text='formato pdf',blank=True, null=True, verbose_name='Recetas')

    #Diagnóticos y Tx

    diagnosis = models.TextField(verbose_name='Diagnósticos')
    obs = models.TextField(verbose_name="Observaciones")
    txs = models.TextField(verbose_name='Manejos y Tratamientos')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Fecha de Registro')
    update = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')
    reevaluación = models.DateTimeField(blank=True, null=True, verbose_name='prox. reevaluación')
    

    @property
    def tabaquismo(self):
        if self.smoking == 'POS':
            POS = 'TABQUISMO'
            return POS

        
    @property
    def alcoholismo(self):
        if self.alcohol == 'POS':
            return 'ALCOHOLISMO ACTIVO'
                
        
    @property
    def adiccion(self):
        if self.drugs_adictions == 'POS':
            POS = 'ESPECIFIQUE LAS ADICCIONES'
            return POS
                
    
    @property
    def alergias(self):
        if self.allergies == 'POS':
            POS = 'ESPECIFIQUE ALERGIAS'
            return POS

    @property
    def dislpid (self):
        if self.dislipidemia == 'POS':
            POS = 'DISLIPIDEMIA'
            return POS
                
            
    @property
    def diabetes(self):
        if self.dm == 'POS':
            POS = 'DIABETES MELLITUS'
            return POS
            
                
    
    @property
    def hipertension (self):
        if self.hta == 'POS': 
            POS = 'HTA'
            return POS
                

    @property
    def cardiopatia(self):
        if self.inf_ang_de_pecho == 'POS':
            POS = 'CARDIOPATIA ISQUEMICA'
            return POS


    @property
    def encefalopatía(self):
        if self.evc == 'POS':
            POS = 'ENCEFALOPATIA VASCULAR'
            return POS
                

    @property
    def insuf_vasc(self):
        if self.ivp == 'pos':
            POS = 'INSUFICIENCIA VASCULAR PERIFERICA'
            return POS
                    

    @property
    def enf_pulm(self):
        if self.EPOC == 'POS':
            POS = 'EPOC'
            return POS

    @property
    def onc(self):
        if self.cancer == 'POS':
            POS = 'ESPECIFIQUE DATOS DEL CANCER'
            return POS


    @property
    def presion_media(self):
        return (self.tension_sistolica + (2 * self.tension_diastolica))/3 

    @property
    def masa_corporal(self):
        return self.peso/self.estatura ** 2


    @property
    def area_sup_corp(self):
        return sqrt (self.peso * (self.estatura * 100) / 3600)

    @property
    def imc_clasif(self):
        if self.imc < 18.5 and self.imc > 1:
            return 'Desnutrición'
        
        elif self.imc >18.5 and self.imc <24.9:
            return 'Normal'

        elif self.imc >25 and self.imc < 26.9:
            return 'Sobrepeso Grado I'

        elif self.imc >27 and self.imc < 29.9:
            return 'Sobrepeso Grado II'

        elif self.imc >30 and self.imc < 34.9:
            return 'Obesidad Tipo I'

        elif self.imc >35 and self.imc < 39.9:
            return 'Obesidad Tipo II'

        elif self.imc >40 and self.imc < 49.9:
            return 'Obesidad Tipo III-Mórbida'

        elif self.imc >50:
            return 'Obesidad Tipo IV-Extrema'
        elif self.imc < 1:
            return 'Hay que pesar al paciente'


    def save(self):
        self.imc = self.masa_corporal
        self.climc = self.imc_clasif
        self.asc = self.area_sup_corp
        self.pam = self.presion_media
        self.dxs_antec = self.tabaquismo, self.alcoholismo, self.alergias, self.dislpid, self.diabetes, self.hipertension, self.cardiopatia, self.insuf_vasc, self.enf_pulm, self.onc
        super(Paciente, self).save()


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='a) Pacientes'

    

class Reevaluacion(models.Model):
    IMSS = 'IMSS'
    ISSSTE = 'ISSSTE'
    SecMarina = 'Secretaría de Marina'
    PEMEX = 'PEMEX'
    SEDENA = 'SEDENA'
    OTRO = 'Otro'
    DERECHOHABIENCIA = [(IMSS, 'IMSS'), (ISSSTE, 'ISSSTE'), (SecMarina, 'Secretaría de Marina'),
    (SEDENA, 'SEDENA'), (PEMEX, 'PEMEX'), (OTRO, 'Otro')]

    paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE)

    entitlement = models.CharField(max_length=50, choices=DERECHOHABIENCIA, blank=True, null=True, verbose_name='Derechohabiencia')

    specify= models.CharField(max_length=30, verbose_name='Especifique otra derechohabiencia', blank=True, null=True)
    
    phone = models.CharField(max_length=15, verbose_name='Teléfono', blank=True, null=True)

    email = models.EmailField(blank=True, null=True)

    dxs_previos = models.TextField(blank=True, null=True)

    immediate_background = models.TextField(verbose_name="Padecimiento o Situación Actual")

    tension_sistolica = models.PositiveSmallIntegerField(blank=True, null=True, default=1)
    tension_diastolica = models.PositiveSmallIntegerField(blank=True, null=True, default=1)
    pam = models.IntegerField(default=0, verbose_name='PAM')
    fc = models.IntegerField(blank=True, null=True, verbose_name='FC')
    fr= models.IntegerField(blank=True, null=True, verbose_name='FR')
    temp =  models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2, verbose_name='Temp')
    saturacion = models.IntegerField(blank=True, null=True, verbose_name='Sa02')
    dextrostix = models.IntegerField(blank=True, null=True, verbose_name='Dextrostix', default=0)
    a1c = models.CharField(max_length=5, blank=True, null=True)
    peso = models.FloatField(blank=True, null=True, default=0) 
    estatura = models.FloatField(blank=True, null=True, default=1)
    imc = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name='IMC')
    climc = models.CharField(max_length=100, blank=True, null=True, verbose_name='Calsificación Masa Corporal')
    asc = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name='ASC')
    per_abdominal = models.IntegerField(blank=True, null=True, verbose_name='Per. Abd en cms')
    expl = models.TextField(verbose_name='Complemente Exploración', blank=True, null=True)


     # Paraclínicos

    Imagenología1 = models.FileField(upload_to='Reevalucion', help_text='formato jpg, jpge', blank=True, null=True)
    Imagenología2 = models.FileField(upload_to='Reevalucion', help_text='formato jpg, jpge', blank=True, null=True)
    Imagenología3 = models.FileField(upload_to='Reevalucion', help_text='formato jpg, jpge', blank=True, null=True)

    Labs1 = models.FileField(upload_to='Reevalucion', help_text='formato pdf, jpg, jpge', blank=True, null=True)
    Labs2 = models.FileField(upload_to='Reevalucion',help_text='formato pdf, jpg, jpge', blank=True, null=True)
    recetas = models.FileField(upload_to='Reevalucion', help_text='formato pdf, jpg, jpge', blank=True, null=True, verbose_name='Recetas')

    #Diagnóticos y Tx

    diagnosis = models.TextField(verbose_name='Diagnósticos')
    obs = models.TextField(verbose_name="Observaciones")
    txs = models.TextField(verbose_name='Manejos y Tratamientos')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Fecha de Registro')
    update = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')
    reevaluación = models.DateTimeField(blank=True, null=True, verbose_name='prox. reevaluación')


    @property
    def presion_media(self):
        return (self.tension_sistolica + (2 * self.tension_diastolica))/3 

    @property
    def masa_corporal(self):
        return self.peso/self.estatura ** 2

    @property
    def imc_clasif(self):
        if self.imc < 18.5 and self.imc > 1:
            return 'Desnutrición'
        
        elif self.imc >18.5 and self.imc <24.9:
            return 'Normal'

        elif self.imc >24.9 and self.imc < 26.99:
            return 'Sobrepeso Grado I'

        elif self.imc > 27 and self.imc < 29.99:
            return 'Sobrepeso Grado II'

        elif self.imc >30 and self.imc < 34.9:
            return 'Obesidad Tipo I'

        elif self.imc >35 and self.imc < 39.9:
            return 'Obesidad Tipo II'

        elif self.imc >40 and self.imc < 49.9:
            return 'Obesidad Tipo III-Mórbida'

        elif self.imc >50:
            return 'Obesidad Tipo IV-Extrema'
        elif self.imc < 1:
            return 'Hay que pesar al paciente'


    @property
    def area_sup_corp(self):
        return sqrt (self.peso * (self.estatura * 100) / 3600)


    def save(self):
        self.imc = self.masa_corporal
        self.climc = self.imc_clasif
        self.asc = self.area_sup_corp
        self.pam = self.presion_media
        super(Reevaluacion, self).save()
        

    
    def __str__(self):
        return self.immediate_background

    class Meta:
        verbose_name_plural='b) Reevaluación'


   



