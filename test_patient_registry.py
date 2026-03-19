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
    def test_id_not_changed_during_update(self):
        patient_id = self.patient_registry.register_patient("John Smith")
        updated_record = self.patient_registry.update_patient_name(patient_id, "Jim Smith")
        self.assertIsNotNone(updated_record)
        self.assertEqual(updated_record["name"], "Jim Smith")
        self.assertEqual(updated_record["patient_id"], patient_id)


    #Tests: REQ-04 - Update
    #Unit Test UT-05: Invalid Update
    def test_invalid_update(self):

        patient_update = self.patient_registry.update_patient_name("P-000","John Smith")
        self.assertIsNone(patient_update)

    #Tests: REQ-05 - Deletion
    #Unit Test UT-06: Valid and invalid delete
    def test_valid_invalid_del(self):

        patient_id = self.patient_registry.register_patient("Delete Check")
        deleted_patient = self.patient_registry.delete_patient(patient_id)
        self.assertTrue(deleted_patient)
        self.assertIsNone(self.patient_registry.get_patient(patient_id))

        deleted_id = self.patient_registry.delete_patient("P-000")
        self.assertFalse(deleted_id)

    #Tests: REQ-1, REQ-2, REQ-3, & REQ-4
    #Component Test CT-01: valid workflow
    def test_register_update_retrival_flow(self):

        patient_id = self.patient_registry.register_patient("Jane Doe")
        self.patient_registry.update_patient_name(patient_id, "Jane Smith")
        patient_record = self.patient_registry.get_patient(patient_id)


        self.assertIsNotNone(patient_record)
        self.assertEqual(patient_record["name"], "Jane Smith")
        self.assertEqual(patient_record["patient_id"], patient_id)


    #Tests: REQ-1, REQ-2, & REQ-5
    #Component Test CT-02: delete and retrieve fail flow
    def test_patient_delete_retrival_failure_flow(self):

        patient_id = self.patient_registry.register_patient("Jo Johnson")
        deleted_patient = self.patient_registry.delete_patient(patient_id)
        patient_record = self.patient_registry.get_patient(patient_id)

        self.assertTrue(deleted_patient)
        self.assertIsNone(patient_record)

    #Tests: Extra because i have helpers for listing and getting patients and only have 79% coverage
    #Unit Test UT-07: list patients full check
    def test_patient_list(self):
        patient_1 = self.patient_registry.register_patient("Jane Doe")
        patient_2 = self.patient_registry.register_patient("John Smith")

        all_patients= self.patient_registry.list_all_patients()

        self.assertIsNotNone(all_patients)
        self.assertEqual(len(all_patients), 2)
        self.assertIn({"patient_id": patient_1, "name": "Jane Doe"}, all_patients)
        self.assertIn({"patient_id": patient_2, "name": "John Smith"}, all_patients)

    #Unit Test UT-08: list patients empty check
    def test_patient_list_empty(self):
        all_patients = self.patient_registry.list_all_patients()
        self.assertIsNone(all_patients)

    #Unit Test UT-09: valid get patient check
    def test_get_patient_val(self):
        patient_id = self.patient_registry.register_patient("Jane Doe")
        name = self.patient_registry.get_patient_name(patient_id)
        self.assertIsNotNone(name)
        self.assertEqual(name, "Jane Doe")


    #Unit Test UT-10: invalid get patient check
    def test_get_patient_invalid(self):

        patient_name = self.patient_registry.get_patient_name("P-000")
        self.assertIsNone(patient_name)




if __name__ == '__main__':
    unittest.main()
