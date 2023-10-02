import mysql.connector
class FileManagement:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'olajames',
            database = 'finalproject'
        )
        self.cursor = self.mydb.cursor()
    
    def accept_fileinformation(self):
        fileID = int(input('Enter FileID: '))
        filename = input('Enter File Name: ')
        filesize = input('Enter file size in MB: ')
        lastmodifieddate = input('Enter last modified date [format(Year-Month-Date): ]: ')
        lastaccesseddate = input('Enter last modified date [format(Year-Month-Date): ]: ')
        filetype = input('Enter file type : ')
        
        insert_query = """
                INSERT INTO filemanagement(fileID,filename,filesize,lastmodifieddate,lastaccesseddate,filetype) VALUES
                (%s,%s,%s,%s,%s,%s)
            """
        print(f'Property with ID {fileID} has been added.')
              
    def search_fileinformation(self):
        fileID = input('Enter File ID to search: ')
        search_query = f'SELECT * from filemanagement where fileID = %s'
        self.cursor.execute(search_query,(fileID,))
        found = self.cursor.fetchall()
        
        if found:
            print('File Found')
            for x in found:
                print(x)
        else:
            print('No matching file')
            
    def update_fileinformation(self):
        fileID = input('Enter file ID of what to update: ')
        column = input('Enter column to update its value')
        newvalue = input('Enter the new value: ')
        update_query = f'update filemanagement set {column} = %s where fileID = %s'
        self.cursor.execute(update_query, (newvalue,fileID,))
        self.mydb.commit()
        
        if self.cursor.rowcount > 0:
            print(f'File with ID {fileID} has been updated')
            
        else:
            print('No matching file')
      
    def delete_fileinformation(self):
        fileID = input('Enter fileID to delete: ')
        delete_query = f'delete from filemanagement where fileID = %s'
        self.cursor.execute(delete_query,(fileID,))
        self.mydb.commit()
        
        if self.cursor.rowcount > 0:
            print(f'Property with ID {fileID} has been deleted')
            
        else:
            print('No matching file')
            
    def display_fileinformation(self):
        self.cursor.execute('select * from filemanagement')
        for x in self.cursor:
            print(x)
            
management = FileManagement()
admin = '1107'
adminpassid = input('Enter Admin PassID: ')
counter = 1
system = input('Enter start to perform operation: ')
if admin == adminpassid:
    while system == 'start':
        operation = input('Choose task [accept file,search file,update file,delete file,display file,logout]: ')
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
            print('shutting down app')
            break
            system = input('Enter start to keep performing operation: ')
            counter += 1
            
else:
    print('Invalid Admin Pass ID')
