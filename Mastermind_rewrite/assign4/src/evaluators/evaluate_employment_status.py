from src.response import *


def evaluate_applicant(application):
    return (PASS, "Applicant has had previous employment.") \
        if application.employment_status else (FAIL, "Applicant has no previous employment.")
