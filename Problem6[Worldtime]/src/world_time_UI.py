import sys
from Worldtime_fetch_city_name import fetch_city_name
from Worldtime_time_difference import calculate_time_difference


def display_time_difference(city_names):
    print("Displaying the number of hours difference between the time at a specific location and GMT time ...")

    for city, time in zip(city_names, calculate_time_difference(city_names)):
        print(f"{city.ljust(10)} {str(time).rjust(4)}")


if __name__ == '__main__':
    display_time_difference(fetch_city_name(sys.argv[1]))


