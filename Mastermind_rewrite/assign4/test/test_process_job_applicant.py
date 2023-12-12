import unittest
from src.job_applicant_processor import *
from src.application_info import *
from src.evaluators import evaluate_employment_status, evaluate_criminal_records
from src.response import *

class ProcessJobApplicantTests(unittest.TestCase):
    def setUp(self):
        self.employment_criteria = evaluate_employment_status.evaluate_applicant
        self.criminal_records = evaluate_criminal_records.evaluate_applicant

    def test_canary(self):
        self.assertTrue(True)

    def test_process_applicant_takes_an_application_and_no_criteria(self):
        self.assertEqual((PASS, 'Nothing to check'), process_applicant(Application()))

    def test_process_applicant_takes_an_application_and_employment_criteria(self):
        application = Application(employment_status = True)

        self.assertEqual((PASS, "Applicant has had previous employment."), process_applicant(application, self.employment_criteria))

    def test_process_applicant_takes_an_application_and_employment_criteria_and_fails(self):
        application = Application(employment_status = False)

        self.assertEqual((FAIL, "Applicant has no previous employment."), process_applicant(application, self.employment_criteria))
    
    def test_process_applicant_takes_an_application_and_employment_and_criminal_records_criterias_and_passes(self):
        application = Application(employment_status = True, criminal_records = False)                

        message = "Applicant has had previous employment. Applicant has had no criminal records."

        self.assertEqual((PASS, message), process_applicant(application, self.employment_criteria, self.criminal_records))

    def test_process_applicant_takes_an_application_and_employment_fail_and_criminal_records_pass_criterias_and_fails_overall(self):
        application = Application(employment_status = False, criminal_records = False)

        message = "Applicant has no previous employment. Applicant has had no criminal records."

        self.assertEqual((FAIL, message), process_applicant(application, self.employment_criteria, self.criminal_records))

    def test_process_applicant_takes_an_application_and_employment_pass_and_criminal_records_fail_criterias_and_fails_overall(self):
        application = Application(employment_status = True, criminal_records = True)

        message = "Applicant has had previous employment. Applicant has criminal records."

        self.assertEqual((FAIL, message), process_applicant(application, self.employment_criteria, self.criminal_records))
