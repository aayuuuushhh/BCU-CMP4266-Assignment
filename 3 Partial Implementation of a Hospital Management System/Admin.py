from Doctor import Doctor
from Patient import Patient

class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.__username = username
        self.__password = password
        self.__address =  address
        
    def save_admin(self):
        with open ("admin.txt","w") as f:
            f.write(f"{self.__username},{self.__password},{self.__address}")
            
    def load_admin():
        try:
            with open("admin.txt","r") as f:
                username, password, address = f.read().strip().split(",")
                return Admin(username, password, address)
        except FileNotFoundError:
            return Admin("admin","123","B1 1AB")
                

    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')
            
    def find_index(self,index,doctors):
        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            
            return True

        # if the id is not in the list of doctors
        else:
            return False

    def login(self) :
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
    
        print("-----Login-----")
        #Get the details of the admin

        username = input('Enter the username: ')
        password = input('Enter the password: ')

        # check if the username and password match the registered ones
        #ToDo1
        if username == self.__username and password == self.__password:
            print("Login successful.")
            return True
        else:
            print("Invalid username or password.")
            return False
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        #ToDo2
        first_name = input("Enter doctor's first name: ")
        surname = input("Enter doctor's surname: ")
        speciality = input("Enter doctor's speciality: ")
        return Doctor(first_name, surname, speciality)

    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        #ToDo3
        op = input("Input:")


        # register
        if op == '1':
            print("-----Register-----")

            # get the doctor details
            print('Enter the doctor\'s details:')
            #ToDo4
            new_doctor = self.get_doctor_details()
            first_name = new_doctor.get_first_name()
            surname = new_doctor.get_surname()

            # check if the name is already registered
            name_exists = False
            for doctor in doctors:
                if first_name == doctor.get_first_name() and surname == doctor.get_surname():
                    print('Name already exists.')
                    #ToDo5
                    name_exists = True # save time and end the loop
                    break

            #ToDo6
            if name_exists == False:     # add the doctor ...
                doctors.append(new_doctor)# ... to the list of doctors
                self.save_doctors(doctors)
                print('Doctor registered.')

        # View
        elif op == '2':
            print("-----List of Doctors-----")
            #ToDo7
            print('ID |          Full name           |  Speciality')
            self.view(doctors)


        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index=self.find_index(index,doctors)
                    if doctor_index!=False:
                        break
                    else:
                        print("Doctor not found") # doctor_index is the ID mines one (-1)
                        
                except ValueError: # the entered id could not be changed into an int
                    print('The ID entered is incorrect')

            # menu
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')
            op = int(input('Input: ')) # make the user input lowercase

            #ToDo8
            if op == 1:
                new_first_name = input("Enter the new first name: ")
                doctors[index].set_first_name(new_first_name)
                
            elif op == 2:
                new_surname = input("Enter the new surname: ")
                doctors[index].set_surname(new_surname)
                
            elif op == 3:
                new_speciality = input("Enter the new speciality: ")
                doctors[index].set_speciality(new_speciality)
                
            else:
                print("Invalid field choosen.")
            
            self.save_doctors(doctors)
            print("Doctor details updated successfully.")

        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)
            try:
                doctor_id = int(input('Enter the ID of the doctor to be deleted: '))
                doctor_index = doctor_id - 1
                #ToDo9
                if 0 <= doctor_index < len(doctors):
                    deleted_doctor = doctors.pop(doctor_index)
                    print(f"Doctor {deleted_doctor.full_name()} deleted successfully.")
                    self.save_doctors(doctors)
                else:
                    print('The id entered is incorrect')

        # if the id is not in the list of patients
            except ValueError:
                print('Invalid operation choosen. Check your spelling!')
        else:
            print('Invalid operation chosen.')
                    

    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        #ToDo10
        self.view(patients)
        
    def add_patient(self):
        """
        Adds a new patient to the system
        """
        first_name = input("Enter Patient's first name: ")
        last_name = input("Enter Patient's last name: ")
        while True:
            try:
                age = int(input("Enter Patient's age: "))
                break
            except ValueError:
                print("Please enter a valid age.")
        
        mobile = input("Enter Patient's mobile number: ")
        address = input("Enter Patient's address: ")
        symptoms = []
        while True:
            symptom = input("Enter symptoms one by one (press q or Q when you're done!): ")
            if symptom.lower() == 'q':
                break
            symptoms.append(symptom)
        
        return Patient(first_name, last_name, age, mobile, address, symptoms)
    
    def view_symptoms(self, patient):
        """
        Prints the list of all symptoms
        """
        self.view_patient(patient)
        op = int(input('Please select the ID of the patient you want to view the symptoms of: ')) - 1
        try:
            print()
            print("-----Symptoms-----")
            if op in range(len(patient)):
                patient[op].print_symptoms()
            print()
        except:
            print("Invalid Choice.")
            
    def view_grouped_patient(self, patient, grouped_patients):
        """
        Prints the grouped patients by surname
        """
        
        # Step 1: Sort patients by surname
        patients_sorted = sorted(patient, key=lambda p: p.get_surname())
        
        # Step 2: Print grouped patients
        current_surname = None
        
        for p in patients_sorted:
            surname = p.get_surname()
            
            if surname != current_surname:
                print(f"\n--- Family: {p.get_surname()}---")
                current_surname = surname
                grouped_patients[surname] = []
                
            print(p)
            grouped_patients[surname].append(p)
                
    def patient_management(self, patient, grouped_patients):
        """
        This function is used to manage the patient data
        """
        info = """
        1- add patient
        2- view patient
        3- view symptoms
        4- view grouped patients
        """
        print(info)
        try:
            op = int(input("Please selection operation: "))
            
            if op == 1:
                new_patient = self.add_patient()
                patient.append(new_patient)
                self.save_patients(patient)
                print("Patient added successfully.")
                
            elif op == 2:
                self.view_patient(patient)
                
            elif op == 3:
                self.view_symptoms(patient)
                
            elif op == 4:
                self.view_grouped_patient(patient, grouped_patients)
                
            else:
                print("Invalid choice.")
                
        except ValueError:
            print("Please choose Numeric value only.")

    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(input('Please enter the patient ID: ')) - 1
            if patient_index not in range(len(patients)):
                print('Invalid patient ID.')
                return
        except ValueError:
            print('Please enter a valid numeric patient ID.')
            return

        print("\n-----Doctors-----")
        print('ID |          Full Name           |  Speciality')
        self.view(doctors)

        try:
            doctor_index = int(input('Please enter the doctor ID: ')) - 1
            if doctor_index not in range(len(doctors)):
                print('Invalid doctor ID.')
                return
        except ValueError:
                print('Please enter a valid numeric doctor ID.')
                return

    # Check if patient already has a doctor
        if patients[patient_index].get_doctor() != 'None':
            print('This patient already has a doctor assigned.')
            return

    # Link patient and doctor
        patients[patient_index].link(doctors[doctor_index].full_name())
        doctors[doctor_index].add_patient(patients[patient_index].full_name())

        print('Doctor assigned to patient successfully.')


    def discharge(self, patients, discharged_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        print("-----Discharge Patient-----")
        self.view_patient(patients)

        #ToDo12
        try:
            patient_index = int(input("Please enter the patient ID: ")) - 1
            if 0 <= patient_index < len(patients):
                discharged = patients.pop(patient_index)
                discharged_patients.append(discharged)
                print(f"Patient {discharged.full_name()} has been discharged.")
            else:
                print("The id entered was not found.")
        except ValueError:
                print("The id entered is incorrect.")

    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        #ToDo13
        if not discharged_patients:
            print("No discharged patients.")
            return
        
        self.view(discharged_patients)
        
    def reallocation(self, patients, doctors):
        """
        This function is used to reallocate the patient to a doctor
        """
        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)
        
        patient_index = input('Please enter the patient ID you want to reallocate: ')
        try:
            patient_index = int(patient_index) - 1
            if patient_index not in range (len(patients)):
                return
            
        except ValueError:
            print('The id entered is incorrect.')
            return
        print("-----Doctors Select-----")
        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter doctor ID: ')
        try:
            doctor_index = int(doctor_index) - 1
            
            if self.find_index(doctor_index, doctors)!= False:
                patients[patient_index].link(doctors[doctor_index].full_name())
                doctors[doctor_index].add_patient(patients[patient_index])
                print('The patient is now reallocated to new doctor.')
            else:
                print('The id entered was not found.')
        except ValueError:
            print('The id entered is incorrect.')
            
    def management_report(self, doctors, patients):
        """
        Prints a management summary report
        """
        print("-----Management Report-----")
        print(f"Total number of doctors   : {len(doctors)}")
        print(f"Total number of patients  : {len(patients)}")
        print("-" * 45)
        
        for doctor in doctors:
            print(f"Doctor Name   : {doctor.full_name()}")
            print(f"Speciality    : {doctor.get_speciality()}")
            print(f"No. of Patients Assigned : {len(doctor.get_patients())}")
            print(f"No. of Appointments      : {len(doctor.get_appointments())}")
            print("-" * 45)
            
    def save_doctors(self, doctors):
        with open("doctors.txt","w") as f: 
            for d in doctors: 
                f.write( 
                        f"{d.get_first_name()},"
                        f"{d.get_surname()},"
                        f"{d.get_speciality()}\n" 
                )

    def save_patients(self, patients):
        with open("patients.txt", "w") as f:
            for p in patients:
                f.write(
                    f"{p.full_name()},"
                        f"{p.get_age()},"
                    f"{p.get_mobile()},"
                    f"{p.get_postcode()},"
                    f"{','.join(p.write_symptoms())}\n"
                 )
                
    def save_data(self, patient, discharge_patients):
        """
        This function is used to save the patient data into a file
        """
        with open('patients.txt', 'w') as f:
            for p in patient:
                f.write(f"Name: {p.full_name()}\n")
                f.write(f"Age: {p.get_age()}\n")
                f.write(f"Mobile No.: {p.get_mobile()}\n")
                f.write(f"Address: {p.get_postcode()}\n")
                f.write(f"Symptoms: {p.write_symptoms()}\n")
                f.write(f"Is_Discharged: NO\n")
                f.write("\n")
                
            for d in discharge_patients:
                f.write(f"Name: {d.full_name()}\n")
                f.write(f"Age: {d.get_age()}\n")
                f.write(f"Mobile No.: {d.get_mobile()}\n")
                f.write(f"Address: {d.get_postcode()}\n")
                f.write(f"Symptoms: {d.write_symptoms()}\n")
                f.write(f"Is_Discharged: YES\n")
                f.write("\n")
                
    def load_data(self):
        """
        This function is used to load the patient data from a file and display it in the terminal
        """
        try:
            with open('patients.txt', 'r') as f:
                print('-----Loaded Patient Data-----')
                patient_data = {}
                
                for line in f:
                    line = line.strip()
                    
                    if not line:
                        if patient_data:
                            print(f"Name: {patient_data.get('Name', 'N/A')}")
                            print(f"Age: {patient_data.get('Age', 'N/A')}")
                            print(f"Mobile No: {patient_data.get('Mobile No.', 'N/A')}")
                            print(f"Address: {patient_data.get('Address', 'N/A')}")
                            print(f"Symptoms: {patient_data.get('Symptoms', 'N/A')}")
                            print(f"Is Discharged: {patient_data.get('Is_Discharged', 'N/A')}")
                            print("")
                            patient_data = {}
                        continue
                        
                    key, value = line.split(": ", 1)
                    patient_data[key] = value
                                
                if patient_data:
                    print(f"Name: {patient_data.get('Name', 'N/A')}")
                    print(f"Age: {patient_data.get('Age', 'N/A')}")
                    print(f"Mobile No: {patient_data.get('Mobile No', 'N/A')}")
                    print(f"Address: {patient_data.get('Address', 'N/A')}")
                    print(f"Symptoms: {patient_data.get('Symptoms', 'N/A')}")
                    print(f"Is Discharged: {patient_data.get('Is_Discharged', 'N/A')}")      
                    print("")
                    
        except FileNotFoundError:
            print("The file patients.txt does not exist. ")
        except Exception as e:
            print(f"An error occured: {e}")

    def update_details_terminal(self):
        """
        Allows the user to update and change username, password and address
        """

        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = int(input('Input: '))

        if op == 1:
            #ToDo14
            new_username = input('Enter the new username: ')
            self.__username = new_username
            self.save_admin()
            print('Username updated successfully.')

        elif op == 2:
            password = input('Enter the new password: ')
            # validate the password
            if password == input('Enter the new password again: '):
                self.__password = password
                self.save_admin()
                print('Password updated successfully.')

        elif op == 3:
            #ToDo15
            new_address = input("Enter new address: ")
            self.__address = new_address
            self.save_admin()
            print(f'Address updated successfully to {self.__address}.')

        else:
            #ToDo16
            print('Invalid option selected. Please choose 1, 2, or 3.')
                     