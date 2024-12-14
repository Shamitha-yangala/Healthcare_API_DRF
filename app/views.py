from django.shortcuts import render
from django.http import HttpResponse

from . models import Patient,Family_member,Medications,Emergency_contact
from .serializers import (PatientSerializer,Family_memberSerializer,MedicationsSerializer,EmergencyContactSerializer)

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView,
                                     CreateAPIView,
                                     UpdateAPIView,
                                     ListCreateAPIView,
                                     RetrieveUpdateAPIView,
                                     DestroyAPIView,
                                     RetrieveUpdateDestroyAPIView)
def home(request):
    return HttpResponse("hello")

class create_patient(ListCreateAPIView):
    queryset=Patient.objects.all()
    serializer_class=PatientSerializer

class patient_list(ListAPIView):
    queryset=Patient.objects.all()
    serializer_class=PatientSerializer

class patient_details(RetrieveAPIView):
    queryset=Patient.objects.all()
    serializer_class=PatientSerializer

class update_patient(RetrieveUpdateDestroyAPIView):
    queryset=Patient.objects.all()
    serializer_class=PatientSerializer




class Add_family_member(ListCreateAPIView):
    queryset=Family_member.objects.all()
    serializer_class=Family_memberSerializer




# using list ap view
class patient_family_members(ListAPIView, RetrieveUpdateDestroyAPIView):

    serializer_class=Family_memberSerializer
    def get_queryset(self):
        patient=self.kwargs['pk']
        return Family_member.objects.filter(patient=patient)


# retriving the single member and perform the crud operations 
class patient_family_member_details(RetrieveUpdateDestroyAPIView):
    serializer_class=Family_memberSerializer
    lookup_field ='pk'

    def get_queryset(self):
        patient_id=self.kwargs['patient_pk']

      
        return Family_member.objects.filter(patient=patient_id)





class patient_Medications(ListCreateAPIView):
    
    serializer_class=MedicationsSerializer


    def get_queryset(self):
        patient_id=self.kwargs['patient_id']
        return Medications.objects.filter(patient=patient_id)
       


class patient_update_medications(RetrieveUpdateAPIView,DestroyAPIView):
   
    serializer_class=MedicationsSerializer
    lookup_field='pk'
    def get_queryset(self):
        patient=self.kwargs['patient_id']
        return Medications.objects.filter(patient=patient)





class patient_active_medications(ListAPIView):
    serializer_class=MedicationsSerializer

    def get_queryset(self):
       patient=self.kwargs['pk']
       return Medications.objects.filter(patient=patient,active=True)


class emergency_contact(ListCreateAPIView):
    queryset=Emergency_contact.objects.all()
    serializer_class=EmergencyContactSerializer


class patient_emergency_contact(ListAPIView):
    
    serializer_class=EmergencyContactSerializer


    def get_queryset(self):
       patient_id=self.kwargs['pk']
       return Emergency_contact.objects.filter(patient=patient_id)
    
class update_patent_emergency_contact(RetrieveUpdateDestroyAPIView):
    serializer_class=EmergencyContactSerializer
    lookup_field='pk'

    def get_queryset(self):
        patient=self.kwargs['patinet_id']
        return Emergency_contact.objects.filter(patient=patient)