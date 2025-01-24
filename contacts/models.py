from django.db import models

class Contacts(models.Model):
    image = models.ImageField(upload_to='contacts/')
    phone_numbers = models.CharField(max_length=15)
    fax_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()
    address = models.TextField()