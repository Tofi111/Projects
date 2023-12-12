import requests


def get_response():
    try:
        return requests.get('http://worldtimeapi.org/api/ip.txt').text
    except requests.exceptions.RequestException as e:
        handle_error(e)

def get_error_message(e):
    return f"Error: {e}"

def handle_error(e):
    print(get_error_message(e))
