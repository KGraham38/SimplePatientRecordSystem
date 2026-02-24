#Main class for our Simple Patient Record System
from typing import Any


class PatientRegistry:
    def __init__(self):

        self.patient_registry = {}
        self.id_increment = 101


    #Generates a unique ID and stores the patient - REQ-1
    def register_patient(self,name: str) -> str:

        patient_id = "P-" + str( self.id_increment)

        self.patient_registry[id] = {"patient_id": id, "name": name}
        self.id_increment +=1

        return str(id)

    #Returns patient data or an error if not found - REQ-2
    def get_patient(self, patient_id:str) -> dict | None:

        if patient_id in self.patient_registry:
            return self.patient_registry[patient_id]

        return None

    #REQ 3 - NO CHANGING PATIENT ID

    #REQ-4
    def update_patient_name(self,patient_id:str, new_name: str) -> dict | None:

        if patient_id in self.patient_registry:
            self.patient_registry[patient_id]["name"] = new_name
            return self.patient_registry[patient_id]

        return None

    #REQ-5
    def delete_patient(self, patient_id:str) -> bool:
        if patient_id in self.patient_registry:
            self.patient_registry.pop(patient_id)
            return True

        return False

    def list_all_patients(self):
        return list(self.patient_registry.values())