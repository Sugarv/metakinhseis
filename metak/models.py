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
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings


class Metakinhsh(models.Model):
  metak_from = models.CharField('Από', max_length=100)
  metak_to = models.CharField('Προορισμός', max_length=100)
  date_from = models.DateField('Ημ/νία Από')
  date_to = models.DateField('Ημ/νία Έως',null=True)
  km = models.IntegerField('Χιλιόμετρα')
  egkrish = models.BooleanField('Έγκριση', default=False)
  pragmat = models.BooleanField('Πραγματοποιήθηκε', default=False)
  aitiologia = models.TextField('Αιτιολογία')
  person = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, verbose_name='Χρήστης', null=True)
  handler = models.CharField('Χειριστής',max_length=80,default=None,blank=True,null=True,choices=(
      ('Επόπτης', 'Επόπτης'),('Οικονομικό', 'Οικονομικό')))
  
  class Meta:
    verbose_name = 'Μετακίνηση'
    verbose_name_plural = 'Μετακινήσεις'

  def __str__(self):
    return f'{self.person.last_name} -> {self.metak_to} @ {self.date_from}'
  
  def get_absolute_url(self): # new
    return reverse('metakinhsh_list')#, args=[str(self.id)])

# Use signals to send_mail when a new object is created in Metakinhsh
@receiver(post_save, sender=Metakinhsh)
def send_email(sender, instance, created, **kwargs):
    if created:
        fname = instance.person.first_name + ' ' + instance.person.last_name
        formatted_date = instance.date_from.strftime("%d/%m/%Y")
        subject = 'Νέα Μετακίνηση'
        message = f'<h3>Εισαγωγή νέας μετακίνησης</h3><br>Σύμβουλος εκπαίδευσης: <b>{fname}</b><br>Ημερομηνία: <b>{formatted_date}</b><br>\
          Προορισμός: <b>{instance.metak_to}</b><br>Αιτιολογία: <b>{instance.aitiologia}</b>'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = settings.RECIPIENT_LIST  # Replace with the desired recipient email addresses
        # print(message)
        send_mail(subject, message, from_email, recipient_list, html_message=message)
