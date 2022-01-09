from django.db import models

# Create your models here.

class Encuesta(models.Model):
    id = models.AutoField(primary_key = True)
    correo = models.EmailField(max_length = 100)
    rango_edad = models.CharField(max_length = 5)
    sexo = models.CharField(max_length = 10)
    red_social_fav = models.CharField(max_length = 20)

    # Tiempo promedio al dia en minutos.

    prom_FB = models.PositiveIntegerField() # Facebook.
    prom_WA = models.PositiveIntegerField() # WhatsApp.
    prom_TW = models.PositiveIntegerField() # Twitter.
    prom_IN = models.PositiveIntegerField() # Instagram.
    prom_TK = models.PositiveIntegerField() # TikTok.

    def __str__(self) -> str:
        texto = "{0} ({1})"
        return texto.format(self.correo, self.id)