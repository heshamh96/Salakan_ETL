import pyodbc 
import pandas as pd


def Set_Up_a_CSV_File_Connection():
    print("Enter The Following File Creditinals \n")
    print("File Path ")
    print("File Name \n")
    
    path=input("Enter the Path to the File \n")
    filename=input("Enter the File Name \n")
    df =pd.read_csv(path+'/'+filename)
    return df
    

def Set_Up_a_Json_File_Connection():
    path=input("Enter the Path to the File \n")
    filename=input("Enter the File Name")
    df =pd.read_json(path+'/'+filename)
    return df
    


def Set_Up_SQL_Server_Connection():

# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
    server = input("Enter The Server Name \n")
    port=input("Enter the Port number \n")
    database = input("Enter the Database Name \n") 
    username = input("Enter your Username \n") 
    password = input("Enter your Password \n") 
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+','+port+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    query=input("Enter a Query for your DataSet \n")
    df = pd.read_sql(query, cnxn)
    return cursor,df