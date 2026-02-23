#Kody Graham
#02/22/2026
#Simple Patient Record System


class PatientRegistry:
    def __init__(self):
        self.patient_registry = {}
        self.name = ""
        self.patient_id = 0
        self.new_name = ""



    #Generates a unique ID and stores the patient
    def register_patient(self,name: str) -> str:


        return

    #Returns patient data or an error if not found
    def get_patient(self, patient_id:str) -> dict:
        return

    def update_patient_name(self,patient_id:str, new_name: str) -> dict:

        return

    def delete_patient(self, patient_id:str) -> bool:
        return

    def draw_menu(self):
        return