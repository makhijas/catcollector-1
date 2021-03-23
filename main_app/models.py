from django.db import models

# Create your models here.
class Cat(models.Model):
    age = models.IntegerField()
    breed = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# garfield = Cat('Garfield', 'Tabby', 'I have never heard of Tabby', 9)
# print(garfield)