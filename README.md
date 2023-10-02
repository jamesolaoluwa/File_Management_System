•  File Management System
-  This Python script provides a simple file management system that interacts with a MySQL database to perform basic file management tasks. 
-  It allows users to perform operations such as accepting file information, searching for files, updating file information, deleting files, and displaying all files in the database.

•  Prerequisites
-  Before using this script, make sure you have the following prerequisites installed:
-  Python 3
-  MySQL
-  Python mysql-connector library (Install using pip install mysql-connector-python)

•  Usage
-  Clone this repository or download the Python script.
-  Configure the MySQL database connection details in the __init__ method of the FileManagement class. Modify the host, user, password, and database fields to match your MySQL server settings.

START CODE:
-  self.mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='your_password',
    database='finalproject'
)
Enter the Admin Pass ID when prompted. The default Admin Pass ID is '1107'.

• Choose a task from the following options:

-  accept file: Add a new file entry to the database.
-  search file: Search for a file by File ID.
-  update file: Update the information of an existing file.
-  delete file: Delete a file by File ID.
-  display file: Display all files in the database.
-  logout: Exit the application.

•  This script provides a basic file management system and can be extended to meet specific requirements.
•  Ensure that the MySQL server is running and the database schema is set up correctly with a filemanagement table.
