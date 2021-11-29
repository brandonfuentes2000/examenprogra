from django.db import models
from django.contrib import admin

class Alumno(models.Model):
    nombre  =   models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    nombre    = models.CharField(max_length=60)
    alumnos   = models.ManyToManyField(Alumno, through='Actuacion')

    def __str__(self):
        return self.nombre

class Actuacion (models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

class ActuacionInLine(admin.TabularInline):
    model = Actuacion
    extra = 1

class AlumnoAdmin(admin.ModelAdmin):
    inlines = (ActuacionInLine,)

class CursoAdmin (admin.ModelAdmin):
    inlines = (ActuacionInLine,)