#Kody Graham
#02/24/2026
#Simple Patient Record System
#Class for our Simple Patient Record System that will handle all access to registry

class PatientRegistry:
    def __init__(self):

        self.patient_registry = {}
        self.id_increment = 101

    # REQ-01
    #Generates a unique ID and stores the patient
    def register_patient(self,name: str) -> str:

        patient_id = "P-" + str( self.id_increment)

        self.patient_registry[patient_id] = {"patient_id": patient_id, "name": name}
        self.id_increment +=1

        return patient_id

    # REQ-02
    #Returns patient data or an error if not found
    #Moddified to return None, this is just to further enforce our access to patient registry only happening in this class file
    def get_patient(self, patient_id:str) -> dict | None:

        if patient_id in self.patient_registry:
            return self.patient_registry[patient_id]

        return None

    # REQ-03
    #NO PATIENT ID CHANGE ALLOWED

    # REQ-04
    #Modified again just to also allow a return of None to keep my patient exist check within this class
    def update_patient_name(self,patient_id:str, new_name: str) -> dict | None:

        if patient_id in self.patient_registry:
            self.patient_registry[patient_id]["name"] = new_name
            return self.patient_registry[patient_id]

        return None

    # REQ-05
    def delete_patient(self, patient_id:str) -> bool:
        if patient_id in self.patient_registry:
            self.patient_registry.pop(patient_id)
            return True

        return False

    #Again modified to also allow a return of None just to keep all access to our registry within this class
    def list_all_patients(self) -> list[dict] | None:

        patients = list(self.patient_registry.values())
        if len(patients) == 0:
            return None
        return patients

    #Extra helpers to keep access of our registry contained in this class will go here

    #Just to prevent main from having to access our patient registry
    def get_patient_name(self, patient_id:str) -> str | None:
        record = self.get_patient(patient_id)
        if record is None:
            return None
        return record["name"]