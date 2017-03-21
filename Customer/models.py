from django.db import models

#Property Model
class Property(modesl.Model):
    id = models.Integer
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    address_id = models.Integer
    owner_id = models.Integer
    
