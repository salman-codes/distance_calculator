import configparser
from util import fetch_customers, calculate_distance, sort_customers, create_new_file
from test import test_distance_calculator


if __name__ == '__main__':
    """ Reading the source coordinates from config file """
    config = configparser.ConfigParser()
    config.read('config.ini')

    """ To run the test cases - Uncomment below line """
    test_distance_calculator(source_coordinates=config['source_coordinates'])

    customers = fetch_customers(filename='customers.txt')
    customers_new_data = []
    for customer in customers:
        customer['distance_in_km'] = calculate_distance(
            source_coordinates=config['source_coordinates'], destination_coordinates=customer
        )
        customers_new_data.append(customer)

    customers_new_data = sort_customers(customers_data=customers_new_data)

    if create_new_file(filename='output.txt', customers=customers_new_data):
        print('New File Created (Includes Distance)!')
    else:
        print('Error in creating file!')
