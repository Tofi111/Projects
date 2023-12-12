import unittest
from src.evaluators import evaluate_criminal_records
from src.application_info import *
from src.response import *

class CriminalRecordsTests(unittest.TestCase):
    def test_criminal_records_criteria_passes_an_applicant(self):
        application = Application(criminal_records= False)

        self.assertEqual((PASS, "Applicant has had no criminal records."), evaluate_criminal_records.evaluate_applicant(application))

    def test_criminal_records_criteria_fails_an_applicant(self):
        application = Application(criminal_records= True)

        self.assertEqual((FAIL, "Applicant has criminal records."), evaluate_criminal_records.evaluate_applicant(application))
