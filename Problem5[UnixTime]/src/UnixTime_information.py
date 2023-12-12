import requests


def get_response():
    return requests.get('http://worldtimeapi.org/api/ip.txt').text
def get_unixtime():
    lines = get_response().split('\n')

    unixtime_line = next((line for line in lines if 'unixtime' in line), None)
    if unixtime_line:

        _, unixtime_value = unixtime_line.split(':')
        return unixtime_value.strip()
    else:
        print("Error: 'unixtime' not found in the response")
        return None
