from hospital_package.hospital import Hospital
from employee_package.employee import Employee, MedicalStaff, Doctor, Nurse, Custodian, Patient
from admin_package.admin import ADMIN
import os

#driver code

hospital = Hospital('Anti-Death Hospital','Kuala Lumpur')

doctor_jim = Doctor('UofT', 'Cancer', 'Jim', 'doctor_jim', 'asdf')

doctor_steve = Doctor('Waterloo', 'Emergency', 'Steve', 'doctor_steve', 'asdf')

nurse_melinda = Nurse('Cancer', 'Melinda', 'nurse_melinda', 'asdf')

nurse_josephine = Nurse('Emergency', 'Josephine', 'nurse_josephine', 'asdf')

custodian_maximus = Custodian('Maximus', 'custodian_maximus', 'asdf')

custodian_roger = Custodian('Roger', 'custodian_roger', 'asdf')

hospital.add_employee(doctor_jim)
hospital.add_employee(doctor_steve)
hospital.add_employee(nurse_melinda)
hospital.add_employee(nurse_josephine)
hospital.add_employee(custodian_maximus)
hospital.add_employee(custodian_roger)

#end of driver code

print('============================================')

print(f'Welcome to {hospital.name}, {hospital.location}')

print('============================================')


CURRENT_USER = None

while CURRENT_USER==None:
    print()
    username = input('Please enter username: ')
    password = input('Please enter password: ')
    
    if username in hospital.usernames and password in hospital.passwords:
        os.system('clear')
        CURRENT_USER = hospital.employees[username]
        print('============================================')
        print(f'Welcome {CURRENT_USER.name}. Your access level is {CURRENT_USER.__class__.__name__}.')
        print('============================================')
    elif username == 'ADMIN' and password == 'asdf':
        ADMIN = ADMIN()
        CURRENT_USER = ADMIN
        print('============================================')        
        print(f'Welcome {CURRENT_USER.name}. Your access level is {CURRENT_USER.__class__.__name__}.')
        print('============================================')        
    else:
        os.system('clear')
        print('try again fam')

def id():
    return CURRENT_USER.id

def name():
    return CURRENT_USER.name

if CURRENT_USER.__class__.__name__ == 'ADMIN':

    def new_doctor(medical_school, ward, name, username, password):
        return Doctor(medical_school, ward, name, username, password)

    def new_nurse(ward, name, username, password):
        return Nurse(ward, name, username, password)

    def new_custodian(name, username, password):
        return Custodian(name, username, password)

    def new_patient(id, ward):
        return Patient(id, ward)

    def add_employee(employee):
        hospital.add_employee(employee)

    def add_patient(patient):
        hospital.add_patient(patient)

print()
print('What you down for???')

breakpoint()