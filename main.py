import sys
from admin import *


def main():
    print('this is in  main')

    admin_loggedin = False

    while(1):
        cmd = input('Enter command')
        if cmd == 'admin':
            if not admin_loggedin:
                user = input("Enter admin username")
                password = input('Enter admin password:')
                admin_loggedin = admin_login(user, password)
            else:
                # Can edit users and stuff here
                print('')
        elif cmd == 'Edit':
            print('Use this to add/edit/remove patient data')
        elif cmd == 'View':
            print('Use this option to view a patient"s data')
        
        else:
            print('Please etner a valid command')



if __name__ == "__main__":
    main()