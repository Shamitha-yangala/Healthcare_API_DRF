from django.contrib import admin
from . models import Patient,Family_member,Medications,Emergency_contact


admin.site.register(Patient)
admin.site.register(Family_member)
admin.site.register(Medications)
admin.site.register(Emergency_contact)