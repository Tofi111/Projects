def fetch_city_name(filename):
    with open(filename, 'r') as file:
        city_names = [line.strip() for line in file.readlines()]

    return city_names

