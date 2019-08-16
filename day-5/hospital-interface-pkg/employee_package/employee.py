class Employee():
    idnum = 0
    def __init__(self,name, username, password):
        Employee.idnum += 1
        z = Employee.idnum
        self.id = z
        self.name = name
        self.username = username
        self.password = password

class MedicalStaff(Employee):
    def __init__(self, ward, name, username, password):
        Employee.__init__(self, name, username, password)
        self.ward = ward
        #view patient records

class Doctor(MedicalStaff):
    def __init__(self, medical_school, ward, name, username, password):
        MedicalStaff.__init__(self, ward, name, username, password)
        self.medical_school = medical_school
        #add patient records
        #remove patient reords

class Nurse(MedicalStaff):
    def __init__(self, ward, name, username, password):
        MedicalStaff.__init__(self, ward, name, username, password)

class Custodian(Employee):
    def __init__(self, name, username, password):
        Employee.__init__(self, name, username, password)

class Patient():
    def __init__(self, id, ward):
        self.id = id
        self.ward = ward
        self.records = []