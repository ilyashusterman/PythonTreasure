from __future__ import unicode_literals
from django.utils.text import slugify
from django.db import models

# Create your models here.


class Treasure(models.Model):
        name = models.CharField(max_length=100)
        value = models.DecimalField(max_digits=10,
                                    decimal_places=2)
        material = models.CharField(max_length=100)
        location = models.CharField(max_length=100)
        slug = models.SlugField(max_length=100, blank=True)

        # *args takes the ordered list and  **kwargs takes the dictionary
        # self is the checked state
        def save(self, *args, **kwargs):
            if not self.pk:
                self.slug = slugify(self.name)
            super(Treasure, self).save(*args, **kwargs)

        def __str__(self):
            return self.name


# class Treasure:
#     def __init__(self, name, value, material, location):
#         self.name = name
#         self.value = value
#         self.material = material
#         self.location = location

# treasures = [
#     Treasure(name='Gold_Nugget', value=1000.00, material='gold', location='Tel-Aviv'),
#     Treasure(name='Gold_Box', value=2000.00, material='gold', location='Ashdod'),
#     Treasure(name='Silver_Bottle', value=400.00, material='silver', location='Herzelia')
# ]