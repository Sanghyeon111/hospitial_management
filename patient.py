"""
Name: Sanghyeon Lee
Date: 2023/04/23
"""

# Patient class
class Patient:
    def __init__(self, **kwargs):
        self.patient_id = kwargs.get('patient_id')
        self.name = kwargs.get('name')
        self.disease = kwargs.get('disease')
        self.gender = kwargs.get('gender')
        self.age = kwargs.get('age')

    # getters get patient properties
    def get_patient_id(self):
        return self.patient_id
    def get_name(self):
        return self.name
    def get_disease(self):
        return self.disease
    def get_gender(self):
        return self.gender
    def get_age(self):
        return self.age

    # setters change patient's information
    def set_patient_id(self, new_patient_id):
        self.patient_id = new_patient_id
    def set_name(self,new_name):
        self.name = new_name
    def set_disease(self,new_disease):
        self.disease = new_disease
    def set_gender(self,new_gender):
        self.gender = new_gender
    def set_age(self,new_age):
        self.age = new_age

    def __str__(self):
        return (f"{self.get_patient_id()}_{self.get_name()}_{self.get_disease()}_{self.get_gender()}_{self.get_age()}")

# PatientManager Class
class PatientManager:
    path_patients_file = "Project Data/patients.txt"
    def __init__(self):
        self.patient_list = []
        self.read_patients_file()

    # read path_patients_file and create ptient object to store list.
    # return list which includes patient data
    def read_patients_file(self):
        with open(PatientManager.path_patients_file,'r') as f:
           for line in f.readlines()[1:]:
                line = line.strip("\n").split("_")
                patient = Patient(patient_id=line[0],name=line[1],disease=line[2],gender=line[3],age=line[4])
                self.patient_list.append(patient)

    # receive patient object and format its properties
    def format_pa_info(self,patient_object):
        return (f"{patient_object.get_patient_id()}_{patient_object.get_name()}_{patient_object.get_disease()}_{patient_object.get_gender()}_{patient_object.get_age()}")
    
    # receive patient properties and create new patient object with inputted properties
    def enter_pa_info(self):
        id = input("Enter patient id: ")
        name = input("Enter name: ")
        disease = input("Enter disease: ")
        gender = input("Enter patient gender: ")
        age = input("Enter patient age: ")
        patient_object = Patient(patient_id=id, name=name, disease=disease, gender=gender, age=age)
        return patient_object

    # receive ID that user want to find and find if entered id matched in patient_list using for loop.
    # if there is matched id, display according patient object by calling display_patient_info method, otherwise, return "Can’t find the patient…." message
    def search_patient_by_id(self):
        ID = input("Enter patient ID: ")
        for patient in self.patient_list:
            if patient.patient_id == ID:
                self.display_patient_info(patient)
                return
        print("Can’t find the Patient with the same id on the system\n")

    # receive name that user want to look and find if entered name matched in patient_list using for loop.
    # if there is matched name, display according patient object by calling display_patient_info method, otherwise, return "Can’t find the patient…." message
    def search_patient_by_name(self):
        NAME = input("Enter patient name: ")
        for patient in self.patient_list:
            if patient.name == NAME:
                self.display_patient_info(patient)
                return
        print("Can’t find the Patient with the same name on the system\n")

    # recieve patient object and display its properites
    def display_patient_info(self, patient_object):
        print("{:6s} {:16s} {:16s} {:20s} {:18s}\n".format("ID", "Name", "Disease", "Gender", "Age"))
        print("{:6s} {:16s} {:16s} {:20s} {:18s}".format(patient_object.get_patient_id(),patient_object.get_name(),patient_object.get_disease(),patient_object.get_gender(),patient_object.get_age()))

    # prompt user to enter id. If there is same id in patient list, prompt user to enter new properties and update new properties using setters.
    def edit_patient_info(self):
        edit_id = input("Please enter the id of the patient that you want to edit their information: ")
        for patient in self.patient_list:
            if patient.patient_id == edit_id:
                name = input("Enter new Name: ")
                disease = input("Enter new disease: ")
                gender = input("Enter new gender: ")
                age = input("Enter new age: ")
                patient.set_name(name)
                patient.set_disease(disease)
                patient.set_gender(gender)
                patient.set_age(age)
                self.Write_list_of_patients_to_file()
                print()
                print(f"Patient whose ID is {patient.get_patient_id()} has been edited.")
                return
        
        print(f"Can't find the Patient with the same id on the system")

    # display every objects with formatted form
    def display_patients_list(self):
        print("{:6s} {:16s} {:16s} {:20s} {:18s}\n".format("ID", "Name", "Disease", "Gender", "Age"))
        for patient_object in self.patient_list:
            print("{:6s} {:16s} {:16s} {:20s} {:18s}".format(patient_object.get_patient_id(),patient_object.get_name(),patient_object.get_disease(),patient_object.get_gender(),patient_object.get_age()))
            if(patient_object != self.patient_list[-1]):
                print()

    # write patient_list in formatted form calling format_pa_info method
    def Write_list_of_patients_to_file(self):
        with open(PatientManager.path_patients_file,'w') as f:
            f.write("id_Name_Disease_Gender_Age\n")
            for patient_object in self.patient_list:
                f.write(self.format_pa_info(patient_object))
                f.write("\n")

    # create patient object by calling enter_pa_info method. and append new object to patient list
    # append new patient in patient data
    def add_pa_to_file(self):
        new_patient = self.enter_pa_info()
        self.patient_list.append(new_patient)
        self.Write_list_of_patients_to_file()
        print()
        print(f"Patient whose ID is {new_patient.get_patient_id()} has been added")