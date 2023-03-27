# Heather Smith Student ID: 001266423

from deliveries import total_distance
from menu import search_by_id
from menu import search_by_address
from menu import search_by_deadline
from menu import search_by_city
from menu import search_by_zip
from menu import search_by_weight
from menu import search_by_status
from menu import print_timestamp

def main():
    try :
        # This is the display message that is shown when the user runs the program. The interface is accessible from here
        print('Welcome to the WGUPS package tracking system...')
        print('Current route was completed in', '{0:.2f}'.format(total_distance()),' miles.')
        start = 1
        while start != 0:   
            start = int(input('\nPress 1 to lookup package \n'
                        'Press 2 for timestamps    \n'
                        'Press 0 to exit           \n'))           
            # if user types 'timestamp' then they are prompted for a time to display. Once a time is provided it will
            # display all packages at that timestamp. Runtime of this process is O(N)
            if start == 1:
                search = int(input( 'Press 1 to search by ID \n'
                                'Press 2 to search by delivery address \n'
                                'Press 3 to search by delivery deadline \n'
                                'Press 4 to search by delivery city \n'
                                'Press 5 to search by delivery zip code \n'
                                'Press 6 to search by package weight \n'
                                'Press 7 to search by delivery status\n'))
                
                if search == 1:
                    search_by_id()
                elif search == 2:
                    search_by_address()
                elif search == 3:
                    search_by_deadline()
                elif search == 4:
                    search_by_city()
                elif search == 5:
                    search_by_zip()
                elif search == 6:
                    search_by_weight()
                elif search == 7:
                    search_by_status()
                
            # If 'lookup' is selected than the user is prompted for a package ID followed by a timestamp
            # Once that information is enter1ed then the user will be shown a particular package at a given time
            elif start == 2:
                print_timestamp()
        #User has entered 0 and exits from the program
        exit()
    except ValueError:
        print('Incorrect response.')
if __name__ == '__main__':
    main()
            
    
    