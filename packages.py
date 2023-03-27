# Heather Smith Student ID: 001266423

import csv
from hashtable import HashTable

#Creates object for the hashtable
insert_hash_map = HashTable()

#Lists represent both trucks and first_truck's second trip
first_truck = []
second_truck = []
first_truck_reload = []

#Reads and iterates through the csv file
with open('WGUPS_Package_File.csv', newline='') as file:
    package = csv.reader(file, delimiter=',')

    for row in package:
        package_id = row[0]
        address = row[1]
        city = row[2]
        state = row[3]
        zipcode = row[4]
        delivery_time = row[5]
        package_weight = row[6]
        notes = row[7]
        delivery_start = ''
        address_location = ''
        delivery_status = 'At hub'

        package_info = [package_id, address_location, address, city, state, zipcode, delivery_time, package_weight, notes, delivery_start, delivery_status]

        #Sets the key and value for the hashmap
        key = package_id
        value = package_info
            
        #If/else statement appends packages to appointed lists
        if notes == 'None':
            if '4580 S 2300 E' in address or '5383 South 900 East #104' in address:
                first_truck.append(value)
            if '3595 Main St' in address or '177 W Price Ave' in address:
                first_truck.append(value)
            if '2530 S 500 E' in address:
                first_truck_reload.append(value)
            if '1330 2100 S' in address or '380 W 2880 S' in address:
                second_truck.append(value)
            if '84104' in zipcode:
                first_truck.append(value)
            if '84103' in zipcode or '84111' in zipcode or '84118' in zipcode or '84121' in zipcode:
                second_truck.append(value)
            if '3365 S 900 W' in address:
                first_truck_reload.append(value)
            if '3575 W Valley Central Station bus Loop' in address:
                first_truck.append(value)
            if '84107' in zipcode:
                first_truck.append(value)
            if '600 E 900 South' in address:
                first_truck_reload.append(value)
            if '3148 S 1100 W' in address:
                second_truck.append(value)
            if '195 W Oakland Ave' in address:
                first_truck.append(value)
        else:
            if 'truck 2' in notes:
                second_truck.append(value)
            if 'Delayed' in notes:
                first_truck_reload.append(value)
            if 'Wrong address' in notes:
                first_truck_reload.append(value)
            if 'Must be delivered' in notes:
                first_truck.append(value)

        #Insert key value into hashtable   
        insert_hash_map.insert(key,value)

#Returns the hashmap
#O(1) complexity
def get_hash_map():
    return insert_hash_map
#Returns the list of the first truck
#O(1) complexity
def get_first_truck():
    return first_truck
 #Returns the list of the second truck
 #O(1) complexity   
def get_second_truck():
    return second_truck
#Returns the list of the first truck reload  
#O(1) complexity
def get_first_truck_reload():
    return first_truck_reload
        
            

