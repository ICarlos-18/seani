from django.db import models

class Stage(models.Model):
    stage = models.IntegerField(
            verbose_name = "Etapa")
    appliacation_date = models.DateField(
        verbose_name = "Fecha de Apliacación")
    
    @property
    def year(self):
        return self.appliacation_date.year
    
    @property
    def month(self):
        months = ['enero', 'febrero', 'marzo',
            'abril', 'mayo', 'junio',
            'julio', 'agosto', 'septiembre', 
            'octubre', 'noviembre', 'diciembre']
        return months[self.appliacation_date.month -1]
    
    def __str__(self):
        return f"{ self.stage } - { self.month} / { self.year }"
    
    class Meta:
        verbose_name = "etapa"
        verbose_name_plural = "etapas"