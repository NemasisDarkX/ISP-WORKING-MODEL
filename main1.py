import pandas as pd
import socket
import webbrowser,time

def introduction():
    msg = '''
          This is a python project only for educational purpose.

          This project consist of 2 python files.
          Files auto starts on running access.py
          
          This project is based on how internet service providers collect 
          data from clients.
          
          This projects scripts are uploaded to github: https://github.com/NemasisDarkX
                                                                                  
                                                                                     ~regards Abhay R\n\n\n\n\n'''
    for x in msg:
        print(x, end='')
        time.sleep(0.002)
    wait = input('Press any key to continue.....')

introduction()
print()
    
def begin():
    url=input("ENTER YOUR WEB HERE:")
    web=webbrowser.open_new_tab(url) 


    weblink = url


    Domain_name = ""


    x = weblink.split("/")

 

    if(x[0] == "https:" or x[0] == "http:"):

          x = x[2].split(".")

 

    else:

          x = x[0].split(".")
 

    if(len(x) == 2):

          Domain_name = x[0]


    else:

        Domain_name = x[1]

    #print("Domain Name Is:",Domain_name)        

    dns=socket.gethostbyname(weblink)
    #print("DNS:",dns)


    domain=Domain_name
    dns=dns
    data={"WEBSITE":weblink,"DOMAIN":domain,"DNS":dns}
    def alt():
        
        df=pd.DataFrame(data,index=[1])
        df.to_csv("data.csv",index=False,mode='a',header=False)
        #print(df)
    alt()    

begin()
