import sys
import os
import AES
import getpass
from db import *

DB_NAME = '"encrypted_patients"'
KEY = [0x54, 0x68, 0x61, 0x74, 0x73, 0x20, 0x6D, 0x79, 0x20, 0x4B, 0x75, 0x6E, 0x67, 0x20, 0x46, 0x75]

def main():

    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_db_file>")
        sys.exit(1)

    db_file = sys.argv[1]

    # Check if the file exists
    while not os.path.exists(db_file):
        print("File does not exist. Please check the path.")
        input('Enter a new database file path: ')

    loggedin = False

    db = Mimic_DB(db_file)
    roundkeys = AES.generate_roundkeys(KEY)

    while(1):
        try:
            cmd = input('Enter command: ')
        except KeyboardInterrupt:
            print("\nCtrl+C detected. Exiting...")
            exit()
        if cmd == 'login':
            username = input('Username: ')
            password = getpass.getpass('Password: ')

            e_user = AES.encrypt(username.encode('ascii'), roundkeys)
            e_pass = AES.encrypt(password.encode('ascii'), roundkeys)

            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (e_user, e_pass))
            rows = cursor.fetchall()

            if len(rows) == 0:
                print('Invalid login')
            else:
                print('Login successful')
                loggedin = True

        elif cmd == 'edit':
            if loggedin:

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

                db.edit(roundkeys, DB_NAME, filter_cols, filter_vals, edit_cols, edit_vals)
            else:
                print('Login to edit database')

        elif cmd == 'view':
            if loggedin:
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
                rows = db.search(roundkeys, DB_NAME, columns, values)
                for row in rows:
                    print(row)
            else:
                print('Please login to view database')

        elif cmd == 'logout':
            loggedin=False
            print('Successfully logged out')
            
        elif cmd == 'help':
            print("\u0332".join("Command List: "))
            print('''                           
login: Use the user databse to access the record data

view: use filter(s) to fetch patient data
    
edit: use filter(s) to edit value(s)

exit: logout and quit the application 
            ''')
            print("\u0332".join("Available Fields: "))

            print('''
subject_id: unique identifier which specifies an individual patient
gender: genotypical sex of the patient
anchor_age: patient’s age in the anchor_year
anchor_year: shifted year for the patient
anchaor_year_group: range of years - the patient’s anchor_year occurred during this range
ded
                  
Reference: https://mimic.mit.edu/docs/iv/modules/hosp/patients/
            ''')
        elif cmd == 'exit':
            db.close()
            print('Have a nice day!')
            break

        # Used for debugging only!
        elif cmd == 'c':
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
            db.table_transfer(roundkeys, '"hosp/patients"', columns, values, 'encrypted_patients')
          
        else:
            print('Please etner a valid command')


if __name__ == "__main__":
    main()