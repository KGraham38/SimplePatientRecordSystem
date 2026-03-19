#Kody Graham
#03/17/2026
#Simple Patient Record System - Test Class
#Class to test our Simple Patient Record System

#Ive never used either recommended testing frameworks, unittest is built in so Ill just use it
import unittest
from patient_registry import PatientRegistry

class PatientRegistryTest(unittest.TestCase):
    def setUp(self):
        self.patient_registry = PatientRegistry()

    #Tests: REQ-01 - Creation
    #Unit Test UT-01: Normal Case - register patient
    def test_patient_registration(self):
        patient_id = self.patient_registry.register_patient("John Smith")
        self.assertEqual(patient_id, "P-101")
        self.assertIn(patient_id, self.patient_registry.patient_registry)
        self.assertEqual(self.patient_registry.patient_registry[patient_id], {"patient_id": patient_id, "name": "John Smith"})

    #Tests: REQ-02 - Retrieval
    #Unit test UT-02: Normal Case
    def test_patient_retrival(self):

        patient_id= self.patient_registry.register_patient("John Smith")
        patient_record = self.patient_registry.get_patient(patient_id)
        self.assertEqual(patient_record, {"patient_id": patient_id, "name": "John Smith"})

    #Tests: REQ-02 - Retrieval
    #Unit Test UT-03: Invalid
    def test_patient_retrival_failure(self):
        patient_record = self.patient_registry.get_patient("P-000")
        self.assertIsNone(patient_record)

    #Tests: REQ-03 & REQ-04 - Immutability & Retrieval
    #Unit Test UT-04: Update patient name, ID not change


    #Tests: REQ-04 - Update
    #Unit Test UT-05: Invalid Update

    #Tests: REQ-05 - Deletion
    #Unit Test UT-06: Valid and invalid delete

    #Tests: REQ-1, REQ-2, REQ-3, & REQ-4
    #Component Test CT-01: valid workflow

    #Tests: REQ-1, REQ-2, & REQ-5
    #Component Test CT-02: delete and retrieve fail flow
    def test_patient_delete_retrival_failure_flow(self):
        patient_id = self.patient_registry.register_patient("Jo Johnson")
        deleted_patient = self.patient_registry.delete_patient(patient_id)
        patient_record = self.patient_registry.get_patient(patient_id)

        self.assertTrue(deleted_patient)
        self.assertIsNone(patient_record)

if __name__ == '__main__':
    unittest.main()
