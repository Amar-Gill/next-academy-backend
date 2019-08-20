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
    idnum = 0
    def __init__(self, ward):
        Patient.idnum += 1
        z = Patient.idnum
        self.patient_id = z
        self.ward = ward
        self.records = {}

class PatientRecord():
    idnum = 0
    def __init__(self, record_description):
        PatientRecord.idnum += 1
        z = PatientRecord.idnum
        self.record_id = z
        self.record_description = record_description