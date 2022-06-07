from tkinter import Text
from django.contrib import admin
from django.forms import TextInput
from .models import Paciente, Reevaluacion
from django import forms

# Register your models here.

admin.site.site_header = "Expediente Clínico AESKVLAPIVS "
admin.site.site_title = "AESKVLAPIVS"
admin.site.index_title = "Bienvenido a tu escritorio médico"


class PacienteAdmin(admin.ModelAdmin):
	list_display = ['name', 'phone', 'email','diagnosis','dextrostix', 'a1c', 'imc', 'climc','timestamp']
	readonly_fields = ('timestamp', 'update')
	search_fields = ('name', 'phone', 'email')
	list_filter = ['entitlement']


class ReevaluacionAdmin(admin.ModelAdmin):
	list_display=['paciente', 'phone', 'email', 'dextrostix', 'a1c', 'imc', 'climc', 'per_abdominal', 'immediate_background', 'timestamp', 'reevaluación']
	readonly_fields = ('timestamp', 'update')
	list_filter = ['timestamp', 'entitlement']
	search_fields = ('paciente__name', 'phone', 'email')
	


admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Reevaluacion, ReevaluacionAdmin)





