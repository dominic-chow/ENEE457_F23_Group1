# This file will be used to manage database access/editing
# Probably using SQLite3 and JSON? subject to change

# Figure out a way to manage keys/salts

# https://physionet.org/content/mimiciv/2.2/hosp/patients.csv.gz
# This should be what's inside the mimic4.db database

import sqlite3
import patient

class Mimic_DB:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None
        self.cursor = None
        try:
            self.connection = sqlite3.connect(self.db_file)
            self.cursor = self.connection.cursor()
            print(f"Connected to the database: {self.db_file}")
        except sqlite3.Error as e:
            print(f"Error connecting to the database: {e}")

    def edit(self, roundkey, table, f_col, f_val, e_col, e_val):
        query_str = 'UPDATE {} '.format(table)

        # Appebd new values to query
        for i in range(len(e_col)):
            if i == 0:
                query_str += 'SET '
            else:
                query_str += ', '
            query_str += '{} = ?'.format(e_col[i])

        # Append filter values
        for i in range(len(f_col)):
            if i == 0:
                query_str += ' WHERE '
            else:
                query_str += ' AND '
            query_str += '{} = ?'.format(f_col[i])

        print(query_str)
        print(tuple(patient.encrypt(roundkey,  e_val) + patient.encrypt(roundkey, f_val)))
        self.cursor.execute(query_str, tuple(patient.encrypt(roundkey,  e_val) + patient.encrypt(roundkey, f_val)))
        self.connection.commit()

    def search(self, roundkeys, table, columns, values):

        # Encrypt the search filters
        encrypted_search = patient.encrypt(roundkeys, values)

        # Search the values with the encrypted filters
        search_str = 'SELECT * FROM {} '.format(table)
        for i in range(len(columns)):
            if i == 0:
                search_str += 'WHERE '
            else:
                search_str += ' AND '
            search_str += '{} = ?'.format(columns[i])
        self.cursor.execute(search_str, encrypted_search)
        rows = self.cursor.fetchall()

        # Decrypt the found encrypted rows
        decrypted_rows = []
        for row in rows:
            decrypted_rows.append(patient.decrypt(roundkeys, row))

        return decrypted_rows

    # Debugging method used to create an encrypted table    
    def table_transfer(self, roundkeys, table, columns, values, new_table):
        # Search the decrypted values
        search_str = 'SELECT * FROM {} '.format(table)
        for i in range(len(columns)):
            if i == 0:
                search_str += 'WHERE '
            else:
                search_str += ' AND '
            search_str += '{} = ?'.format(columns[i])
        self.cursor.execute(search_str, values)
        rows = self.cursor.fetchall()

        # Create an ecrypted table
        conn = sqlite3.connect('encrypted_mimic.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS encrypted_patients (
                subject_id BLOB,
                gender BLOB,
                anchor_age BLOB,
                anchor_year BLOB,
                anchor_year_group BLOB,
                dod BLOB
            )
        ''')
        # Done creating encrypted table
        for row in rows:
            # print(row)
            encrypted = patient.encrypt(roundkeys, row)
            # print(encrypted)
            cursor.execute('INSERT INTO encrypted_patients VALUES (?, ?, ?, ?, ?, ?)', encrypted)
            conn.commit()
        cursor.close()
        conn.close()

    def close(self):
        self.cursor.close()
        self.connection.close()