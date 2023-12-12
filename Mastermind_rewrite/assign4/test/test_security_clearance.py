import unittest
from src.evaluators import evaluate_security_clearance
from src.application_info import *
from src.response import *

class SecurityClearancetests(unittest.TestCase):
    def test_security_clearance_criteria_passes_an_applicant(self):
        application = Application(security_clearance= True)

        self.assertEqual((PASS, "Applicant has security clearance."), evaluate_security_clearance.evaluate_applicant(application))

    def test_security_clearance_criteria_fails_an_applicant(self):
        application = Application(security_clearance= False)

        self.assertEqual((FAIL, "Applicant has no security clearance."), evaluate_security_clearance.evaluate_applicant(application))
