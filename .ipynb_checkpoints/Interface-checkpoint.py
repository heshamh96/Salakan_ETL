import Connectors as conn


def home_page():
    print("choose your The Source you are going ot extract from \n")
    print("Enter 1 for CSV \n")
    print("Enter 2 for json \n")
    print("Enter 3 for Sql-Server \n")
    print("Enter 4 for Denodo \n")
    Src_Choice=input("your Choice ... \n")
    return int(Src_Choice)


def call_Src_Connections(Src_Choice): ## it returns a Dataframe hodling the source
    if Src_Choice==1:
        return conn.Set_Up_a_CSV_File_Connection()
    elif Src_Choice==2:
        return conn.Set_Up_a_Json_File_Connection()
    else:
        return conn.Set_Up_SQL_Server_Connection()
    
