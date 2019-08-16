from hospital_package.hospital import Hospital
from employee_package.employee import Employee, MedicalStaff, Doctor, Nurse, Custodian
from admin_package.admin import add_employee, ADMIN

#driver code

hospital = Hospital('Anti-Death Hospital','Kuala Lumpur')

doctor_jim = Doctor('UofT', 'Cancer', 'Jim', 'doctor_jim', 'asdf', 420)

doctor_steve = Doctor('Waterloo', 'Emergency', 'Steve', 'doctor_steve', 'asdf', 455)

nurse_melinda = Nurse('Cancer', 'Melinda', 'nurse_melinda', 'asdf', 666)

nurse_josephine = Nurse('Emergency', 'Josephine', 'nurse_josephine', 'asdf', 969)

custodian_maximus = Custodian('Maximus', 'custodian_maximus', 'asdf', 128)

custodian_roger = Custodian('Roger', 'custodian_roger', 'asdf', 129)

add_employee(hospital, doctor_jim)
add_employee(hospital, doctor_steve)
add_employee(hospital, nurse_melinda)
add_employee(hospital, nurse_josephine)
add_employee(hospital, custodian_maximus)
add_employee(hospital, custodian_roger)

print('============================================')

print(f'Welcome to {hospital.name}, {hospital.location}')

print('============================================')

CURRENT_USER = None

while CURRENT_USER==None:
    username = input('Please enter username: ')
    password = input('Please enter password: ')
    
    if username in hospital.usernames and password in hospital.passwords:
        CURRENT_USER = username
        print('============================================')
        print(f'Welcome {CURRENT_USER.name}. Your access level is {}.')
        print('============================================')
    elif username == 'ADMIN' and password == 'asdf':
        ADMIN = ADMIN()
        CURRENT_USER = ADMIN
        print('============================================')        
        print('WELCOME GRAND OVERLORD')
        print('============================================')        
    else:
        print('try again fam')
print()
print('What you down for???')

breakpoint()