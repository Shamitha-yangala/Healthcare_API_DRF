from rest_framework import serializers
from .  models import Patient,Family_member,Medications,Emergency_contact

# family member serialization
class Family_memberSerializer(serializers.ModelSerializer):
        patient=serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())
        class Meta:
            model=Family_member
            fields=['id','name','relation','contact','patient_id','patient']
            


#  Medications Serializer    
class MedicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Medications
        fields='__all__'


# Emergency Contact Serializer
class EmergencyContactSerializer(serializers.ModelSerializer):
     class Meta:
          model=Emergency_contact
          fields=['patient','name','relation','contact_number']



# Patient Serializer
class PatientSerializer(serializers.ModelSerializer):
    # # Nested serializer for family members associated with the patient.
    family_members=Family_memberSerializer(many=True,read_only=True) 
  
    # Nested serializer for the medications associated with the patient.
    # It provides a way to include details of related medication objects.
    medications=MedicationsSerializer(many=True,read_only=True)

    # Nested serializer for emergency contacts of the patient.
    # This includes a list of emergency contact details using the EmergencyContactSerializer.
    emergency_contact=EmergencyContactSerializer(many=True,read_only=True)

    class Meta:
        model=Patient
        fields=['id','name','DOB','gender','address','contact','family_members','medications','emergency_contact']