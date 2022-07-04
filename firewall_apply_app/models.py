from asyncio import protocols
from ipaddress import ip_address
from django.db import models
from django.utils import timezone

# Create your models here.
class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")

    def __str__(self) -> str:
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"

class User(models.Model):
    username = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    is_admin = models.BooleanField()

class FirewallApply(models.Model):
    status = models.IntegerField()
    apply_date = models.DateField()
    name = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    device_place_location = models.CharField(max_length=300)
    source_ip_address = models.GenericIPAddressField()
    destination_ip_address = models.GenericIPAddressField()
    open_direction = models.IntegerField()
    protocols = models.CharField(max_length=10)
    ports = models.CharField(max_length=300)
    reason = models.CharField(max_length=300)
    apply_during_begin = models.DateField()
    apply_during_end = models.DateField()
    declare = models.BooleanField()
