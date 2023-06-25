#import classes
from Doctor import DoctorManager
from patient import PatientManager
#define class
class Management:
    def display_menu(self):
        #loop continues until user selects option 3.
        while True:
            print("Welcome to Alberta Hospital (AH) Managment system")
            option = input("Select from the following options, or select 3 to stop:\n" + 
                "1 - 	Doctors\n"+
                "2 - 	Patients\n"+
                "3 - 	Exit Program \n"+
                ">>> ")
            if option == "0":
                break
            #If the user selects option 1, the DoctorManager class is created.  
            elif option == "1":
                dcm = DoctorManager()
                while True:
                    #Another loop starts giving user different options and continues untill user enters 6.
                    doctorOption = input("\nDoctors Menu:\n" + 
                    "1 - Display Doctors list\n"+
                    "2 - Search for doctor by ID\n"+
                    "3 - Search for doctor by name\n"+
                    "4 - Add doctor\n" + 
                    "5 - Edit doctor info\n" +
                    "6 - Back to the Main Menu\n"+
                    ">>> ")
                    print()
                    if doctorOption == "1":
                        dcm.display_doctors_list()
                    if doctorOption == "2":
                        dcm.search_doctor_by_id()
                    if doctorOption == "3":
                        dcm.search_doctor_by_name()
                    if doctorOption == "4":
                        dcm.add_dr_to_file()
                    if doctorOption == "5":
                        dcm.edit_doctor_info()
                    if doctorOption == "6":
                        break
            #If the user selects option 2, the PatientManager class is created.
            elif option == "2":
                pam = PatientManager()
                while True:
                    #Another loop starts giving user different options and continues untill user enters 5.
                    patOption = input("\nPatients Menu:\n" +
                        "1 - Display patients list\n" +
                        "2 - Search for patient by ID\n" + 
                        "3 - Add patient\n" + 
                        "4 - Edit patient info\n" + 
                        "5 - Back to the Main Menu\n" +
                        ">>> ")
                    print()
                    if patOption == "1":
                        pam.display_patients_list()
                    elif patOption == "2":
                        pam.search_patient_by_id()
                    elif patOption == "3":
                        pam.add_pa_to_file()
                    elif patOption == "4":
                        pam.edit_patient_info()
                    elif patOption == "5":
                        break
            #If the user selects option 3, the program exits.
            elif option == "3":
                #Program ends printing the end message.
                print("Thanks for using the program. Bye!")
                break
mag = Management()
mag.display_menu()
