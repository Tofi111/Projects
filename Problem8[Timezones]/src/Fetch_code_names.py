def fetch_code_name():
    with open('Timezones', 'r') as file:
        codes = [line.strip() for line in file.readlines()]

    return codes
