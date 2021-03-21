from django.db import models


# Create your models here.
class Main(models.Model):
    weather = models.CharField('Sun Cloudy Rain', max_length=40, null=True)
    links = models.CharField('pc1:url,pc2:url', max_length=250, null=True)
    nfc_codes = models.CharField('name#code,name#code,name#code', max_length=250, null=True)
    temperature = models.CharField('Exam. 24', max_length=250, null=True)
    custom_text = models.CharField('Any Text In ENGLISH', max_length=250, null=True)

    mode = models.CharField('0 - 4', max_length=250, null=True)
    date = models.DateTimeField('Date', auto_now_add=True)
