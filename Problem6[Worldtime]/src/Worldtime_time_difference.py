from worldtime_raw_offset import get_raw_offset


def calculate_time_difference(city_name):
    times = []
    for i in city_name:
        try:
            times.append(get_raw_offset(i) // 3600)
        except Exception as e:
            print(f"{i.ljust(10)} {"Err".rjust(4)}")

    return times
