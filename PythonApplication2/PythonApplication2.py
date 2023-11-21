import os
import mysql.connector
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class FileManagement:
    def __init__(self):
        self.mydb = None
        self.cursor = None
        try:
            self.mydb = mysql.connector.connect(
                host='localhost',  # host parameter
                user='root',
                password='Supernatural_2006',
                database='file_management_systemsdb'
            )
            self.cursor = self.mydb.cursor()
            print("Database connection established.")  # Logging for successful connection
        except mysql.connector.Error as err:
            print(f"Database Connection Error: {err}")
            if self.mydb is not None:
                self.mydb.close()  # Close connection if partially established


    def accept_fileinformation(self):
        try:
            fileID = int(input('Enter FileID: '))
            filename = input('Enter File Name: ')
            filesize = float(input('Enter file size in MB: '))
            lastmodifieddate = input('Enter last modified date [YYYY-MM-DD]: ')
            lastaccesseddate = input('Enter last accessed date [YYYY-MM-DD]: ')
            filetype = input('Enter file type: ')

            insert_query = """
                INSERT INTO filemanagement (fileID, filename, filesize, lastmodifieddate, lastaccesseddate, filetype)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            self.cursor.execute(insert_query, (fileID, filename, filesize, lastmodifieddate, lastaccesseddate, filetype))
            self.mydb.commit()
            print(f'File with ID {fileID} has been added.')
        except mysql.connector.Error as err:
            print(f"SQL Error: {err}")

    def search_fileinformation(self):
        try:
            fileID = int(input('Enter File ID to search: '))
            search_query = 'SELECT * FROM filemanagement WHERE fileID = %s'
            self.cursor.execute(search_query, (fileID,))
            found = self.cursor.fetchall()

            if found:
                print('File Found:')
                for x in found:
                    print(x)
            else:
                print('No matching file')
        except mysql.connector.Error as err:
            print(f"SQL Error: {err}")

    def update_fileinformation(self):
        try:
            fileID = int(input('Enter file ID of what to update: '))
            column = input('Enter column to update its value: ')
            newvalue = input('Enter the new value: ')
            update_query = 'UPDATE filemanagement SET ' + column + ' = %s WHERE fileID = %s'
            self.cursor.execute(update_query, (newvalue, fileID,))
            self.mydb.commit()

            if self.cursor.rowcount > 0:
                print(f'File with ID {fileID} has been updated.')
            else:
                print('No matching file')
        except mysql.connector.Error as err:
            print(f"SQL Error: {err}")

    def delete_fileinformation(self):
        try:
            fileID = int(input('Enter fileID to delete: '))
            delete_query = 'DELETE FROM filemanagement WHERE fileID = %s'
            self.cursor.execute(delete_query, (fileID,))
            self.mydb.commit()

            if self.cursor.rowcount > 0:
                print(f'File with ID {fileID} has been deleted.')
            else:
                print('No matching file')
        except mysql.connector.Error as err:
            print(f"SQL Error: {err}")

    def display_fileinformation(self):
        try:
            self.cursor.execute('SELECT * FROM filemanagement')
            for x in self.cursor:
                print(x)
        except mysql.connector.Error as err:
            print(f"SQL Error: {err}")

    def close_connection(self):
        self.cursor.close()
        self.mydb.close()

# Main execution
management = FileManagement()
admin = '1107'
adminpassid = input('Enter Admin PassID: ')

if admin == adminpassid:
    while True:
        operation = input('Choose task [accept file, search file, update file, delete file, display file, logout]: ').lower()
        if operation == 'accept file':
            management.accept_fileinformation()
        elif operation == 'search file':
            management.search_fileinformation()
        elif operation == 'update file':
            management.update_fileinformation()
        elif operation == 'delete file':
            management.delete_fileinformation()
        elif operation == 'display file':
            management.display_fileinformation()
        elif operation == 'logout':
            print('Shutting down app')
            break
else:
    print('Invalid Admin Pass ID')

management.close_connection()
