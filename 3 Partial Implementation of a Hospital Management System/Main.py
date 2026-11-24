# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient

def main():
    """
    the main function to be ran when the program runs
    """

    # Initialising the actors
    # admin = Admin('admin','123','B1 1AB') # username is 'admin', password is '123'
    admin = Admin.load_admin()
    doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
    patients = [Patient('Sara','Smith', 20, '07012345678','B1 234'), Patient('Mike','Jones', 37,'07555551234','L2 2AB'), Patient('Daivd','Smith', 15, '07123456789','C1 ABC')]
    discharged_patients = []
    grouped_patients = {}

    # keep trying to login tell the login details are correct
    while True:
        if admin.login():
            running = True # allow the program to run
            break
        else:
            print('Incorrect username or password.')

    while running:
        # print the menu
        print('Choose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- Add patient/view patient/print symptoms/ view grouped patients')
        print(' 3- Assign doctor to a patient')
        print(' 4- Discharge patients')
        print(' 5- View discharged patient')
        print(' 6- Update admin details')
        print(' 7- Reallocate patients to another doctor')
        print(' 8- Store patient data to file')
        print(' 9- Load patient data from file')
        print(' 10- Request Management Report')
        print(' 11- Quit')

        # get the option
        op = input('Option: ')

        if op == '1':
            admin.doctor_management(doctors)

        elif op == '2':
            admin.patient_management(patients, grouped_patients)

        elif op == '3':
            admin.assign_doctor_to_patient(patients, doctors)

        elif op == '4':
            admin.view_patient(patients)
            while True:
                choice = input('Do you want to discharge a patient(Y/N): ').strip().upper()
                if choice == 'Y':
                    admin.discharge(patients, discharged_patients)
                elif choice == 'N':
                    break
                else:
                    print('Please answer by yes or no.')

        elif op == '5':
            admin.view_discharge(discharged_patients)

        elif op == '6':
            if admin.update_details_terminal():
                admin.login()

        elif op == '7':
            admin.reallocation(patients, doctors)

        elif op == '8':
            admin.save_data(patients, discharged_patients)
            print("Patient data saved successfully.")

        elif op == '9':
            admin.load_data()

        elif op == '10':
            admin.management_report(doctors, patients)

        elif op == '11':
            print('Exiting the system. Goodbye!')
            running = False

        else:
            print('Invalid option. Try again')

if __name__ == '__main__':
    main()
