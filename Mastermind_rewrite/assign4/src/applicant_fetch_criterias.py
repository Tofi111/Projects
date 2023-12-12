import importlib
import pkgutil


def fetch_a_criterion(criteria):
    module = importlib.import_module(f"src.evaluators.evaluate_{criteria.lower().replace(' ', '_')}")

    return getattr(module, "evaluate_applicant")


def fetch_criterias():
    module = importlib.import_module("src.evaluators")

    return [process_name(name) for _, name, _ in pkgutil.iter_modules([module.__path__[0]])]


def process_name(name):
    return str(name.replace("evaluate_", '').replace('_', ' '))
