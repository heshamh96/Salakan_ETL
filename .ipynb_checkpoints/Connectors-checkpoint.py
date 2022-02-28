import pyodbc 
def Set_Up_SQL_Server_Connection():

# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
    server = input("Enter The Server Name")
    port=input("Enter the Port number")
    database = input("Enter the Database Name") 
    username = input(("Enter your Username") 
    password = input(("Enter your Password") 
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+','+port+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    return cursor