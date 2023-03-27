# Heather Smith Student ID: 001266423

from packages import get_hash_map
from packages import get_first_truck
from packages import get_first_truck_reload
from packages import get_second_truck
from distance import check_distance
from distance import first_truck_time_func
from distance import second_truck_time_func
from distance import third_truck_time_func
from distance import current_distance
from distance import sort_packages
from distance import get_first_opt_truck_index
from distance import get_first_opt_truck_list
from distance import get_second_opt_truck_index
from distance import get_second_opt_truck_list
from distance import get_third_opt_truck_index
from distance import get_third_opt_truck_list

import datetime
import distance

first_delivery = []
second_delivery = []
third_delivery = []
first_truck_distance_list = []
second_truck_distance_list = []
third_truck_distance_list = []

# the times below represent the times that each truck leaves the hub
first_time = '8:00:00'
second_time = '8:00:00'
third_time = '9:45:00'

# the operations below convert the string time into a datetime.timedelta
(h, m, s) = first_time.split(':')
convert_first_time = datetime.timedelta(hours = int(h), minutes = int(m), seconds = int(s))
(h, m, s) = second_time.split(':')
convert_second_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
(h, m, s) = third_time.split(':')
convert_third_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

# for loop updates the delivery status of all packages in truck 1 to when the truck leaves the station
# counter to iterate through for loop
# Space-time complexity is O(N)
i = 0
for value in get_first_truck():
    first_delivery.append(get_first_truck()[i])
    get_first_truck()[i][9] = first_time
    i += 1
    
# this for loop compares the addresses on truck one to the list of addresses and adds the address index to the list
# Space-time complexity is O(N^2)
first_count = 0
for k in first_delivery:
    for j in distance.get_address():
        if k[2] == j[2]:
            first_truck_distance_list.append(j[0])
            first_delivery[first_count][1] = j[0]
    first_count += 1

# calls to the greedy algorithm that sorts the packages in a more efficient order
sort_packages(first_delivery, 1, 0)
first_truck_total_dist = 0

# this for loop takes the values in the first truck and runs them through the distance functions in the distances.py file
# Space-time complexity is O(N)
try:
    first_truck_pack_id = 0
    for index in range(len(get_first_opt_truck_index())):
        # calculate the total distance of the truck
        first_truck_total_dist = check_distance(int(get_first_opt_truck_index()[index]), int(get_first_opt_truck_index()[index + 1]), first_truck_total_dist)
        # calculate the distance of each package along the route
        deliver_package = first_truck_time_func(current_distance(int(get_first_opt_truck_index()[index]), int(get_first_opt_truck_index()[index + 1])))
        get_first_opt_truck_list()[first_truck_pack_id][10] = (str(deliver_package))
        get_hash_map().update(int(get_first_opt_truck_list()[first_truck_pack_id][0]), first_delivery)
        first_truck_pack_id += 1
except:
    pass

# for loop updates the delivery status of all packages in truck 2 to when they leave the station
i = 0  # counter to iterate through for loop
# Space-time complexity is O(N)
for value in get_second_truck():
    get_second_truck()[i][9] = second_time
    second_delivery.append(get_second_truck()[i])
    i += 1
# this for loop compares the addresses on truck two to the list of addresses and adds the address index to the list
# Space-time complexity is O(N^2)
second_count = 0
for k in second_delivery:
    for j in distance.get_address():
        if k[2] == j[2]:
            second_truck_distance_list.append(j[0])
            second_delivery[second_count][1] = j[0]
    second_count += 1

# calls to the greedy algorithm that sorts the packages in a more efficient order
sort_packages(second_delivery, 2, 0)
second_truck_total_dist = 0
# this for loop takes the values in the second truck and runs them through the distance functions in the distances.py file
# Space-time complexity is O(N)
try:
    second_truck_pack_id = 0
    for index in range(len(get_second_opt_truck_index())):
        # calculate the total distance of the truck
        second_truck_total_dist = check_distance(int(get_second_opt_truck_index()[index]), int(get_second_opt_truck_index()[index + 1]), second_truck_total_dist)
        # calculate the distance of each package along the route
        deliver_package = second_truck_time_func(current_distance(int(get_second_opt_truck_index()[index]), int(get_second_opt_truck_index()[index + 1])))
        get_second_opt_truck_list()[second_truck_pack_id][10] = (str(deliver_package))
        get_hash_map().update(int(get_second_opt_truck_list()[second_truck_pack_id][0]), second_delivery)
        second_truck_pack_id += 1
except:
    pass


# for loop updates the delivery status of all packages in truck 1 (second delivery) to 'In transit'
i = 0
# Space-time complexity is O(N)
for value in get_first_truck_reload():
    get_first_truck_reload()[i][9] = third_time
    third_delivery.append(get_first_truck_reload()[i])
    i += 1
# this for loop compares the addresses on truck one (second delivery) to the list of addresses and adds the address index to the list
# Space-time complexity is O(N^2)
third_count = 0
for k in third_delivery:
    for j in distance.get_address():
        if k[2] == j[2]:
            third_truck_distance_list.append(j[0])
            third_delivery[third_count][1] = j[0]
    third_count += 1

# calls to the greedy algorithm that sorts the packages in a more efficient order
sort_packages(third_delivery, 3, 0)
third_truck_total_dist = 0

# this for loop takes the values in the third truck and runs them through the distance functions in the distances.py file
# Space-time complexity is O(N)
third_truck_pack_id = 0
try:
    for index in range(len(get_third_opt_truck_index())):
        
        # calculate the total distance of the truck
        third_truck_total_dist = check_distance(int(get_third_opt_truck_index()[index]), int(get_third_opt_truck_index()[index + 1]), third_truck_total_dist)
        # calculate the distance of each package along the route
        deliver_package = third_truck_time_func(current_distance(int(get_third_opt_truck_index()[index]), int(get_third_opt_truck_index()[index + 1])))
        get_third_opt_truck_list()[third_truck_pack_id][10] = (str(deliver_package))
        get_hash_map().update(int(get_third_opt_truck_list()[third_truck_pack_id][0]), third_delivery)
        third_truck_pack_id += 1
except:
    pass

# function returns total distance of all 3 trips to calculate the distance of all packages
# Space-time complexity is O(1)
def total_distance():
    route_distance = first_truck_total_dist + second_truck_total_dist + third_truck_total_dist
    return route_distance

