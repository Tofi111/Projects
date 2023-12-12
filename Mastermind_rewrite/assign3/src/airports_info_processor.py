from dataclasses import replace

def process_airports(airports, sort_by_criteria=lambda airports: airports):
    return sort_by_criteria([convert_name_to_uppercase(airport) for airport in airports])

def convert_name_to_uppercase(airport):
    return replace(airport, Name=airport.Name.upper())
