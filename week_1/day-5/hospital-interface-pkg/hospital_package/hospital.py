class Hospital():
    wards = {'Emergency', 'Psychiatric', 'Cancer', 'Cardiological'}
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.employees = {}
        self.usernames = []
        self.passwords = []
        self.patients = {}

    def add_employee(self, employee):
        self.employees[employee.username] = employee
        self.usernames.append(employee.username)
        self.passwords.append(employee.password)

    def add_patient(self, patient):
        self.patients[patient.patient_id] = patient

    
    #show wards
    #show patients in ward
    #show employees in ward

    #add employee by child class into a ward
    #show employees
    #show employee child classes (Doc, Nurse, Recep, Custodian)
    #show employee by ward 

    #add patient into a ward
    #show patients
    #show patient by ward


    
