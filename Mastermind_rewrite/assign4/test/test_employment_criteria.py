import unittest
from src.evaluators import evaluate_employment_status
from src.application_info import *
from src.response import *

class EmploymentCriteriontests(unittest.TestCase):
    def test_employment_criteria_passes_an_applicant(self):
        application = Application(employment_status= True)

        self.assertEqual((PASS, "Applicant has had previous employment."), evaluate_employment_status.evaluate_applicant(application))

    def test_employment_criteria_fails_an_applicant(self):
        application = Application(employment_status= False)

        self.assertEqual((FAIL, "Applicant has no previous employment."), evaluate_employment_status.evaluate_applicant(application))
