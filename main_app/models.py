from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Treasure(models.Model):
        name = models.CharField(max_length=100)
        value = models.DecimalField(max_digits=10,
                                    decimal_places=2)
        material = models.CharField(max_length=100)
        location = models.CharField(max_length=100)

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