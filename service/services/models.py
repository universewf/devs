from django.db import models
from django.core.validators import MaxValueValidator
from clients.models import Client
from services.tasks import set_price

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    full_price = models.PositiveIntegerField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__full_price = self.full_price

    def save(self, *args,**kwargs):
        if self.full_price != self.__full_price:
            for subscription in self.subscriptions.all():
                set_price.delay(subscription.id)
        return super().save(*args,**kwargs)


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__discount_percent = self.discount_percent

    def save(self, *args,**kwargs):
        if self.discount_percent != self.__discount_percent:
            for subscription in self.subscriptions.all():
                set_price.delay(subscription.id)
        return super().save(*args,**kwargs)


class Subscription(models.Model):
    client = models.ForeignKey(to=Client,related_name='subscriptions',on_delete=models.PROTECT)
    service = models.ForeignKey(to=Service,related_name='subscriptions',on_delete=models.PROTECT)
    plan = models.ForeignKey(to=Plan,related_name='subscriptions',on_delete=models.PROTECT)
    price  = models.PositiveIntegerField(default=0)


