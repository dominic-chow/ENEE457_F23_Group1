# This file will be used to manage database access/editing
# Probably using SQLite3 and JSON? subject to change

# Figure out a way to manage keys/salts

# https://physionet.org/content/mimiciv/2.2/hosp/patients.csv.gz
# This should be what's inside the mimic4.db database

import sqlite3

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

    def edit(self, table, f_col, f_val, e_col, e_val):
        query_str = 'UPDATE {} '.format(table)

        for i in range(len(e_col)):
            if i == 0:
                query_str += 'SET '
            else:
                query_str += ', '
            query_str += '{} = ?'.format(e_col[i])

        for i in range(len(f_col)):
            if i == 0:
                query_str += ' WHERE '
            else:
                query_str += ' AND '
            query_str += '{} = ?'.format(f_col[i])

        print(query_str)
        print(tuple(f_val + e_val))
        self.cursor.execute(query_str, tuple(e_val + f_val))
        self.connection.commit()

    def search(self, table, columns, values):
        search_str = 'SELECT * FROM {} '.format(table)
        for i in range(len(columns)):
            if i == 0:
                search_str += 'WHERE '
            else:
                search_str += ' AND '
            search_str += '{} = ?'.format(columns[i])

        self.cursor.execute(search_str, tuple(values))
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)


    def close(self):
        self.cursor.close()
        self.connection.close()