from django.contrib import admin

from .models import *

admin.site.register(Address)
admin.site.register(Party)
admin.site.register(Property)
admin.site.register(InspectionEvent)
