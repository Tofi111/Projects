import unittest
from src.applicant_fetch_criterias import *
from src.application_info import *
from src.response import *

class FetchCriterionTests(unittest.TestCase):
    def test_fetch_criterion_gets_criteria_given_name_as_employment_status(self):
        expected_criteria = fetch_a_criterion('employment status')

        self.assertEqual((PASS, "Applicant has had previous employment."), expected_criteria(Application(employment_status = True)))

    def test_fetch_criterion_gets_criteria_given_name_as_criminal_records(self):
        expected_criteria = fetch_a_criterion('criminal records')

        self.assertEqual((PASS, "Applicant has had no criminal records."), expected_criteria(Application(employment_status = True)))

    def test_fetch_criterias_returns_all_criterias_employment_status_included(self):
    	self.assertTrue('employment status' in fetch_criterias())

    def test_fetch_criterias_returns_all_criterias_criminal_records_included(self):
    	self.assertTrue('criminal records' in fetch_criterias())
