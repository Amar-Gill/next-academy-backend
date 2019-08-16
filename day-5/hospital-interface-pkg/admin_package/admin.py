def add_employee(hospital, employee):
    hospital.employees.add(employee)
    hospital.usernames.append(employee.username)
    hospital.passwords.append(employee.password)

class ADMIN():#inherit from med staff???

    username = 'ADMIN'
    password = 'asdf'
    name = 'Eren Jaeger'
    id = 'HYPER SMASH'

    def add_employee(self,hospital, employee):
        hospital.employees.add(employee)
        hospital.usernames.append(employee.username)
        hospital.passwords.append(employee.password)