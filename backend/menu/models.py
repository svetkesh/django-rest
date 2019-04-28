from django.db import models

# Create your models here.
class Menu(models.Model):
    REGULAR = 'REG'
    VEGETARIAN = 'VEG'  # vegetarian
    SPECIAL = 'SO'   # chef special offer
    BABY = 'BABY'
    HOT = 'HOT'
    MEAL_CHOICES = (
        (REGULAR, 'Regular'),
        (VEGETARIAN, 'Vegetarian'),
        (SPECIAL, 'Special offer'),
        (BABY, 'Baby menu'),
        (HOT, 'Hot'),
        )

    type = models.CharField(
        max_length=4,
        choices=MEAL_CHOICES,
        default=REGULAR
    )
    title = models.CharField(max_length=100) # may be 200 check later
    description = models.TextField()
    weight = models.IntegerField(default=0)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)


    def __str__(self):
        """A string representation of the menu."""
        return f"{self.title} {self.type}"
