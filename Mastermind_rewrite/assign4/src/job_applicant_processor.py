from src.response import *
from functools import reduce

SPACE = ' '


def process_applicant(application, *evaluate_criterias):
    return (PASS, 'Nothing to check') if evaluate_criterias == () \
        else reduce(merge_results, [evaluate(application) for evaluate in evaluate_criterias])


def merge_results(result1, result2):
    (response1, message1), (response2, message2) = result1, result2

    return PASS if response1 == response2 == PASS else FAIL, f"{message1} {message2}".strip()
