from src.applicant_fetch_criterias import *
from src.job_applicant_processor import *
from src.application_info import *
from src.response import *


def main():
    available_criterias = fetch_criterias()

    print_available_criterias(available_criterias)

    selected_criteria_names = get_criteria_names(available_criterias, get_criteria_input())

    while input('To continue press enter or else type exit to terminate: ') != "exit":
        print(evaluate_applicant(create_application(available_criterias), selected_criteria_names))


def print_available_criterias(criterias):
    print('0. no sorting')

    for index in range(0, len(criterias)):
        print(f"{index + 1}. {criterias[index]}")

    print(f'{len(criterias) + 1}. exit')


def get_criteria_input():
    print("Enter criteria numbers from the options above separated by a space (same line):")

    return eval(f"[{input().replace(' ', ',')}]")


def get_criteria_names(available_criterias, criteria_numbers):
    return [] if is_no_sort(criteria_numbers) else [available_criterias[number - 1] for number in criteria_numbers]


def is_no_sort(criteria_numbers):
    return 0 in criteria_numbers


def create_application(criterias):
    return Application(*get_application_data(criterias))


def get_application_data(criterias):
    print("Enter Application Data for each field (type corresponding values and press enter): ")

    return [eval(input(f"{criteria_name} (True/False): ")) for criteria_name in criterias]


def evaluate_applicant(application, criteria_names):
    return process_applicant(application, *get_criterias(criteria_names))


def get_criterias(criteria_names):
    return [fetch_a_criterion(criteria_name) for criteria_name in criteria_names]


main()
