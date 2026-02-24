#Main class for our Simple Patient Record System
class PatientRegistry:
    def __init__(self):

        self.patient_registry = {}
        self.name = ""
        self.patient_id = ""
        self.new_name = ""
        self.running = True
        self.id_increment = 101
        self.all_patient_id = []

        #Entry point for all other functions is draw_main_menu()
        while self.running:
            self.draw_main_menu()

        SystemExit(0)

    #Generates a unique ID and stores the patient
    def register_patient(self,name: str) -> str:

        id = "P-" + str( self.id_increment)

        self.patient_registry[id] = {"patient_id": id, "name": name}
        self.id_increment +=1

        print("")
        print("#####################################")
        print(f"Patient {name} registration successful!")
        print("#####################################")
        print("")
        print("Returning to main menu")

        return str(id)

    #Returns patient data or an error if not found
    def get_patient(self, patient_id:str) -> dict:

        if patient_id in self.patient_registry:
            return self.patient_registry[patient_id]
        else:
            print("")
            print("#####################################")
            print("Patient does not exist")
            print("#####################################")
            print("")

        return None

    #All other functions below are pretty self-explanatory

    def update_patient_name(self,patient_id:str, new_name: str) -> dict:

        for patient in self.patient_registry.items():
            if patient_id in self.patient_registry:
                self.patient_registry[patient_id]["name"] = new_name
                print("")
                print("#####################################")
                print("Name Changed")
                print("#####################################")

            else:
                print("")
                print("#####################################")
                print("Patient does not exist")
                print("#####################################")
                print("")
        return self.patient_registry

    def delete_patient(self, patient_id:str) -> bool:
        for patient in self.patient_registry.items():
            if patient_id in self.patient_registry:
                print(f"Patient {self.patient_registry[patient_id]["name"]} about to be deleted")
                conformation = input("Continue, Y/N?: ")
                if conformation.lower() == "y":
                    print("")
                    print("#####################################")
                    print("Patient deleted")
                    print("#####################################")

                    self.patient_registry.pop(patient_id)
                    return True
                else:
                    print("#####################################")
                    print("Patient deletion cancelled!")
                    print("#####################################")
                    return False

            else:
                print("")
                print("#####################################")
                print("Patient does not exist")
                print("#####################################")
                print("")

        return False

    def list_all_patients(self):
        i=0
        if self.patient_registry == {}:
            print("")
            print("#####################################")
            print("Patient Registry is empty")
            print("#####################################")
            print("")

            return
        else:
            for patient, record in self.patient_registry.items():
                i+=1
                print("")
                print("#####################################")
                print("Patient #: " + str(i))
                print("Patient Info: " + str(record))
                print("#####################################")
                print("")