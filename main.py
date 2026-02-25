#Kody Graham
#02/22/2026
#Simple Patient Record System
#Class that will handle all of our menu logic and input validations


from PatientRegistry import PatientRegistry


class Main:
    def __init__(self):
        self.running = True
        self.registry = PatientRegistry()
        self.name = ""
        self.patient_id = ""
        self.new_name = ""
        self.running = True
        self.all_patient_id = []

        # Entry point for all other functions is draw_main_menu()
        while self.running:
            self.draw_main_menu()


        raise SystemExit(0)

    def draw_app_menu(self):
        app_menu_running = True
        while app_menu_running:
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
            print("")
            choices = ["1", "2", "3","4","5","6","7"]
            #Not a fan or if else chains but for simplicity will use one here if i add a real GUI i will use a click listener instead
            if choice == "1":
                self.name = input("Enter new patient's name: ").title()

                id_generated= self.registry.register_patient(self.name)

                print("")
                print("#####################################")
                print(f"Patient {self.name} registration successful assigned id is: {id_generated}")
                print("#####################################")
                print("")
                print("Returning to application menu")

            elif choice == "2":
                print("")
                self.patient_id = input("Enter patient ID to retrieve patient data (Starts with 'P-'): ")
                self.patient_id = self.patient_id.upper()

                patient_record= self.registry.get_patient(self.patient_id)

                if patient_record is not None:
                    print("")
                    print("#####################################")
                    print(f"Patient {self.patient_id}'s info: " + str(patient_record))
                    print("#####################################")
                    print("")
                else:
                    print("")
                    print("#####################################")
                    print("Patient does not exist")
                    print("#####################################")
                    print("")

                print("Returning to application menu")


            elif choice == "3":
                print("")
                self.patient_id= input("Enter patient ID to update patient name (Starts with 'P-'): ")
                self.patient_id = self.patient_id.upper()

                curr_name = self.registy.get_patient_name(self.patient_id)

                record = self.registry.get_patient(self.patient_id)
                if curr_name is not None:
                    curr_name = record["name"]
                print("")

                if curr_name is not None:
                    pick= input(f"Are you sure you want to change {curr_name}'s patient name? (Y/N): ")

                    pick = pick.upper()
                    if pick == "Y":
                        self.new_name= input("Enter patient's updated name: ")
                        self.new_name = self.new_name.title()
                        patient_exist = self.registry.update_patient_name(self.patient_id, self.new_name)

                        if patient_exist is not None:
                            print("")
                            print("#####################################")
                            print("Name Changed")
                            print("Updated Info: " + str(patient_exist))
                            print("#####################################")

                        else:
                            print("")
                            print("#####################################")
                            print("Patient does not exist")
                            print("#####################################")
                            print("")


                        print("")

                print("Returning to application menu")


            elif choice == "4":
                print("")
                self.patient_id= input("Enter patient ID to delete patient record (Starts with 'P-'): ")
                self.patient_id = self.patient_id.upper()

                p_name = self.registry.get_patient(self.patient_id)
                if p_name is not None:
                    print(f"Patient {p_name['name']} about to be deleted")
                    conformation = input("Continue, Y/N?: ")
                    if conformation.lower() == "y":
                        patient_exist = self.registry.delete_patient(self.patient_id)
                        print("")
                        print("#####################################")
                        print("Patient deleted")
                        print("#####################################")

                    else:
                        print("#####################################")
                        print("Patient deletion cancelled!")
                        print("#####################################")

                        print("")

                else:
                    print("")
                    print("#####################################")
                    print("Patient does not exist")
                    print("#####################################")
                    print("")

                print("Returning to application menu")


            elif choice == "5":

                all_patients = self.registry.list_all_patients()
                if all_patients is None:
                    print("")
                    print("#####################################")
                    print("Patient Registry is empty")
                    print("#####################################")
                    print("")

                else:
                    i = 0
                    for record in all_patients:
                        i += 1

                        print("")
                        print("#####################################")
                        print("Patient #: " + str(i))
                        print("Patient Info: " + str(record))
                        print("#####################################")
                        print("")

                print("")
                print("Returning to Application menu")


            elif choice == "6":
                print("")
                print("Returning to main menu")
                app_menu_running = False

            elif choice == "7":

                self.running = False

            else:
                print("")
                print("Please enter a valid choice: Single digit from 1 to 7")
                print("")


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
    app = Main()