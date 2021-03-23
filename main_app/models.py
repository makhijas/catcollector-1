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

# tuples (value1, value2, value3) immutable. pop() doesn't work
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Feeding(models.Model):
    date = models.DateField()
    meal = models.CharField(
        max_length = 1,
        #possible choices are the MEALS
        choices = MEALS,
        default = MEALS[0][0]
    )

    #what happens if we delete the parent node, in this case a specific cat
    #association to Cat Model, when cat is deleted, delete associated feedings
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE )
    
    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"