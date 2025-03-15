from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(User,on_delete=models.PROTECT)
    company_name = models.CharField(max_length=255)
    full_adress = models.CharField(max_length=255)


    def __str__(self):
        return f"Client: {self.company_name}"