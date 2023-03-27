# Heather Smith Student ID: 001266423

import csv
import datetime

#Reads the WGUPS_Distance_Table_Name.csv and puts the addresses into a list
with open('WGUPS_Distance_Table_Name.csv') as name_file:
    address_file = csv.reader(name_file)
    address_list = list(address_file)
    
#Reads the WGUPS_Distance_Table.csv and puts the distances into a list
with open('WGUPS_Distance_Table.csv') as dist_file:
    distance_file = csv.reader(dist_file)
    distance_file = list(distance_file)

    # these lists represent the sorted trucks that are put in order of efficiency in the function below
    first_opt_truck = []
    first_truck_index_list = []
    second_opt_truck = []
    second_truck_index_list = []
    third_opt_truck = []
    third_truck_index_list = []

    first_truck_index_list.insert(0, '0')
    second_truck_index_list.insert(0, '0')
    third_truck_index_list.insert(0, '0')

    #This function takes the row and column number from the distance_file
    # and will calculate and return the distance. The space-time complexity is O(1) 
    def check_distance(row_value, column_value, distance_sum):
        distance = distance_file[row_value][column_value]
        if distance == '':
            distance = distance_file[column_value][row_value]
        distance_sum += float(distance)

        return distance_sum

    #This function takes the row and column value and returns the current distance.
    #Space-time complexity is O(1)
    def current_distance(row_value, column_value):
        distance = distance_file[row_value][column_value]
        if distance == '':
            distance = distance_file[column_value][row_value]
        return float(distance)
    
    #This is the times that the trucks leave the hub
    first_truck_time = ['8:00:00']
    second_truck_time = ['8:00:00']
    truck_reload_time = ['09:45:00']

    #This function returns the total distance of truck 1.
    #The space-time complexity is O(N)
    def first_truck_time_func(distance):
        check_time = distance / 18
        dist_minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(check_time * 60, 60))
        total_time = dist_minutes + ':00'
        first_truck_time.append(total_time)
        sum = datetime.timedelta()
        for i in first_truck_time:
            (h,m,s) = i.split(':')
            dt = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            sum += dt
        return sum
    
    #Returns the total distance of truck 2.
    #The space-time complexity is O(N)
    def second_truck_time_func(distance):
        check_time = distance / 18
        dist_minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(check_time * 60, 60))
        total_time = dist_minutes + ':00'
        second_truck_time.append(total_time)
        sum = datetime.timedelta()
        for i in second_truck_time:
            (h,m,s) = i.split(':')
            dt = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            sum += dt
        return sum
    
    #Returns the total distance of truck 3.
    #The space-time complexity is O(N)
    def third_truck_time_func(distance):
        check_time = distance / 18
        dist_minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(check_time * 60, 60))
        total_time = dist_minutes + ':00'
        truck_reload_time.append(total_time)
        sum = datetime.timedelta()
        for i in truck_reload_time:
            (h,m,s) = i.split(':')
            dt = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            sum += dt
        return sum

    #Returns the time oject to use in package file.
    #Space-time complexity is O(1)
    def get_address():
        return address_list
    

    # This is my sorting algorithm that uses a greedy approach to automate optimizing the delivery route for each truck.
    # the function takes 3 parameters 
    # First parameter is the list of packages on a truck that has not been optimized yet
    # The second parameter represents the truck number
    # The third parameter represents the current location that is updated each time a truck moves

    # The base case of the algorithm is stated in the initial if statement. 
    # This breaks the recursion
    # once the input list has a size of 0.
    # It starts by setting a "lowest value" of 50.0 and then uses the check current distance function to loop through
    # every possible point that is currently available to see if there is a lower value. If there is than the lowest
    # value is updated and the search continues. Once it has searched through all possible routes
    # the truck can go given the available packages, it then adds that package object and associated index to
    # new lists. To ensure that the right truck packages are being associated, the second parameter
    # is checked. If the truck truck is being sorted than the optimized delivery path will be associated to the lists
    # first_opt_truck and first_opt_truck_index. Each time these lists are updated, the lowest value is
    # removed from the argument list, truck_distance_list. This will allow us to update current location and recursively
    # call the function. Once the argument list is empty it will return the empty list and the function call will end.

    # The space-time complexity of this algorithm is O(N^2). This is due to the two for loops and the repeated lookup
    # functionality required to determine the lowest possible path then move the truck to that position.

    def sort_packages(truck_distance_list, truck_number, current_location):
        if len(truck_distance_list) == 0:
            return truck_distance_list
        else:
            lowest_value = 10.0
            new_location = 0
            for index in truck_distance_list:
                if current_distance(current_location, int(index[1])) < lowest_value:
                    lowest_value = current_distance(current_location, int(index[1]))
                    new_location = int(index[1])
            for index in truck_distance_list:
                if current_distance(current_location, int(index[1])) == lowest_value:
                    if truck_number == 1:
                        first_opt_truck.append(index)
                        first_truck_index_list.append(index[1])
                        pop_value = truck_distance_list.index(index)
                        truck_distance_list.pop(pop_value)
                        current_location = new_location
                        sort_packages(truck_distance_list, 1, current_location)
                    elif truck_number == 2:
                        second_opt_truck.append(index)
                        second_truck_index_list.append(index[1])
                        pop_value = truck_distance_list.index(index)
                        truck_distance_list.pop(pop_value)
                        current_location = new_location
                        sort_packages(truck_distance_list, 2, current_location)
                    elif truck_number == 3:
                        third_opt_truck.append(index)
                        third_truck_index_list.append(index[1])
                        pop_value = truck_distance_list.index(index)
                        truck_distance_list.pop(pop_value)
                        current_location = new_location
                        sort_packages(truck_distance_list, 3, current_location)
               

    # Space-time complexity is O(1)
    def get_first_opt_truck_index():
        return first_truck_index_list

    # Space-time complexity is O(1)
    def get_first_opt_truck_list():
        return first_opt_truck

    # Space-time complexity is O(1)
    def get_second_opt_truck_index():
        return second_truck_index_list

    # Space-time complexity is O(1)
    def get_second_opt_truck_list():
        return second_opt_truck

    # Space-time complexity is O(1)
    def get_third_opt_truck_index():
        return third_truck_index_list

    # Space-time complexity is O(1)
    def get_third_opt_truck_list():
        return third_opt_truck

    
   
                
        
    
