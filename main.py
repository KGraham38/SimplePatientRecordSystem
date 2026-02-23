#Kody Graham
#02/22/2026
#Simple Patient Record System


class PatientRegistry:
    def __init__(self):
        self.patient_registry = {}
        self.name = ""
        self.patient_id = ""
        self.new_name = ""
        self.running = True
        self.id_increment = 101
        self.all_patient_id = []

        while self.running:
            self.draw_main_menu()

        SystemExit(0)

    #Generates a unique ID and stores the patient
    def register_patient(self,name: str) -> str:

        id = "P-" + str( self.id_increment)

        self.patient_registry[id] = {"patient_id": id, "name": name}
        self.id_increment +=1

        return str(id)

    #Returns patient data or an error if not found
    def get_patient(self, patient_id:str) -> dict:

        if patient_id in self.patient_registry:
            return self.patient_registry[patient_id]
        else:
            print("")
            print("Patient does not exist")
            print("")

        return self.patient_registry

    def update_patient_name(self,patient_id:str, new_name: str) -> dict:

        for patient in self.patient_registry.items():
            if patient_id in self.patient_registry:
                self.patient_registry[patient_id]["name"] = new_name
                print("")
                print("Name Changed")
            else:
                print("")
                print("Patient does not exist")
                print("")
        return self.patient_registry

    def delete_patient(self, patient_id:str) -> bool:
        for patient in self.patient_registry.items():
            if patient_id in self.patient_registry:
                print("Patient about to be deleted")
                conformation = input("Continue, Y/N?: ")
                if conformation.lower() == "y":
                    print("")
                    print("Patient deleted")
                    self.patient_registry.pop(patient_id)
                    return True
                else:
                    print("Patient deletion cancelled!")
                    return False

            else:
                print("")
                print("Patient does not exist")
                print("")

        return False

    def list_all_patients(self):
        i=0
        if self.patient_registry == {}:
            print("")
            print("Patient Registry is empty")
            print("")

            return
        else:
            for patient, record in self.patient_registry.items():
                i+=1
                print("")
                print("Patient #: " + str(i))
                print("Patient Info: " + str(record))
                print("")

    def draw_app_menu(self):
        print("1. Register a new patient")
        print("2. Retrieve patient ID")
        print("3. Update patient name (ID change NOT permitted)")
        print("4. Delete patient ID")
        print("5. List all patients")
        print("6. Go back to main menu")
        print("7. Exit")

        choice = input("Enter your choice: ")
        choices = ["1", "2", "3", "4", "5", "6", "7"]

        #Not a fan or if else chains but for simplicity will use on here
        if choice == "1":
            self.name = input("Enter new patient's name: ")
            self.register_patient(self.name)

        elif choice == "2":
            self.get_patient(self.patient_id)

        elif choice == "3":
            print("")
            self.patient_id= input("Enter patient ID to update patient name (Starts with 'P-'): ")
            self.new_name= input("Enter patient's updated name: ")
            self.update_patient_name(self.patient_id, self.new_name)

        elif choice == "4":
            print("")
            self.patient_id= input("Enter patient ID to delete patient record (Starts with 'P-'): ")

            self.delete_patient(self.patient_id)

        elif choice == "5":
            self.list_all_patients()

        elif choice == "6":
            self.draw_main_menu()

        elif choice == "7":
                self.running = False

        elif choice not in choices:
            print("")
            print("Please enter a valid choice: Single digit from 1 to 7")
            print("")
            self.draw_app_menu()

    def draw_main_menu(self):

        #Simple menu to start may use pygame to generate a true UI menu
        print("")
        print("Welcome to the Patient Registry!")
        print("")
        print("1. Run Application")
        print("2. Exit")
        print("")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("")
            print("Application Running...")
            print("")
            self.draw_app_menu()

        elif choice == "2":
            print("")
            print("")
            print("")
            print("Thank you for using our Simple Patient Record System!")
            print("Goodbye!")
            self.running = False

        elif choice != "1" and choice != "2":
            print("")
            print("Please enter a valid choice: 1 or 2")
            print("")

        return

if __name__ == "__main__":
    app = PatientRegistry()