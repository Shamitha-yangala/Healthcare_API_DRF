
from django.urls import path
from .views import *
urlpatterns = [
    
    
    
    # Creation of patient
    path('create_patient',create_patient.as_view(),name='create_patient'),
    # retrive the list of all patients
    path('patient_list/',patient_list.as_view(),name='patient_list'),

    # retrieve the details of a single patient
    path('patient_details/<int:pk>/',patient_details.as_view(),name='patient_details'),
    # update the details of a single patient
    path('update_patient/<int:pk>/',update_patient.as_view(),name="update_patient"),


    # add the family memeber to the patient
    path('Add_family_member/',Add_family_member.as_view(),name="Add_family_member"),
    # list of the  patient family members
    path('patient/<int:pk>/list_family_members/',patient_family_members.as_view(),name='patient_family_members_list'),
    # single family member details of the patient
    path('patient/<int:patient_pk>/member_details/<int:pk>/',patient_family_member_details.as_view(),name='patient_family_member_details'),
   

    # creation and list patient medications information  
    path('patient/<int:patient_id>/Medications/',patient_Medications.as_view(),name='medication_patient'),
    # updation of the ptients medication information
    path('patient/<int:patient_id>/update_medications/<int:pk>/',patient_update_medications.as_view(),name='update_medications'),
    # deletion of the patient  active medications information (status)
    path('patient_active_medications/<int:pk>/',patient_active_medications.as_view(),name='patient_active_medications'),


    # create and list of patient emergency contact information
    path('Emergency_contact/',emergency_contact.as_view(),name='Emergency_contact'),
    # retrieve the details of a single patient emergency contact
    path('patient/<int:pk>/emergency_contact',patient_emergency_contact.as_view(),name='patient_emergency_contact'),
    # update the details of a single patient emergency contact
    path('patient/<int:patinet_id>/update_emergency_contact/<int:pk>/',update_patent_emergency_contact.as_view(),name='update_patent_emergency_contact'),
]
