# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.conf import settings
# from django.core.validators import RegexValidator
from django.urls import reverse

class Metakinhsh(models.Model):
  metak_from = models.CharField('Από', max_length=100)
  metak_to = models.CharField('Προορισμός', max_length=100)
  date_from = models.DateField('Ημ/νία Από')
  date_to = models.DateField('Ημ/νία Έως')
  km = models.IntegerField('Χιλιόμετρα')
  egkrish = models.BooleanField('Έγκριση', default=False)
  pragmat = models.BooleanField('Πραγματοποιήθηκε', default=False)
  aitiologia = models.TextField('Αιτιολογία')
  person = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, verbose_name='Χρήστης')
  
  class Meta:
    verbose_name = 'Μετακίνηση'
    verbose_name_plural = 'Μετακινήσεις'

  def __str__(self):
    return f'{self.person.last_name} -> {self.metak_to} @ {self.date_from}'
  def get_absolute_url(self): # new
    return reverse('metakinhsh_list')#, args=[str(self.id)])
