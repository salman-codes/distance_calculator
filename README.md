# Calculate distance between two coordinates in KM
## The util.py file
### 1. fetch_customers(filename)
This function takes _filename_ as argument and loads data from the file, and returns the list of _dict objects_.

Note:- The data in the file should be as shown in customers.txt

### 2. sort_customers(customers_data)
Takes the list of dict objects as argument, sorts the _customers list of dictionary_ in ascending order of _user_id_ present in the file, and returns the new sorted list.

### 3. calculate_distance(source_coordinates, destination_coordinates)
Takes the source and destination coordinates in arguments which are dictionary objects with keys _latitude_ and _longitude_.
Calculates the distance(in KM) between the two using this() formula and returns it.

### 4. create_new_file(filename, customers)
Finally save the new data in new file, sorted by _user_id_.

## The test.py file
### 1. test_distance_calculator()
This function tests the distance calculator logic. 
I've fetched few cities coordinates in _Ireland_ and there distance from _Dublin, Ireland_, and checking if the distnace found from net is the same as calculate by 3rd function i.e _calculate_distance()_.


## How to Run
1. Create a virtual environment by runing _**python -m venv my_virtualenv**_.
2. Install requirement.txt by running _**pip install -r requirement.txt**_.
3. To execute test cases, remove/comment everything below _**line 12**_ in _app.py_ file.
4. Now simply run, _**python app.py**_.
5. The new output will be saved in _output.txt_ file, the output contains customers with less than or equal to 100KM distance from the source.
