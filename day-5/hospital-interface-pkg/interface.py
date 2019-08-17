from hospital_package.hospital import Hospital
from employee_package.employee import Employee, MedicalStaff, Doctor, Nurse, Custodian, Patient, PatientRecord
from admin_package.admin import ADMIN
import os

#driver code

hospital = Hospital('Anti-Death Hospital','Kuala Lumpur')

ADMIN = ADMIN()

doctor_jim = Doctor('UofT', 'Cancer', 'Jim', 'doctor_jim', 'asdf')

doctor_steve = Doctor('Waterloo', 'Emergency', 'Steve', 'doctor_steve', 'asdf')

nurse_melinda = Nurse('Cancer', 'Melinda', 'nurse_melinda', 'asdf')

nurse_josephine = Nurse('Emergency', 'Josephine', 'nurse_josephine', 'asdf')

custodian_maximus = Custodian('Maximus', 'custodian_maximus', 'asdf')

custodian_roger = Custodian('Roger', 'custodian_roger', 'asdf')

patient_1 = Patient('Cancer')

patient_2 = Patient('Psychiatric')

hospital.add_employee(ADMIN)

hospital.add_employee(doctor_jim)
hospital.add_employee(doctor_steve)
hospital.add_employee(nurse_melinda)
hospital.add_employee(nurse_josephine)
hospital.add_employee(custodian_maximus)
hospital.add_employee(custodian_roger)
hospital.add_patient(patient_1)
hospital.add_patient(patient_2)

#end of driver code

print('============================================')

print(f'Welcome to {hospital.name}, {hospital.location}')

print('============================================')


CURRENT_USER = None

def log_in():
    global CURRENT_USER
    # global ADMIN()

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
        # elif username == 'ADMIN' and password == 'asdf':
        #     os.system('clear')
        #     ADMIN = ADMIN()
        #     CURRENT_USER = ADMIN
        #     print('============================================')        
        #     print(f'Welcome {CURRENT_USER.name}. Your access level is {CURRENT_USER.__class__.__name__}.')
        #     print('============================================')        
        else:
            os.system('clear')
            print('try again fam')

log_in()

print()
print('Available Options:')
print()

def id():
    return CURRENT_USER.id

def name():
    return CURRENT_USER.name

def exit():
    global CURRENT_USER
    CURRENT_USER = None
    log_in()

print('id()')
print('name()')

if CURRENT_USER.__class__.__name__ == 'ADMIN':

    print('new_doctor()')
    print('new_nurse()')
    print('new_custodian')
    print('new_patient')
    print('list_employees')

    def new_doctor():
        print('Initiating new Doctor protocol')
        medical_school = input('Enter Medical School: ')
        while True:
            ward = input('Enter ward (Emergency, Cancer, Psychiatric, Cardiological): ')
            if ward in hospital.wards:
                break
            else:
                print(f'{ward} is not a valid ward. Please try again.')
        name = input('Enter full name: ')
        username = input('Enter system username: ')
        password = input('Enter password: ')
        doc = Doctor(medical_school, ward, name, username, password)
        add_employee(doc)
        print(f'Doctor {doc.name} has been added to the employee database!')

    def new_nurse():
        print('Initiating new Nurse protocol')
        while True:
            ward = input('Enter ward (Emergency, Cancer, Psychiatric, Cardiological): ')
            if ward in hospital.wards:
                break
            else:
                print(f'{ward} is not a valid ward. Please try again.')
        name = input('Enter full name: ')
        username = input('Enter system username: ')
        password = input('Enter password: ')
        nurse = Nurse(ward, name, username, password)
        add_employee(nurse)
        print(f'Nurse {nurse.name} has been added to the employee database!')

    def new_custodian():
        print('Initiating new Custodian protocol')
        name = input('Enter full name: ')
        username = input('Enter system username: ')
        password = input('Enter password: ')
        custodian = Custodian(name, username, password)
        add_employee(custodian)
        print(f'Custodian {custodian.name} has been added to the employee database!')

    def new_patient():
        print('Initiating new Patient protocol')
        while True:
            ward = input('Enter ward (Emergency, Cancer, Psychiatric, Cardiological): ')
            if ward in hospital.wards:
                break
            else:
                print(f'{ward} is not a valid ward. Please try again.')
        patient = Patient(ward)
        add_patient(patient)
        print(f'Patient #{patient.patient_id} has been added to the database!')

    def add_employee(employee):
        hospital.add_employee(employee)

    def add_patient(patient):
        hospital.add_patient(patient)

    def list_employees():
        print()
        for e in hospital.employees:
            print(f'{hospital.employees[e].name} - access level: {hospital.employees[e].__class__.__name__}')


if (CURRENT_USER.__class__.__name__ == 'Doctor' or
 CURRENT_USER.__class__.__name__ == 'ADMIN' or 
 CURRENT_USER.__class__.__name__ == 'Nurse'):

    print('add_patient_record()')
    print('list_patients()')
    print('list_records()')
    print('exit()')


    def add_patient_record():
        print('Initiating add paatient record protocol.')
        print('See existing patient database')
        list_patients()
        patient_id = input('Enter patient id: ')
        patient_id = int(patient_id)
        record_description = input('Enter record description: ')
        new_patient_record = PatientRecord(record_description)
        hospital.patients[patient_id].records[new_patient_record.record_id] = new_patient_record
        print(f'New record added for patient #{patient_id}.')

    def list_patients():
        print()
        for p in hospital.patients:
            print(f' Patient #{hospital.patients[p].patient_id} - ward: {hospital.patients[p].ward}')

    def list_records():
        list_patients()
        patient_id = input('Enter patient id: ')
        for r in hospital.patients[patient_id].records:
            print(f'Record #{hospital.patients[patient_id].records[r].record_id} - {hospital.patients[patient_id].records[r].record_description}')


breakpoint()