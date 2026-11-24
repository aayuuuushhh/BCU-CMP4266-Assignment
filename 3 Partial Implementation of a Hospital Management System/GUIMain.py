import tkinter as tk
from tkinter import messagebox, ttk
from Admin import Admin
from Doctor import Doctor
from Patient import Patient

class HospitalGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1100x650")

       
        self.admin = Admin("admin", "123", "B1 1AB")
        self.doctors = [
            Doctor("John", "Smith", "Internal Med."),
            Doctor("Jone", "Smith", "Pediatrics"),
            Doctor("Jone", "Carlos", "Cardiology")
        ]
        self.patients = [
            Patient("Sara", "Smith", 20, "07012345678", "B1 234"),
            Patient("Mike", "Jones", 37, "07555551234", "L2 2AB"),
            Patient("David", "Smith", 15, "07123456789", "C1 ABC")
        ]
        self.discharged_patients = []
        self.login_screen()

    
    def login_screen(self):
        self.clear()
        frame = tk.Frame(self.root)
        frame.pack(expand=True)

        tk.Label(frame, text="Admin Login", font=("Arial", 22)).pack(pady=15)

        tk.Label(frame, text="Username").pack()
        self.username = tk.Entry(frame, width=30)
        self.username.pack()

        tk.Label(frame, text="Password").pack()
        self.password = tk.Entry(frame, show="*", width=30)
        self.password.pack()

        tk.Button(frame, text="Login", width=15, command=self.login).pack(pady=15)

    def login(self):
        if self.username.get() == "admin" and self.password.get() == "123":
            self.dashboard()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    
    def dashboard(self):
        self.clear()

        self.left = tk.Frame(self.root, width=260, bg="#e0e0e0")
        self.left.pack(side="left", fill="y")

        self.right = tk.Frame(self.root)
        self.right.pack(side="right", expand=True, fill="both")

        buttons = [
            ("1. Doctor Management", self.doctor_menu),
            ("2. Discharge Patient", self.discharge_patient),
            ("3. View Discharged Patients", self.view_discharged),
            ("4. Assign Doctor", self.assign_doctor),
            ("5. Update Admin Details", self.update_admin),
            ("6. Patient Management", self.patient_menu),
            ("7. Store Patient Data", self.save_data),
            ("8. Load Patient Data", self.load_data),
            ("9. Reallocate Patient", self.reallocate),
            ("10. Management Report", self.management_report),
            ("11. Quit", self.root.quit)
        ]

        for text, cmd in buttons:
            tk.Button(self.left, text=text, width=30, command=cmd).pack(pady=4)

    
    def doctor_menu(self):
        self.right_clear()
        tk.Label(self.right, text="Doctor Management", font=("Arial", 18)).pack(pady=10)

        tk.Button(self.right, text="Register Doctor", command=self.register_doctor).pack(pady=5)
        tk.Button(self.right, text="View Doctors", command=lambda: self.list_display(self.doctors)).pack(pady=5)
        tk.Button(self.right, text="Delete Doctor", command=self.delete_doctor).pack(pady=5)
        
    def delete_doctor(self):
        def delete_action(doctor):
            self.doctors.remove(doctor)
            messagebox.showinfo(
                "Success",
                f"Doctor {doctor.full_name()} deleted successfully"
            )
            self.doctor_menu()

        self.select_item_action(
            "Delete Doctor",
            self.doctors,
            delete_action
        )



    def register_doctor(self):
        self.right_clear()
        f = self.form_frame()
        
        entries = {}
        for field in ["First Name","Surname","Speciality"]:
            tk.Label(f, text=field).pack()
            e = tk.Entry(f, width=40)
            e.pack()
            entries[field] = e
            
        def save():
            if not all(entries[k].get().strip() for k in entries):
                messagebox.showerror("Error","All fields required.")
                return
            
            new_doctor = Doctor(
                entries["First Name"].get(),
                entries["Surname"].get(),
                entries["Speciality"].get()
            )
            self.doctors.append(new_doctor)
            messagebox.showinfo("Success","Doctor registered")
            self.doctor_menu()
        tk.Button(
            f, 
            text="Save Doctor", 
            command=save, 
            bg="#4CAF50",
            fg="white",
            width=20
        ).pack(pady=20)
        
    
    def patient_menu(self):
        self.right_clear()
        tk.Label(self.right, text="Patient Management", font=("Arial", 18)).pack(pady=10)

        tk.Button(self.right, text="Add Patient", command=self.add_patient).pack(pady=5)
        tk.Button(self.right, text="View Patients", command=lambda: self.list_display(self.patients)).pack(pady=5)
        tk.Button(self.right, text="View Symptoms", command=self.view_symptoms).pack(pady=5)
        tk.Button(self.right, text="View Grouped Patients", command=self.view_grouped).pack(pady=5)

    def add_patient(self):
        self.form_clear()
        f = self.form_frame()

        entries = {}
        for field in ["First Name", "Surname", "Age", "Mobile", "Address"]:
            tk.Label(f, text=field).pack(anchor="w")
            e = tk.Entry(f, width=40)
            e.pack()
            entries[field] = e

        tk.Label(f, text="Symptoms (one per line)").pack(anchor="w")
        symptoms_box = tk.Text(f, height=6, width=40)
        symptoms_box.pack()

        def save():
            try:
                symptoms = [s.strip() for s in symptoms_box.get("1.0", tk.END).strip().split("\n") if s.strip()]
                self.patients.append(
                    Patient(
                        entries["First Name"].get(),
                        entries["Surname"].get(),
                        int(entries["Age"].get()),
                        entries["Mobile"].get(),
                        entries["Address"].get(),
                        symptoms
                    )
                )
                messagebox.showinfo("Success", "Patient added")
                self.patient_menu()
            except ValueError:
                messagebox.showerror("Error", "Age must be numeric")

        tk.Button(f, text="Add Patient", command=save).pack(pady=10)

    def view_symptoms(self):
        self.select_patient_action("View Symptoms", lambda p:
            messagebox.showinfo("Symptoms", "\n".join(p.get_symptoms()) or "No symptoms"))

    def view_grouped(self):
        self.right_clear()
        f = tk.Frame(self.right)
        f.pack(expand=True, fill="both", padx=20, pady=20)
        
        grouped = {}
        for p in self.patients:
            surname = p.get_surname()
            if surname not in grouped:
                grouped[surname] = []
            grouped[surname].append(p.full_name())

        text = "GROUPED PATIENTS BY FAMILY:\n\n"
        for surname, names in grouped.items():
            text += f"{surname} Family:\n"
            for name in names:
                text += f"  - {name}\n"
            text += "\n"

        text_widget = tk.Text(f, height=25, width=80, font=("Arial", 11))
        text_widget.insert("1.0", text)
        text_widget.config(state="disabled")
        text_widget.pack(expand=True, fill="both")

    
    def discharge_patient(self):
        self.select_patient_action(
            "Discharge Patient",
            lambda p: self._discharge(p)
        )

    def _discharge(self, patient):
        if patient in self.patients:
            self.patients.remove(patient)
            self.discharged_patients.append(patient)
            messagebox.showinfo("Discharged", f"{patient.full_name()} discharged")
        self.patient_menu()

    def view_discharged(self):
        self.list_display(self.discharged_patients)

    
    def assign_doctor(self):
        self.show_id_based_interface(True)

    def reallocate(self):
        self.show_id_based_interface(False)

    def show_id_based_interface(self, is_assign=True):
        self.right_clear()
        main_frame = tk.Frame(self.right)
        main_frame.pack(expand=True, fill="both", padx=20, pady=20)

        title = "ASSIGN DOCTOR" if is_assign else "REALLOCATE DOCTOR"
        tk.Label(main_frame, text=title, font=("Arial", 20, "bold")).pack(pady=20)

        
        tk.Label(main_frame, text="Patients", font=("Arial", 14, "bold")).pack(pady=(0,10))
        
        patients_frame = tk.Frame(main_frame)
        patients_frame.pack(fill="x", pady=(0,10))
        
        
        header = "ID |          Full Name           |      Doctor's Full Name      | Age |    Mobile     | Postcode"
        tk.Label(patients_frame, text=header, font=("Courier", 11, "bold"), bg="#e0e0e0", relief="ridge").pack(fill="x")
        
        
        for i, p in enumerate(self.patients, 1):
            doctor_name = p.get_doctor() if hasattr(p, 'get_doctor') else getattr(p, '_Patient__doctor', 'None')
            try:
                age = p._Patient__age  
                mobile = p._Patient__mobile
                address = p._Patient__address
            except:
                age = "N/A"
                mobile = "N/A" 
                address = "N/A"
                
            row = f"{i:2d}| {p.full_name():<22} | {doctor_name:>22} | {age:<3} | {mobile:>12} | {address}"
            tk.Label(patients_frame, text=row, font=("Courier", 10), relief="ridge", anchor="w").pack(fill="x")

        
        tk.Label(main_frame, text=f"Please enter the patient ID you want to {'assign':<8}:" if is_assign else "Please enter the patient ID you want to reallocate:", 
                font=("Arial", 12)).pack(pady=(10,5))
        self.patient_id_entry = tk.Entry(main_frame, width=10, font=("Arial", 14), justify="center")
        self.patient_id_entry.pack(pady=(0,20))
        self.patient_id_entry.focus()

        
        tk.Label(main_frame, text="Doctors Select", font=("Arial", 14, "bold")).pack(pady=(0,10))
        
        doctors_frame = tk.Frame(main_frame)
        doctors_frame.pack(fill="x", pady=(0,10))
        
        
        header = "ID |          Full Name           |  Speciality"
        tk.Label(doctors_frame, text=header, font=("Courier", 11, "bold"), bg="#e0e0e0", relief="ridge").pack(fill="x")
        
        
        for i, d in enumerate(self.doctors, 1):
            row = f"{i:2d}| {d.full_name():<22} | {d.get_speciality():<12}"
            tk.Label(doctors_frame, text=row, font=("Courier", 10), relief="ridge", anchor="w").pack(fill="x")

        
        tk.Label(main_frame, text="Please enter doctor ID:", font=("Arial", 12)).pack(pady=(10,5))
        self.doctor_id_entry = tk.Entry(main_frame, width=10, font=("Arial", 14), justify="center")
        self.doctor_id_entry.pack(pady=(0,20))

        
        button_frame = tk.Frame(main_frame)
        button_frame.pack(pady=30)

        def apply_assignment():
            try:
                p_id = int(self.patient_id_entry.get())
                d_id = int(self.doctor_id_entry.get())
                
                if not (1 <= p_id <= len(self.patients)):
                    messagebox.showerror("Error", f"Patient ID must be between 1 and {len(self.patients)}")
                    return
                if not (1 <= d_id <= len(self.doctors)):
                    messagebox.showerror("Error", f"Doctor ID must be between 1 and {len(self.doctors)}")
                    return

                patient = self.patients[p_id - 1]
                doctor = self.doctors[d_id - 1]
                
                
                patient.link(doctor.full_name())
                
                action = "assigned" if is_assign else "reallocated"
                messagebox.showinfo("Success", 
                    f"The patient is now {action} to new doctor.\n\n"
                    f"Patient: {patient.full_name()}\n"
                    f"Doctor: {doctor.full_name()}")
                
                
                self.show_id_based_interface(is_assign)
                
            except ValueError:
                messagebox.showerror("Error", "Please enter valid numeric IDs (1, 2, 3 etc.)")
            except Exception as e:
                messagebox.showerror("Error", f"Assignment failed!\n\nDetails: {str(e)}\n\nMake sure Patient.link() method exists and works.")

        tk.Button(button_frame, text="Apply", command=apply_assignment,
                 bg="#4CAF50", fg="white", font=("Arial", 14, "bold"), width=12, height=2).pack(side="left", padx=20)
        tk.Button(button_frame, text="Back", command=self.dashboard,
                 bg="#f44336", fg="white", font=("Arial", 12), width=12).pack(side="left")

    
    def update_admin(self):
        self.right_clear()
        f = tk.Frame(self.right)
        f.pack(expand=True, fill="both", padx=50, pady=50)

        tk.Label(f, text="Update Admin Details", font=("Arial", 20)).pack(pady=20)

        tk.Label(f, text="New Username", font=("Arial", 12)).pack(pady=(20,5))
        self.new_username = tk.Entry(f, width=40, font=("Arial", 12))
        self.new_username.pack()

        tk.Label(f, text="New Password", font=("Arial", 12)).pack(pady=(20,5))
        self.new_password1 = tk.Entry(f, show="*", width=40, font=("Arial", 12))
        self.new_password1.pack()

        tk.Label(f, text="Confirm Password", font=("Arial", 12)).pack(pady=(10,5))
        self.new_password2 = tk.Entry(f, show="*", width=40, font=("Arial", 12))
        self.new_password2.pack()

        tk.Label(f, text="New Address", font=("Arial", 12)).pack(pady=(20,5))
        self.new_address = tk.Entry(f, width=40, font=("Arial", 12))
        self.new_address.pack()

        def save():
            if self.new_password1.get() != self.new_password2.get():
                messagebox.showerror("Error", "Passwords do not match")
                return
            if not all([self.new_username.get(), self.new_password1.get(), self.new_address.get()]):
                messagebox.showerror("Error", "All fields are required")
                return
                
            try:
                self.admin._Admin__username = self.new_username.get()
                self.admin._Admin__password = self.new_password1.get()
                self.admin._Admin__address = self.new_address.get()
                messagebox.showinfo("Success", "Admin details updated successfully")
                self.dashboard()
            except Exception as e:
                messagebox.showerror("Error", f"Update failed: {str(e)}")

        tk.Button(f, text="Update Admin", command=save, bg="#2196F3", fg="white", 
                 font=("Arial", 14), width=20).pack(pady=30)

    
    def management_report(self):
        self.right_clear()
        report_frame = tk.Frame(self.right)
        report_frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        report = "-----Management Report-----\n"
        report += f"Total number of doctors   : {len(self.doctors)}\n"
        report += f"Total number of patients  : {len(self.patients)}\n"
        report += f"Total discharged patients : {len(self.discharged_patients)}\n"
        report += "=" * 50 + "\n\n"

        for d in self.doctors:
            count = sum(1 for p in self.patients if (hasattr(p, 'get_doctor') and p.get_doctor() == d.full_name()))
            report += f"Doctor: {d.full_name()}\n"
            report += f"Speciality: {d.get_speciality()}\n"
            report += f"Patients Assigned: {count}\n"
            report += f"Appointments: {count}\n"
            report += "-" * 50 + "\n"

        text = tk.Text(report_frame, height=30, width=90, font=("Courier", 10))
        scrollbar = tk.Scrollbar(report_frame)
        scrollbar.pack(side="right", fill="y")
        text.pack(side="left", fill="both", expand=True)
        text.config(yscrollcommand=scrollbar.set, state="normal")
        scrollbar.config(command=text.yview)
        
        text.insert("1.0", report)
        text.config(state="disabled")

    
    def save_data(self):
        try:
            self.admin.save_data(self.patients, self.discharged_patients)
            messagebox.showinfo("Saved", "Data saved successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Save failed: {str(e)}")

    def load_data(self):
        try:
            loaded_data = self.admin.load_data()
            if loaded_data and len(loaded_data) >= 2:
                self.patients, self.discharged_patients = loaded_data
                messagebox.showinfo("Loaded", f"Loaded {len(self.patients)} patients, {len(self.discharged_patients)} discharged")
            else:
                messagebox.showinfo("Loaded", "No data found or load successful (empty)")
        except Exception as e:
            messagebox.showerror("Error", f"Load failed: {str(e)}")

   
    def select_patient_action(self, title, action):
        self.right_clear()
        frame = tk.Frame(self.right)
        frame.pack(expand=True, fill="both", padx=20, pady=20)

        tk.Label(frame, text=title, font=("Arial", 18)).pack(pady=20)

        list_frame = tk.Frame(frame)
        list_frame.pack(fill="x", pady=10)
        
        lb = tk.Listbox(list_frame, height=15, width=80)
        scrollbar = tk.Scrollbar(list_frame, orient="vertical")
        lb.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=lb.yview)
        
        lb.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        for p in self.patients:
            lb.insert(tk.END, p.full_name())

        def go():
            try:
                selected = lb.curselection()[0]
                if selected < len(self.patients):
                    action(self.patients[selected])
                else:
                    messagebox.showerror("Error", "Invalid selection")
            except IndexError:
                messagebox.showerror("Error", "Please select a patient")
            except Exception as e:
                messagebox.showerror("Error", f"Error: {str(e)}")

        tk.Button(frame, text="Proceed", command=go, width=15).pack(pady=20)
        
        
    def select_item_action(self, title, data, action):
        self.right_clear()
        frame = tk.Frame(self.right)
        frame.pack(expand=True, fill="both", padx=20, pady=20)

        tk.Label(frame, text=title, font=("Arial", 18)).pack(pady=20)

        lb = tk.Listbox(frame, height=15, width=60)
        lb.pack(pady=10)

        for item in data:
            lb.insert(tk.END, item.full_name())

        def go():
            try:
                index = lb.curselection()[0]
                action(data[index])
            except IndexError:
                messagebox.showerror("Error", "Please select an item")

        tk.Button(frame, text="Delete", command=go, width=15).pack(pady=10)
        tk.Button(frame, text="Back", command=self.doctor_menu, width=15).pack()



    def list_display(self, data):
        self.right_clear()
        frame = tk.Frame(self.right)
        frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        tk.Label(frame, text=f"List of {len(data)} Records", font=("Arial", 16)).pack(pady=10)
        
        list_frame = tk.Frame(frame)
        list_frame.pack(fill="both", expand=True)
        
        canvas = tk.Canvas(list_frame)
        scrollbar = tk.Scrollbar(list_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        for item in data:
            label = tk.Label(scrollable_frame, text=str(item), anchor="w", 
                           font=("Arial", 10), padx=10, pady=2)
            label.pack(fill="x")

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def selection_delete(self, data, menu_callback=None):
        def delete_action(selected_item):
            if selected_item in data:
                data.remove(selected_item)
                messagebox.showinfo("Success", f"{selected_item.full_name()} deleted successfully")
        if menu_callback:
            menu_callback()
        else:
            self.list_display(data)

        self.select_patient_action("Delete Doctor", delete_action)

    def clear(self):
        for w in self.root.winfo_children():
            w.destroy()

    def right_clear(self):
        if hasattr(self, 'right') and self.right.winfo_exists():
            for w in self.right.winfo_children():
                w.destroy()

    def form_clear(self):
        if hasattr(self, 'right') and self.right.winfo_exists():
            for w in self.right.winfo_children():
                if isinstance(w, tk.Frame):
                    w.destroy()

    def form_frame(self):
        f = tk.Frame(self.right)
        f.pack(expand=True, fill="both", pady=20)
        return f

if __name__ == "__main__":
    root = tk.Tk()
    HospitalGUI(root)
    root.mainloop()
