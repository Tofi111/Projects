from src.response import *


def evaluate_applicant(application):
    return (FAIL, "Applicant has criminal records.") \
        if application.criminal_records else (PASS, "Applicant has had no criminal records.")
