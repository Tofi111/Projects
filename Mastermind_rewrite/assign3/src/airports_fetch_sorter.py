import importlib
import pkgutil

def fetch_a_sorter(criteria):
	module = importlib.import_module(f"src.airport_sorters.sort_by_{criteria.lower().replace(' ', '_')}")
	
	return getattr(module, "sort_by_criteria")

def fetch_sort_criteria():
	module = importlib.import_module("src.airport_sorters")

	return [process_name(name) for _, name, _ in pkgutil.iter_modules([module.__path__[0]])]

def process_name(name):
	return str(name.replace("sort_by_", '').replace('_', ' '))
