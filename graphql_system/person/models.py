from django.db import models
from .choices import State

class Address(models.Model):
    number = models.IntegerField()
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=16, choices=State.choices)

    def __str__(self):
        return f"{self.number} {self.street}, {self.city}, {self.state}"


class Person(models.Model):
    email = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ('name',)