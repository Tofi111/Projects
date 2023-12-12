import requests

from Error_message_processor import handle_error
from UnixTime_information import get_unixtime

def main():
    print("Fetching world time information...\n")
    try:
        unix_time = get_unixtime()
        print(f"Unix time is {unix_time}")
    except requests.exceptions.RequestException as e:
        handle_error(e)
main()
