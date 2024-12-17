

## Overview

This is a RESTful API built with Django and Django REST Framework (DRF) for managing patient information, including family members, medications, and emergency contacts. The application provides functionality to create, update, retrieve, and delete records for patients and their related entities.

---

## Features

- **Patient Management**
  - Add, update, retrieve, and delete patient details.
  
- **Family Member Management**
  - Associate family members with patients.
  - CRUD operations for family members.
  
- **Medications**
  - Track patient medications, including dosage, timings, and active status.
  - View active medications for a patient.

- **Emergency Contacts**
  - Maintain a list of up to three emergency contacts for each patient.
  - Validate emergency contact limit during creation.

---

## Models

1. **Patient**
   - Fields: `name`, `DOB`, `gender`, `address`, `contact`.

2. **Family Member**
   - Fields: `name`, `gender`, `relation`, `contact`, `patient`.

3. **Medications**
   - Fields: `patient`, `medication_name`, `dosage`, `timings`, `active`.

4. **Emergency Contact**
   - Fields: `patient`, `family_member`, `name`, `relation`, `contact_number`.


---

## Installation

1. **Clone the Repository**
  
   git clone git@github.com:Shamitha-yangala/Healthcare_API_DRF.git
   cd /Healthcare_API_DRF
   

2. **Set up Virtual Environment**
  
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate     # For Windows
   

3. **Install Dependencies**
   
   pip install -r requirements.txt
 

4. **Run Migrations**
   
   python manage.py makemigrations
   python manage.py migrate


5. **Start the Development Server**
   
   python manage.py runserver
 

---



## Validation Rules

- A patient can have up to **3 emergency contacts**. Attempts to add more will raise a validation error.
- All `ForeignKey` relationships are validated during serialization to ensure data consistency.

---


