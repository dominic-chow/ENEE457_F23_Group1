import sys
import os
from admin import *
from db import *

DB_NAME = '"hosp/patients"'

def main():

    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)

    db_file = sys.argv[1]

    # Check if the file exists
    if os.path.exists(db_file):
        print("File exists!")
    else:
        print("File does not exist. Please check the path.")

    admin_loggedin = False

    db = Mimic_DB(db_file)

    while(1):
        cmd = input('Enter command: ')
        if cmd == 'admin':
            if not admin_loggedin:
                user = input("Enter admin username")
                password = input('Enter admin password:')
                admin_loggedin = admin_login(user, password)
            else:
                # Can edit users and stuff here
                print('')
        elif cmd == 'edit':
            # Use this to edit a patient in the database
            print('Use this to add/edit/remove patient data')

            filter = ''
            filter_cols = []
            filter_vals = []
            edit_cols = []
            edit_vals = []

            print('Enter filters as <Column>=<Value>')
            print('Type done when finished')
            while filter != 'done':
                filter = input('> ')
                if filter == 'done':
                    break
                split_res = filter.split('=')
                filter_cols.append(split_res[0])
                filter_vals.append(split_res[1])

            filter = ''
            print('Enter new values as <Column>=<Value>')
            print('Type done when finished')
            while filter != 'done':
                filter = input('> ')
                if filter == 'done':
                    break
                split_res = filter.split('=')
                edit_cols.append(split_res[0])
                edit_vals.append(split_res[1])

            print(filter_cols)
            print(filter_vals)
            print(edit_cols)
            print(edit_vals)
            db.edit(DB_NAME, filter_cols, filter_vals, edit_cols, edit_vals)


        elif cmd == 'view':
            filter = ''
            columns = []
            values = []
            print('Enter filters as <Column>=<Value>')
            print('Type done when finished')
            while filter != 'done':
                filter = input('> ')
                if filter == 'done':
                    break
                split_res = filter.split('=')
                columns.append(split_res[0])
                values.append(split_res[1])

            # use this access something from the database
            db.search(DB_NAME, columns, values)

        elif cmd == 'exit':
            db.close()
            print('Have a nice day!')
            break
        else:
            print('Please etner a valid command')


if __name__ == "__main__":
    main()