##This Is the main where the Program Starts Excution!

import Interface as ui

def main():
    print ("Welcome To Salakan ETL")
    
    choice=ui.home_page()
    
    lol=ui.call_Src_Connections(choice)
    print(lol)
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    main()