import json
from math import radians, acos, sin, cos


def fetch_customers(filename):
    if not filename:
        return []

    customers = []
    with open(filename) as fp:
        customer = fp.readline()

        while customer:
            customers.append(json.loads(customer))
            customer = fp.readline()

    return customers


def sort_customers(customers_data):
    if not customers_data:
        return []

    customers_data = sorted(customers_data, key=lambda i: i['user_id'], reverse=False)
    return customers_data


def calculate_distance(source_coordinates, destination_coordinates):
    # Radius of earth (KM)
    R = 6373.0

    # Latitude and Longitude of Dublin office from given link
    office_lat, office_long = radians(float(source_coordinates['latitude'])), radians(float(source_coordinates['longitude']))

    customer_lat = radians(float(destination_coordinates['latitude']))
    customer_long = radians(float(destination_coordinates['longitude']))
    # Calculating distance in KM
    distance = R * acos(
        sin(office_lat) * sin(customer_lat) + cos(office_lat) * cos(customer_lat) * cos(office_long - customer_long))

    # adding the calculated distance in dict, rounding the result upto two decimal points
    return round(distance, 2)


def create_new_file(filename, customers):
    if not customers:
        return False

    with open(filename, 'w+') as fp:
        for cust in customers:
            if int(cust['distance_in_km']) <= 100:
                fp.write(json.dumps(cust) + '\n')

    return True

