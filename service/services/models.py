from django.db import models
from django.core.validators import MaxValueValidator
from clients.models import Client

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    full_price = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Plan(models.Model):
    Plan_types = (
        ('full','Full'),
        ('student','Student'),
        ('discount','Discount')
    )

    plan_type = models.CharField(choices=Plan_types,max_length=100)
    discount_percent = models.PositiveIntegerField(default=0,validators=[MaxValueValidator(100)])

    def __str__(self):
        return self.plan_type


class Subscription(models.Model):
    client = models.ForeignKey(to=Client,related_name='subscriptions',on_delete=models.PROTECT)
    service = models.ForeignKey(to=Service,related_name='subscriptions',on_delete=models.PROTECT)
    plan = models.ForeignKey(to=Plan,related_name='subscriptions',on_delete=models.PROTECT)
