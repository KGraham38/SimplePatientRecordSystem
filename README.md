# ***Simple Patient Record System*** 

## Overview
 
 This Simple Patient Record System is a console based Python application that allows users to manage patient records using a menu driven system.

 All of the patient data access is handled in the PatientRegistry class, to maintain registry integrity. The main.py file is responsible only for the user interaction with the system through console input and output.

## Structure

***SimplePatientRecordSystem***
### |
### |--- main.py
### |--- patient_registry.py
### |--- test_patient_registry.py
### |--- README.md

## main.py
Handles:
- UI
- Menu Navigation
- Input validation (indirectly on patient registry data)
- Call my Patient Registry functions


## patient_registry.py
Handles:
- The patient ID generation
- Data storage
- Patient data retrieval
- Updating records
- Deleting patient records
- Listing all patients
  
### ALL patient dict access happens in this class

# Requirements
- REQ-1 - ***Register Patient*** 
- REQ-2 - ***Retrieve Patient Record*** 
- REQ-3 - ***Prevent ID Modification*** 
- REQ-4 - ***Update Patient Name*** 
- REQ-5 - ***Delete Patient Record*** 

## test_patient_registry.py
Handles:
- All of our unit tests
- All of our component tests

# Our Required Tests
- REQ-01 (Creation): Test that register_patient(name: str) successfully generates a unique ID (e.g., P-101) and stores the patient.
- REQ-02 (Retrieval): Test that get_patient(patient_id: str) retrieves the correct dictionary record.
- REQ-03 (Immutability): Test that the Patient ID cannot be modified once assigned.
- REQ-04 (Update): Test that update_patient_name changes the patient's name but keeps the ID unchanged.
- REQ-05 (Deletion): Test that delete_patient(patient_id: str) successfully removes the record.
  
# How to Run

- Make sure you have Python 3.10 or newer (might work with older versions but gurenteed at v3.10)
- Make sure you are in the project directory if not ***cd SimplePatientRecordSystem***
- run the **main.py** file either from your IDE or using ***python main.py***

# Example of Menu Layout

Welcome to the Patient Registry Main Menu!

1. Run Application
2. Exit

Enter your choice: 1

#####################################

Application Running...

#####################################

#

##############################################################

 1. Register a new patient                                  
 2. Retrieve patient ID                                     
 3. Update patient name (ID change NOT permitted)           
 4. Delete patient ID                                       
 5. List all patients                                       
 6. Go back to main menu                                    
 7. Exit
                                                                                                           
##############################################################

Enter your choice: 

# Contributions
## Developer & Tester
***Kody Graham***
## Software Designers
***Seth Wojcik***

***Daniyar Alimkhanov***
