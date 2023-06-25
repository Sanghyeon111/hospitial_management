"""
Name: HuiEn Lin
Date: 2023/04/18
"""

"""
Description: 
Get and set doctor properties
Inputs:
id,name,specialization,workingTime,qualification and roomNumber
"""
class Doctor:
    def __init__(self,**features):
        self.id = features.pop('id')
        self.name = features.pop('name')
        self.specialization = features.pop('specialization')
        self.workingTime = features.pop('workingTime')
        self.qualification = features.pop('qualification')
        self.roomNumber = features.pop('roomNumber')

    # get methods
    def get_doctor_id(self):
        return self.id
    
    def get_doctor_name(self):
        return self.name
    
    def get_doctor_specialization(self):
        return self.specialization
    
    def get_doctor_workingTime(self):
        return self.workingTime
    
    def get_doctor_qualification(self):
        return self.qualification
    
    def get_doctor_roomNumber(self):
        return self.roomNumber
    
    def set_doctor_id(self,new_id):
        self.id = new_id

    #set methods
    def set_doctor_name(self,new_name):
        self.name = new_name

    def set_doctor_specialization(self,new_specialization):
        self.specialization = new_specialization

    def set_doctor_workingTime(self,new_workingTime):
        self.workingTime = new_workingTime

    def set_doctor_qualification(self,new_qualification):
        self.qualification = new_qualification

    def set_doctor_roomNumber(self,new_roomNumber):
        self.roomNumber = new_roomNumber
    
    # Get doctor string, the format is that all doctor properties separates by underscore
    def __str__(self):
        return f"{self.get_doctor_id()}_{self.get_doctor_name()}_{self.get_doctor_specialization()}_{self.get_doctor_workingTime()}_{self.get_doctor_qualification()}_{self.get_doctor_roomNumber()}"

"""
Description: 
Manage, display and search doctor information.
"""
class DoctorManager:
    doctorFilePath = "Project Data/doctors.txt"

    # Create doctors Information list and get doctor data from file to the list.
    def __init__(self):
        self.doctorInformations = []
        self.read_doctors_file()

    # get doctors information from file then put data to list.
    def read_doctors_file(self):
        file = open(DoctorManager.doctorFilePath)
        self.doctorInformations = []
        for line in file:
            info = line.replace("\n","").split("_")
            doctor = Doctor(id = info[0],name = info[1],specialization=info[2],workingTime=info[3],qualification=info[4],roomNumber=info[5])
            self.doctorInformations.append(doctor)
        file.close()
        self.doctorInformations.pop(0)

    # format doctor object information to the format used in doctor file.
    # input: doctor object
    def format_dr_info(self,dc):
        return dc.__str__()
    
    # Ask user to enter doctor properties
    # inputs : id, name, specility, working time, qualification, room number
    # output : doctor object
    def enter_dr_info(self):
        properties = {"ID": "","name": "","specility": "","timing (e.g., 7am-10pm)": "","qualification": "","room number": ""}
        for property in properties.keys():
            value = input(f"Enter the doctor's {property}: ")
            properties[property] = value
        doctor = Doctor(id=properties["ID"],name=properties["name"],specialization=properties["specility"],workingTime=properties["timing (e.g., 7am-10pm)"],qualification=properties["qualification"],roomNumber=properties["room number"])
        return doctor
    
    # Search doctor by id
    # input: id
    # output: display doctor information
    def search_doctor_by_id(self):
        Id = input("Enter the doctor Id: ")
        for doctor in self.doctorInformations:
            if(doctor.id == Id):
                self.display_doctor_info(doctor)
                return
        print("Can't find the doctor with the same ID on the system")
    
    # Search doctor by name
    # input: name
    # output: display doctor information
    def search_doctor_by_name(self):
        name = input("Enter the doctor name: ")
        for doctor in self.doctorInformations:
            if(doctor.name == name):
                self.display_doctor_info(doctor)
                return
        print("Can't find the doctor with the same name on the system")
        
    # display doctor info
    # input: doctor object
    # output: display doctor information
    def display_doctor_info(self,doctor):
            doctor: Doctor
            print(f"{'Id':<8} {'Name':<15} {'Speciality':<10} {'Timing':<10} {'Qualification':<15} {'Room Number':<15}\n")
            print(f"{doctor.get_doctor_id():<8} {doctor.get_doctor_name():<15} {doctor.get_doctor_specialization():<10} {doctor.get_doctor_workingTime():<10} {doctor.get_doctor_qualification():<15} {doctor.get_doctor_roomNumber():<15}")
    
    # edit doctor properties
    # input: id
    # output:
    # 1. if cannot find the doctor by the name: Can't find the doctor with the same ID on the system
    # 2. if complete edit and save the info to file: Doctor whose ID is doctor_id has been edited
    def edit_doctor_info(self):
        id = input("Please enter the id of the doctor that you want to edit their information: ")
        dc = None
        for doctor in self.doctorInformations:
            if(doctor.id == id):
                dc = doctor
                break
        if dc == None:
            print("Can't find the doctor with the same ID on the system")
        else:
            dc:Doctor
            properties = {"Name": "","Specilist in": "","Timing": "","Qualification": "","Room number": ""}
            for property in properties.keys():
                value = input(f"Enter new {property}: ")
                properties[property] = value
            dc.set_doctor_name(properties["Name"])
            dc.set_doctor_specialization(properties["Specilist in"]) 
            dc.set_doctor_workingTime(properties["Timing"])
            dc.set_doctor_qualification(properties["Qualification"])
            dc.set_doctor_roomNumber(properties["Room number"])
            self.Write_list_of_doctors_to_file()
            print()
            print(f"Doctor whose ID is {dc.get_doctor_id()} has been edited")
            
    # display doctor info by form style.
    def display_doctors_list(self):
        print(f"{'Id':<8} {'Name':<15} {'Speciality':<10} {'Timing':<10} {'Qualification':<15} {'Room Number':<15}\n")
        for dc in self.doctorInformations:
            print(f"{dc.id:<8} {dc.name:<15} {dc.specialization:<10} {dc.workingTime:<10} {dc.qualification:<15} {dc.roomNumber:<15}")
            if(dc != self.doctorInformations[-1]):
                print()

    # write doctor list to file
    def Write_list_of_doctors_to_file(self):
        informations = list()
        informations.append("id_name_specilist_timing_qualification_roomNb\n")
        for dc in self.doctorInformations:
           informations.append(self.format_dr_info(dc) + "\n")
        f = open(DoctorManager.doctorFilePath, 'w')
        for newInfo in informations:
            f.write(newInfo)
        f.close()

    # add new doctor to file
    # input: new doctor properties
    # output: Doctor whose ID is doctor_id has been added
    def add_dr_to_file(self):
        newdc= self.enter_dr_info() 
        self.doctorInformations.append(newdc)
        self.Write_list_of_doctors_to_file()
        print()
        print(f"Doctor whose ID is {newdc.get_doctor_id()} has been added")