#Kody Graham
#02/22/2026
#Simple Patient Record System


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

    def draw_app_menu(self):
        print("##############################################################")
        print("#                                                            #")
        print("# 1. Register a new patient                                  #")
        print("# 2. Retrieve patient ID                                     #")
        print("# 3. Update patient name (ID change NOT permitted)           #")
        print("# 4. Delete patient ID                                       #")
        print("# 5. List all patients                                       #")
        print("# 6. Go back to main menu                                    #")
        print("# 7. Exit                                                    #")
        print("#                                                            #")
        print("##############################################################")
        print("")


        choice = input("Enter your choice: ")
        choices = ["1", "2", "3", "4", "5", "6", "7"]
        print("")

        #Not a fan or if else chains but for simplicity will use on here if i add a real GUI i will use a click listener instead
        if choice == "1":
            self.name = input("Enter new patient's name: ")
            self.name = self.name.title()

            self.register_patient(self.name)

        elif choice == "2":
            print("")
            self.patient_id = input("Enter patient ID to retrieve patient data (Starts with 'P-'): ")
            self.patient_id = self.patient_id.title()

            patient= self.get_patient(self.patient_id)

            if patient is not None:
                print("")
                print("#####################################")
                print(f"Patient {self.patient_id}'s info: " + str(patient))
                print("#####################################")
                print("")
            print("Returning to main menu")


        elif choice == "3":
            print("")
            self.patient_id= input("Enter patient ID to update patient name (Starts with 'P-'): ")
            self.patient_id = self.patient_id.title()

            curr_name = None

            for patient in self.patient_registry.items():
                if self.patient_id in self.patient_registry:
                    curr_name = self.patient_registry[self.patient_id]["name"]

            print("")
            if curr_name is not None:
                pick= input(f"Are you sure you want to change {curr_name}'s patient name? (Y/N): ")

                pick = pick.upper()
                if pick == "Y":
                    self.new_name= input("Enter patient's updated name: ")
                    self.new_name = self.new_name.title()
                    self.update_patient_name(self.patient_id, self.new_name)
                    print("")
                    print("Returning to main menu")
                else:
                    print("Returning to main menu")

        elif choice == "4":
            print("")
            self.patient_id= input("Enter patient ID to delete patient record (Starts with 'P-'): ")
            self.patient_id = self.patient_id.title()
            self.delete_patient(self.patient_id)
            print("")
            print("Returning to main menu")

        elif choice == "5":
            self.list_all_patients()
            print("")
            print("Returning to main menu")

        elif choice == "6":
            self.draw_main_menu()

        elif choice == "7":
                self.running = False

        elif choice not in choices:
            print("")
            print("Please enter a valid choice: Single digit from 1 to 7")
            print("")
            self.draw_app_menu()

    #Simple menu to start may use pygame to generate a true UI menu later
    def draw_main_menu(self):

        print("")
        print("Welcome to the Patient Registry Main Menu!")
        print("")
        print("1. Run Application")
        print("2. Exit")
        print("")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("")
            print("#####################################")
            print("Application Running...")
            print("#####################################")
            print("")
            self.draw_app_menu()

        elif choice == "2":
            print("")
            print("")
            print("")
            print("#####################################")
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