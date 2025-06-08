# Medical Services using Abstract Base Classes

from abc import ABC, abstractmethod
import unittest

# Abstract Base Class for all medical services
class Medical_service(ABC):
    
    # Abstract method to schedule a appointment
    @abstractmethod
    def schedule_appointment(self, patient_name, date_time):
        pass

    # Abstract method to record patient data
    @abstractmethod
    def record_patient_data(self, patient_name, data):
        pass
    
    # Abstract method to generate patient report
    @abstractmethod
    def generate_medical_report(self, patient_name):
        pass

# Concrete class for consultation service
class Consultation_service(Medical_service):
    def __init__(self):
        self.appointments = {}  # To store patient appointments
        self.patient_data = {}  # To store patients data
    
    # Method to schedule a consultation appointment
    def schedule_appointment(self, patient_name, date_time):
        self.appointments[patient_name] = date_time
        return f"Consultation appointment for {patient_name} is scheduled on {date_time}"
    
    # Method to record consultation data of patient
    def record_patient_data(self, patient_name, data):
        self.patient_data[patient_name] = data
        return f"Consultation data for {patient_name} has been recorded"
    
    # Method to generate consultation report of patient
    def generate_medical_report(self, patient_name):
        data = self.patient_data[patient_name]
        return f"The Consultation Report for {patient_name}:\n{data}"

# Concrete class for procedure services
class Procedure_service(Medical_service):
    def __init__(self):
        self.appointments = {}  # To store patient appointments
        self.patient_data = {}  # To store patients data

    # Method to schedule a procedure appointment
    def schedule_appointment(self, patient_name, date_time):
        self.appointments[patient_name] = date_time
        return f"Procedure appointment for {patient_name} is scheduled on {date_time}"
    
    # Method to record procedure data of patient
    def record_patient_data(self, patient_name, data):
        self.patient_data[patient_name] = data
        return f"Procedure data for {patient_name} has been recorded"
    
    # Method to generate procedure report of patient
    def generate_medical_report(self, patient_name):
        data = self.patient_data[patient_name]
        return f"The Procedure Report for {patient_name}:\n{data}"

# Concrete class for diagnostic services
class Diagnostic_service(Medical_service):
    def __init__(self):
        self.appointments = {}  # To store patient appointments
        self.patient_data = {}  # To store patients data

    # Method to schedule a diagnosis appointment
    def schedule_appointment(self, patient_name, date_time):
        self.appointments[patient_name] = date_time
        return f"Diagnosis appointment for {patient_name} is scheduled on {date_time}"
    
    # Method to record consultation data of patient
    def record_patient_data(self, patient_name, data):
        self.patient_data[patient_name] = data
        return f"Diagnosis data for {patient_name} has been recorded"
    
    # Method to generate consultation report of patient
    def generate_medical_report(self, patient_name):
        data = self.patient_data[patient_name]
        return f"The Diagnosis Report for {patient_name}:\n{data}"
    
# Unit Tests for all Medical Services
class TestMedicalServices(unittest.TestCase):

    # Create instances of each service for testing
    def setUp(self):
        self.consultation = Consultation_service()
        self.procedure = Procedure_service()
        self.diagnostic = Diagnostic_service()

    # Test scheduling, recording, and reporting for consultation
    def test_consultation_service(self):
        msg = self.consultation.schedule_appointment("Sai", "2025-06-10 10:00")
        self.assertIn("scheduled", msg)
        msg = self.consultation.record_patient_data("Sai", {"symptoms": "Cough", "diagnosis": "Flu", "recommendations": "Rest"})
        self.assertIn("recorded", msg)
        report = self.consultation.generate_medical_report("Sai")
        self.assertIn("Consultation Report for Sai", report)

    # Test scheduling, recording, and reporting for consultation
    def test_procedure_service(self):
        msg = self.procedure.schedule_appointment("Shreya", "2025-06-11 14:00")
        self.assertIn("scheduled", msg)
        msg = self.procedure.record_patient_data("Shreya", {"procedure": "Appendectomy", "outcome": "Successful", "notes": "No complications"})
        self.assertIn("recorded", msg)
        report = self.procedure.generate_medical_report("Shreya")
        self.assertIn("Procedure Report for Shreya", report)

    # Test scheduling, recording, and reporting for diagnostic
    def test_diagnostic_service(self):
        msg = self.diagnostic.schedule_appointment("Shaani", "2025-06-12 09:00")
        self.assertIn("scheduled", msg)
        msg = self.diagnostic.record_patient_data("Shaani", {"test": "X-ray", "results": "Normal", "interpretation": "No issues"})
        self.assertIn("recorded", msg)
        report = self.diagnostic.generate_medical_report("Shaani")
        self.assertIn("Diagnosis Report for Shaani", report)
    
if __name__ == "__main__":
    # Demonstration of each service
    c = Consultation_service()
    print(c.schedule_appointment("Sai", "2025-06-10 10:00"))
    print(c.record_patient_data("Sai", {"symptoms": "Cough", "diagnosis": "Flu", "recommendations": "Rest"}))
    print(c.generate_medical_report("Sai"), end="\n\n")

    p = Procedure_service()
    print(p.schedule_appointment("Shreya", "2025-06-11 14:00"))
    print(p.record_patient_data("Shreya", {"procedure": "Surgey", "outcome": "Successful", "notes": "No complications"}))
    print(p.generate_medical_report("Shreya"), end="\n\n")

    d = Diagnostic_service()
    print(d.schedule_appointment("Shaani", "2025-06-12 09:00"))
    print(d.record_patient_data("Shaani", {"test": "X-ray", "results": "Normal", "interpretation": "No issues"}))
    print(d.generate_medical_report("Shaani"), end="\n\n")

    # Running all unit tests
    unittest.main()