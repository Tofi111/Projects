import requests


def get_raw_offset(worldtime_raw_offset):
    try:
        return worldtime_raw_offset()
    except requests.exceptions.RequestException as e:
        return 'ERR'
    except Exception as e:
        return '---'
