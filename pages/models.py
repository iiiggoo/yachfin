from django.db import models

class Reservation(models.Model):
    names = models.CharField(max_length=50)
    emails = models.EmailField(max_length=254)
    phones = models.CharField(max_length=20)
    days = models.CharField(max_length=500)
    times = models.CharField(max_length=20)
    notes = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=False,verbose_name='i readed this message')
    viewed = models.BooleanField(default=False) 
    def __str__(self):  
        return self.emails 
    class Meta:
        ordering = ['status']