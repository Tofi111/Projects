import requests

def get_response(cityname):
    return requests.get(f"http://worldtimeapi.org/api/timezone/Europe/{cityname}").json()

def get_raw_offset(cityname):
    return get_response(cityname)['raw_offset']


