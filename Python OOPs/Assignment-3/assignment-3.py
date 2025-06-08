# Developing a Patient Record Management System

import unittest

# Creating a Patient class with patient details
class Patient:
    def __init__(self, patient_id: int, name: str, age: int, medical_conditions: tuple):
        self.patient_id = patient_id    # Unique ID given to each patient
        self.name = name                # Patient Name
        self.age = age                  # Patient's age
        self.medical_conditions = medical_conditions    # Medical Conditions of Patient in tuple
    
    # A representation method for the class
    def __repr__(self):
        return f"id: {self.patient_id}, name: {self.name}, age: {self.age}, medical conditions: {self.medical_conditions}"

# Creating a Patient Record class to store all patient details 
class PatientRecord:
    # Creating a dictonary of all patients with patient_id as key
    def __init__(self):
        self.patients = []      # A list of all patients with their data
        self.patients_id = []   # A list of all patient IDs

    # Adding a patient to patient record with Patient class
    def add_patient_record(self, patient: Patient):
        if patient.patient_id in self.patients_id:
            # Don't add patient if already exists
            return None
        else:
            self.patients.append(patient)
            self.patients_id.append(patient.patient_id)
            return f"Added {patient.name} to Patient's record"

    # Updating the medical conditions of patient with patient_id
    def update_patient_medical_info(self, patient_id: int, new_medical_conditions: tuple):
        if patient_id in self.patients_id:
            ind = self.patients_id.index(patient_id)
            self.patients[ind].medical_conditions = self.patients[ind].medical_conditions + new_medical_conditions
            return f"Patient record of {patient_id} has been updated: {self.patients[ind].medical_conditions}"
        else:
            # Don't update if patient doesn't exist
            return None
    
    # Generate a report for all patients
    def generate_medical_reports(self):
        return self.patients

class TestPatientRecordSystem(unittest.TestCase):
    def setUp(self):
        self.patient1 = Patient(101, "Sai", 21, ("ADHD",))
        self.patient2 = Patient(102, "Shreya", 21, ("OCD",))
        self.patient3 = Patient(103, "Shaani", 26, ("BP",))

        self.patient_record = PatientRecord()

        self.patient_record.add_patient_record(self.patient1)
        self.patient_record.add_patient_record(self.patient2)
        self.patient_record.add_patient_record(self.patient3)
    
    # Test to check if patients are added correctly
    def test_add_patient_record(self):
        self.assertEqual(len(self.patient_record.patients), 3)
        self.assertEqual(self.patient_record.patients[0].name, "Sai")
        self.assertEqual(self.patient_record.patients[1].name, "Shreya")
        self.assertEqual(self.patient_record.patients[2].name, "Shaani")
    
    # Test to check if existing patient is added into records
    def test_add_existing_patient(self):
        result = self.patient_record.add_patient_record(patient1)
        self.assertIsNone(result)

    # Test to check if patient's details are updated properly
    def test_update_patient_medical_info(self):
        self.patient_record.update_patient_medical_info(101, ("BP",))
        self.patient_record.update_patient_medical_info(102, ("ADHD",))
        self.patient_record.update_patient_medical_info(103, ("OCD",))

        self.assertEqual(self.patient_record.patients[0].medical_conditions, ("ADHD", "BP"))
        self.assertEqual(self.patient_record.patients[1].medical_conditions, ("OCD", "ADHD"))
        self.assertEqual(self.patient_record.patients[2].medical_conditions, ("BP", "OCD"))
    
    # Test to updating a patient that doesn't exist
    def test_update_nonexistent_patient(self):
        result = self.patient_record.update_patient_medical_info(999, ("Asthma",))
        self.assertIsNone(result)

    # Test to check if generated report is valid or not
    def test_generate_medical_reports(self):
        records = self.patient_record.generate_medical_reports()
        self.assertEqual("Sai", records[0].name)
        self.assertEqual("Shreya", records[1].name)
        self.assertEqual("Shaani", records[2].name)

if __name__ == "__main__":
    # Creating patients
    patient1 = Patient(101, "Sai", 21, ("ADHD",))
    patient2 = Patient(102, "Shreya", 21, ("OCD",))
    patient3 = Patient(103, "Shaani", 26, ("BP",))

    # Creating Patient Records
    patient_record = PatientRecord()

    # Adding Patients into records
    print(f"Adding patient records:")
    print(patient_record.add_patient_record(patient1))
    print(patient_record.add_patient_record(patient2))
    print(patient_record.add_patient_record(patient3))

    # Updating patient medical conditions
    print(f"\nUpdaing patient medical records:")
    print(patient_record.update_patient_medical_info(101, ("BP",)))
    print(patient_record.update_patient_medical_info(102, ("ADHD",)))
    print(patient_record.update_patient_medical_info(103, ("OCD",)))

    # Printing patient report
    print(f"\nGenerating the patient records report:")
    records = patient_record.generate_medical_reports()
    for record in records:
        print(record)

    # Running Unit Tests
    print("\nRunning the Unit Tests:")
    unittest.main()
 