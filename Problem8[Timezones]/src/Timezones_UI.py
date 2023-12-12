from src.Fetch_code_names import fetch_code_name
from src.Timezones_date_and_time import get_date, get_time
from src.Timezones_name import get_timezone_name

def display_Timezones():
    print(f"{'code'.ljust(10)}{'Timezone'.ljust(20)}{'Date'.rjust(13)}{'Time'.rjust(10, ' ')}")

    for code in fetch_code_name():
        if get_timezone_name(code) is not None and get_date(code) is not None:
            print(f"{code.ljust(10)}{get_timezone_name(code).rjust(20)}  {get_date(code).rjust(10, ' ')} {get_time(code).rjust(10, ' ')}")
        else:
            print(f"{code} Error: invalid timezone code")


display_Timezones()
