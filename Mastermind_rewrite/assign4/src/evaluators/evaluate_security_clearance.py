from src.response import *


def evaluate_applicant(application):
    return (PASS, "Applicant has security clearance.") \
        if application.security_clearance else (FAIL, "Applicant has no security clearance.")
