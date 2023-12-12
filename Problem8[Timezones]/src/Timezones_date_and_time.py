import requests
from datetime import datetime


def get_response(code):
    return requests.get(f'http://worldclockapi.com/api/json/{code}/now').json()

def parse_response(code):
    try:
        Dateandtime = get_response(code)['currentDateTime']
        current_date_time = datetime.strptime(Dateandtime, "%Y-%m-%dT%H:%M%z")
        return current_date_time
    except ValueError as e:
        raise ValueError(f"{code} Error: invalid timezone code") from e


def get_date(code):
    return str(parse_response(code).date())


def get_time(code):
    try:
        return str(parse_response(code).strftime("%H:%M"))
    except ValueError as e:
        raise ValueError(f"{code} Error: getting time for code") from e

