from django.db import models

#Address Model
class Address(models.Model):
    name = models.CharField(max_length=50)
    line_1 = models.CharField(max_length=100)
    line_2 = models.CharField(max_length=100, null=True)
    line_3 = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    post_code = models.CharField(max_length=10, default='N/A')
    misc_info = models.CharField(max_length=200)
    geo_location = models.IntegerField

    def __str__(self):
        return self.name


#Party Model
class Party(models.Model):
    name = models.CharField(max_length=100)
    address_id = models.ForeignKey(Address, null=True)
    avatar = models.ImageField(upload_to = 'avatars/', null=True)
    status = models.CharField(max_length=10, default='Active')

    def __str__(self):
        return self.name


#Property Model
class Property(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    owner_id = models.ForeignKey(Party)
    
    def __str__(self):
        return self.name

class Event(models.Model):
    effective_date = models.DateField()
    description = models.CharField(max_length=200)
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE)


class InspectionEvent(Event):
    tax_paid = models.BooleanField()
    eb_paid = models.BooleanField()
    maintenance_paid = models.BooleanField()
    well_maintained = models.BooleanField()
    tenent_complaints = models.CharField(max_length=300)
    external_feedback = models.CharField(max_length=300)
    maint_required = models.CharField(max_length=300)
    maint_estimate = models.DecimalField(default=0, decimal_places=2, max_digits=9)

def property_path(property_id):
    return '{0}/%Y'.format(property_id)

class Artifact(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    artefact = models.ImageField(upload_to = property_path)