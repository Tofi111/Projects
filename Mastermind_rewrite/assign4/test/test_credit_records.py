import unittest
from src.evaluators import evaluate_credit_records
from src.application_info import *
from src.response import *

class Creditrecordstests(unittest.TestCase):
    def test_credit_records_criteria_passes_an_applicant(self):
        application = Application(credit_records= True)

        self.assertEqual((PASS, "Applicant has a credit record."), evaluate_credit_records.evaluate_applicant(application))

    def test_credit_records_criteria_fails_an_applicant(self):
        application = Application(credit_records= False)

        self.assertEqual((FAIL, "Applicant has no credit record."), evaluate_credit_records.evaluate_applicant(application))
