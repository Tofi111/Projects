from src.response import *


def evaluate_applicant(application):
    return (PASS, "Applicant has a credit record.") \
        if application.credit_records else (FAIL, "Applicant has no credit record.")
