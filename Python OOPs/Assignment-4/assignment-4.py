# Using Mixin Classes to implement a HealthCareSystem
# Here multiple classes implement the functionality and a single main class inherits them
# Main uses multiple inheritence to inherit all functionality

# Class to represent an appointment of patient
class Appointment:
    def __init__(self, id, name, age, date):
        self.id = id        # Appointment ID
        self.name = name    # Patient Name
        self.age = age      # Patient age
        self.date = date    # Patient date
    
    # Readable string representation of the appointment
    def __repr__(self):
        return f"appointment_id: {self.id}, name: {self.name}, age: {self.age}, date: {self.date}"

# Class to represent a patient with details
class Patient:
    def __init__(self, id, name, age):
        self.id = id        # Patient ID
        self.name = name    # Patient name
        self.age = age      # Patient age
    
    # Readable string representation of the appointment
    def __repr__(self):
        return f"patient_id: {self.id}, name: {self.name}, age: {self.age}"

# Mixin class for managing appointments
class AppointmentMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Dictionary to store appointments by their id
        self.appointments = {}

    # Schedules a new appointment if the id is not already present
    def schedule_appointment(self, appointment:Appointment):
        if appointment.id not in self.appointments.keys():
            self.appointments[appointment.id] = appointment
            return f"Appointment of {appointment.id} is scheduled for {appointment.date}"
        else:
            return None

    # Cancels an appointment by id if it exists
    def cancel_appointment(self, appointment_id):
        if appointment_id in self.appointments.keys():
            del self.appointments[appointment_id]
            return f"Appointment of {appointment_id} is cancelled"
        else:
            return None

    # Returns a list of all scheduled appointments
    def print_appointments(self):
        return list(self.appointments.values())

# Mixin class for managing patients
class PatientMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Dictionary to store patients by their id
        self.patients = {}

    # Adds a new patient if the id is not already present
    def add_patient(self, patient:Patient):
        if patient.id not in self.patients.keys():
            self.patients[patient.id] = patient
            return f"Patient {patient.id} successfully added"
        else:
            return None

    # Removes a patient by id if present
    def remove_patient(self, patient_id):
        if patient_id in self.patients.keys():
            del self.patients[patient_id]
            return f"Patient {patient_id} successfully removed"
        else:
            return None

    # Returns a list of all current patients
    def print_patients(self):
        return list(self.patients.values())

# Main system class that inherits appointment and patient classes (Multiple Inheritence)
class HealthCareSystem(AppointmentMixin, PatientMixin):
    # Calls __init__ of both mixin classes to initialize appointments and patients
    def __init__(self):
        super().__init__()

if __name__ == "__main__":
    # Create patient objects
    p1 = Patient(101, "Sai", 21)
    p2 = Patient(102, "Shreya", 21)
    p3 = Patient(103, "Shaani", 26)

    # Create the healthcare system object
    h = HealthCareSystem()
    # Now HealthCareSystem has all methods of AppointmentMixin and PatientMixin

    # Add patients to the system
    print(h.add_patient(p1))    # Output: Patient 101 successfully added
    print(h.add_patient(p2))    # Output: Patient 102 successfully added
    print(h.add_patient(p3))    # Output: Patient 103 successfully added
    print()

    # Remove a patient from the system
    print(h.remove_patient(p2.id))  # Output: Patient 102 successfully removed
    print()

    # Print all current patients
    print("Printing Patients:")
    for patient in h.print_patients():
        print(patient)
    print()

    # Create appointment objects
    a1 = Appointment(101, "Sai", 21, "10-06-2025")
    a2 = Appointment(102, "Shreya", 21, "12-06-2025")
    a3 = Appointment(103, "Shaani", 26, "13-06-2025")

    # Schedule appointments for patients
    print(h.schedule_appointment(a1))   # Output: Appointment of 101 is scheduled for 10-06-2025
    print(h.schedule_appointment(a2))   # Output: Appointment of 102 is scheduled for 12-06-2025
    print(h.schedule_appointment(a3))   # Output: Appointment of 103 is scheduled for 13-06-2025
    print()

    # Cancel an appointment
    print(h.cancel_appointment(a2.id))  # Output: Appointment of 102 is cancelled
    print()

    # Print all current appointments
    print("Printing Appointments:")
    for appointment in h.print_appointments():
        print(appointment)
