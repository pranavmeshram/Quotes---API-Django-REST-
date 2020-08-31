from django.db import models

# Create your models here.

class Quotes(models.Model):
    sr_lang = models.TextField(blank=True, null=True)
    en_lang = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=50)
    source = models.CharField(max_length=150, blank=True, null=True)
    rating = models.FloatField()


    class Meta:
        verbose_name = "Quote"
        verbose_name_plural = 'Quotes'


    def __str__(self):
        return str(self.sr_lang) + ' (====> converts to ====>) ' +str(self.en_lang)