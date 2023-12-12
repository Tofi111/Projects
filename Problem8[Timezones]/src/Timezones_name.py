import requests


def get_response(code):
    try:
        response = requests.get(f'http://worldclockapi.com/api/json/{code}/now')
        response.raise_for_status()  # Raise an error for bad HTTP status codes
        return response.json()
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.RequestException as err:
        print(f"Request Error: {err}")
    except requests.exceptions.JSONDecodeError as errj:
        print(f"JSON Decode Error: {errj}")
    return None  # Return None if an error occurs
def get_timezone_name(code):
    return get_response(code)['timeZoneName']


print(get_timezone_name("est"))
