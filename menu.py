# Heather Smith Student ID: 001266423

from packages import get_hash_map
import datetime

#Prints the timestamp for each package
#Space-time complexity O(N)
def print_timestamp():
    try:
        status_time = input('Please enter a time in the HH:MM:SS format: ')
        (h, m, s) = status_time.split(':')
        convert_user_time = datetime.timedelta(hours= int(h), minutes= int(m), seconds= int(s))
        # Space-time complexity is O(N)
        for count in range(1,41):
            first_time = get_hash_map().get_value(str(count))[9]
            second_time = get_hash_map().get_value(str(count))[10]
            (h,m,s) = first_time.split(':')
            convert_first_time = datetime.timedelta(hours= int(h), minutes= int(m), seconds=int(s))
            if second_time != 'At hub':
                (h, m, s) = second_time.split(':')
                convert_second_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            else:
                convert_second_time = datetime.timedelta(hours=0, minutes=0, seconds=0)

            # First checks all packages against the given time determine if they have left the hub yet.
            print_packages(convert_user_time, first_time, convert_first_time, second_time, convert_second_time, count)
    except IndexError:
        print(IndexError)
        exit()
    except ValueError:
        print('Invalid entry!')
        exit()

#Prints the timestamp for package id entered by user
#Space-time complexity O(1)
def search_by_id():
    try:
        count = input('Please enter a package ID to lookup: ')
        first_time = get_hash_map().get_value(count)[9]
        second_time = get_hash_map().get_value(count)[10]
        status_time= input('Please enter a time in the HH:MM:SS format: ')
        (h, m, s) = status_time.split(':')
        convert_user_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        (h, m, s) = first_time.split(':')
        convert_first_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        (h, m, s) = second_time.split(':')
        convert_second_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        print_packages(convert_user_time, first_time, convert_first_time, second_time, convert_second_time, count)
    except ValueError:
        print('Invalid entry')

#Prints timestamp of packages that match the users input for address
#Space-time Complexity of O(N)
def search_by_address():
    try:
        address = input('Please enter the delivery address: ')
        
        status_time = input('Please enter a time in HH:MM:SS format: ')
        (h, m, s) = status_time.split(':')
        convert_user_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        for count in range(1,41):
            delivery_address = str(get_hash_map().get_value(str(count))[2])+ ' ' + str(get_hash_map().get_value(str(count))[3]) + ' ' + str(get_hash_map().get_value(str(count))[4])+ ' ' + str(get_hash_map().get_value(str(count))[5])
            if address in delivery_address:
                first_time = get_hash_map().get_value(str(count))[9]
                second_time = get_hash_map().get_value(str(count))[10]
                (h,m,s) = first_time.split(':')
                convert_first_time = datetime.timedelta(hours= int(h), minutes= int(m), seconds=int(s))
                if second_time != 'At hub':
                    (h, m, s) = second_time.split(':')
                    convert_second_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                else:
                    convert_second_time = datetime.timedelta(hours=0, minutes=0, seconds=0)

                # First checks all packages against the given time determine if they have left the hub yet.
                print_packages(convert_user_time, first_time, convert_first_time, second_time, convert_second_time, count)
    except ValueError:
        print('Incorrect Input.')

#Prints timestamp of packages whose deadline matches the users input
#Space-time Complexity O(N)
def search_by_deadline():
    deadline = input('Please enter delivery by time in HH:MM AM/PM format: ')
    new_time = deadline.upper()
    status_time = input('Please enter a time in HH:MM:SS format: ')
    (h, m, s) = status_time.split(':')
    convert_user_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    # Space-time complexity is O(N)
    for count in range(1,41):
        delivery_deadline = str(get_hash_map().get_value(str(count))[6])
        
        if new_time in delivery_deadline:
            first_time = get_hash_map().get_value(str(count))[9]
            second_time = get_hash_map().get_value(str(count))[10]
            (h,m,s) = first_time.split(':')
            convert_first_time = datetime.timedelta(hours= int(h), minutes= int(m), seconds=int(s))
            if second_time != 'At hub':
                (h, m, s) = second_time.split(':')
                convert_second_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            else:
                convert_second_time = datetime.timedelta(hours=0, minutes=0, seconds=0)

            # First checks all packages against the given time determine if they have left the hub yet.
            print_packages(convert_user_time, first_time, convert_first_time, second_time, convert_second_time, count)

#Prints the timestamps of packages that matches the users input
#Space-time Complexity O(N)
def search_by_city():
    city = input('Please enter city: ')
    status_time = input('Please enter a time in HH:MM:SS format: ')
    (h, m, s) = status_time.split(':')
    convert_user_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    # Space-time complexity is O(N)
    for count in range(1,41):
        delivery_city = str(get_hash_map().get_value(str(count))[3])
        
        if city in delivery_city:
            first_time = get_hash_map().get_value(str(count))[9]
            second_time = get_hash_map().get_value(str(count))[10]
            (h,m,s) = first_time.split(':')
            convert_first_time = datetime.timedelta(hours= int(h), minutes= int(m), seconds=int(s))
            if second_time != 'At hub':
                (h, m, s) = second_time.split(':')
                convert_second_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            else:
                convert_second_time = datetime.timedelta(hours=0, minutes=0, seconds=0)

            # First checks all packages against the given time determine if they have left the hub yet.
            print_packages(convert_user_time, first_time, convert_first_time, second_time, convert_second_time, count)

#Prints timestamp of packages that zipcode matches user input
#Space-time Complexity O(N)
def search_by_zip():
    zipcode = int(input('Please enter zipcode: '))
    status_time = input('Please enter a time in HH:MM:SS format: ')
    try:
        (h, m, s) = status_time.split(':')
        convert_user_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        # Space-time complexity is O(N)
        for count in range(1,41):
            delivery_zip = int(get_hash_map().get_value(str(count))[5])
            
            if zipcode == delivery_zip:
                first_time = get_hash_map().get_value(str(count))[9]
                second_time = get_hash_map().get_value(str(count))[10]
                (h,m,s) = first_time.split(':')
                convert_first_time = datetime.timedelta(hours= int(h), minutes= int(m), seconds=int(s))
                if second_time != 'At hub':
                    (h, m, s) = second_time.split(':')
                    convert_second_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                else:
                    convert_second_time = datetime.timedelta(hours=0, minutes=0, seconds=0)

                # First checks all packages against the given time determine if they have left the hub yet.
                print_packages(convert_user_time, first_time, convert_first_time, second_time, convert_second_time, count)
    except ValueError:
        print('Please enter a zipcode.')

#Prints timestamp of packages that weight matches user input
#Space-time Complexity O(N)
def search_by_weight():
    weight = input('Please enter package weight: ')
    status_time = input('Please enter a time in HH:MM:SS format: ')
    (h, m, s) = status_time.split(':')
    convert_user_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    # Space-time complexity is O(N)
    for count in range(1,41):
        delivery_weight = str(get_hash_map().get_value(str(count))[7])
        
        if weight in delivery_weight:
            first_time = get_hash_map().get_value(str(count))[9]
            second_time = get_hash_map().get_value(str(count))[10]
            (h,m,s) = first_time.split(':')
            convert_first_time = datetime.timedelta(hours= int(h), minutes= int(m), seconds=int(s))
            if second_time != 'At hub':
                (h, m, s) = second_time.split(':')
                convert_second_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            else:
                convert_second_time = datetime.timedelta(hours=0, minutes=0, seconds=0)

            # First checks all packages against the given time determine if they have left the hub yet.
            print_packages(convert_user_time, first_time, convert_first_time, second_time, convert_second_time, count)

#Prints timestamp of packages whose's status matches the user's input
#Space-time Complexity O(N)
def search_by_status():
    status = input('Please enter delivery status: ')
    status = status.lower()
    status_time = input('Please enter a time in HH:MM:SS format: ')
    (h, m, s) = status_time.split(':')
    convert_user_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    # Space-time complexity is O(N)
    for count in range(1,41):
        first_time = get_hash_map().get_value(str(count))[9]
        second_time = get_hash_map().get_value(str(count))[10]
        (h,m,s) = first_time.split(':')
        convert_first_time = datetime.timedelta(hours= int(h), minutes= int(m), seconds=int(s))
        (h, m, s) = second_time.split(':')
        convert_second_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

        if  convert_first_time < convert_user_time and  convert_user_time >= convert_second_time:
            delivery_status = 'delivered'
        elif convert_user_time > convert_first_time and convert_user_time < convert_second_time:
            delivery_status = 'in transit'
        else:
            delivery_status = 'at hub'
        if status in delivery_status:
            # First checks all packages against the given time determine if they have left the hub yet.
            print_packages(convert_user_time, first_time, convert_first_time, second_time, convert_second_time, count)

#Prints packages 
#Space-time Complexity O(1)
def print_packages(convert_user_time, first_time, convert_first_time, second_time, convert_second_time, count):
    if convert_first_time <= convert_user_time:
        change_address_time = datetime.timedelta(hours=10, minutes=20, seconds=0)
        if convert_user_time >= change_address_time:
            get_hash_map().get_value(str(9))[2] = '410 S State St' 
            get_hash_map().get_value(str(9))[3] = 'Salt Lake City'
            get_hash_map().get_value(str(9))[4] = 'UT' 
            get_hash_map().get_value(str(9))[5] = '84111'
            # Then checks if the package has left the hub but has not been delivered yet
        if convert_user_time < convert_second_time:
            print('Package ID:', get_hash_map().get_value(str(count))[0], '\nStreet address:',
                get_hash_map().get_value(str(count))[2], get_hash_map().get_value(str(count))[3],
                get_hash_map().get_value(str(count))[4], get_hash_map().get_value(str(count))[5],
                '\nRequired delivery time:', get_hash_map().get_value(str(count))[6],
                '\nPackage weight:', get_hash_map().get_value(str(count))[7], '\nTruck status: Left at',
                get_hash_map().get_value(str(count))[9], '\nDelivery status: In transit\n')
        else:
            print('Package ID:', get_hash_map().get_value(str(count))[0], '\nStreet address:',
            get_hash_map().get_value(str(count))[2], get_hash_map().get_value(str(count))[3],
            get_hash_map().get_value(str(count))[4], get_hash_map().get_value(str(count))[5],
            '\nRequired delivery time:', get_hash_map().get_value(str(count))[6],
            '\nPackage weight:', get_hash_map().get_value(str(count))[7], '\nTruck status: Left at ',
            get_hash_map().get_value(str(count))[9], '\nDelivery status: Delivered at',
            get_hash_map().get_value(str(count))[10], '\n') 
    else:
        print('Package ID:', get_hash_map().get_value(str(count))[0], '\nStreet address:',
            get_hash_map().get_value(str(count))[2], get_hash_map().get_value(str(count))[3],
            get_hash_map().get_value(str(count))[4], get_hash_map().get_value(str(count))[5],
            '\nRequired delivery time:', get_hash_map().get_value(str(count))[6],
            '\nPackage weight:', get_hash_map().get_value(str(count))[7], '\nTruck status: Leaves at',
            get_hash_map().get_value(str(count))[9], '\nDelivery status: At hub\n')
