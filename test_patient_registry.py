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
    #Unit Test UT-01: Normal Case

    #Tests: REQ-02 - Retrieval
    #Unit test UT-02: Normal Case

    #Tests: REQ-02 - Retrieval
    #Unit Test UT-03: Normal Case

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

if __name__ == '__main__':
    unittest.main()
