class Employee():
    def __init__(self,name, username, password, idnum):
        self.name = name
        self.username = username
        self.password = password
        self.idnum = idnum

class MedicalStaff(Employee):
    def __init__(self, ward, name, username, password, idnum):
        Employee.__init__(self, name, username, password, idnum)
        self.ward = ward

class Doctor(MedicalStaff):
    def __init__(self, medical_school, ward, name, username, password, idnum):
        MedicalStaff.__init__(self, ward, name, username, password, idnum)
        self.medical_school = medical_school

class Nurse(MedicalStaff):
    def __init__(self, ward, name, username, password, idnum):
        MedicalStaff.__init__(self, ward, name, username, password, idnum)

class Custodian(Employee):
    def __init__(self, name, username, password, idnum):
        Employee.__init__(self, name, username, password, idnum)