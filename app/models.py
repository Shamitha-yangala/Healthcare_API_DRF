from django.db import models
from rest_framework.validators import ValidationError

gender_choices=[('M', 'Male'),('F', 'Female'),('O','Others')]

# patient  model
class Patient(models.Model):
    name=models.CharField(max_length=225)
    DOB=models.DateField()
    gender=models.CharField(max_length=20,choices=gender_choices)
    address=models.TextField()
    contact=models.CharField(max_length=12)
    

   

    def __str__(self):
        return self.name


relation_choices=[('Father','father'),
                  ('Mother','mother'),
                  ('Sister','sister'),
                  ('Brother','brother'),
                  ('Spouse','spouse'),
                  ('Child','child'),
                  ('Friend','friend'),
                  ('Guardian','guardian')]

# family member model
class Family_member(models.Model):
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=20,choices=gender_choices)
    relation=models.CharField(max_length=20,choices=relation_choices)
    patient=models.ForeignKey(Patient,related_name="family_members",on_delete=models.CASCADE)
    contact=models.CharField(max_length=12)



    def __str__(self):
        return f'{self.relation}---{self.relation}'
    
#  patient medications model
class Medications(models.Model):

    patient=models.ForeignKey(Patient,related_name="medications",on_delete=models.CASCADE)
    medication_name=models.CharField(max_length=100)
    dosage=models.CharField(max_length=100)
    timings=models.TextField(max_length=200)
    active=models.BooleanField(default=False,null=True)#status
    
    def __str__(self):
        return f'{self.medication_name} ({self.status})'

# patient Emergency contact information
class Emergency_contact(models.Model):
    patient=models.ForeignKey(Patient,related_name="emergency_contact",on_delete=models.CASCADE)
    family_member=models.ForeignKey(Family_member,related_name="emergency_contact_family",null=True,blank=True,on_delete=models.SET_NULL)
    name=models.CharField(max_length=100)
    contact_number=models.CharField(max_length=12)
    relation=models.CharField(max_length=20,choices=relation_choices)

    def save(self,*args,**kwargs):
        if not self.pk:
            emergency_contact_list=Emergency_contact.objects.filter(patient=self.patient)
            if emergency_contact_list.count() >=3:
                raise ValidationError("Patient can have maximum 3 emergency contacts")
        super().save(*args,**kwargs)
    
    def __str__(self):
        if self.family_member:
            return f'{self.family_member.relation}---{self.name}'
        return f'{self.name}'