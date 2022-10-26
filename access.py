import pandas as pd
import matplotlib.pyplot as plt
import time
import warnings as wrn
from ast import Break
import main1 as mn

def format_Warning(message, category, filename, lineno, line=''):
    return str(filename) + ':' + str(lineno) + ': ' + category.__name__ + ': ' +str(message) + '\n'

wrn.formatwarning = format_Warning

def introduction():
    msg = '''
           Auto started the next python script --> access.py
          to continue the working of this project.      


          This part works as the main as the most of the data can be viewed from this script.
           Simply choose what you want to choose from the main menue.
           Only shown option an be used.
           Invalid command will be considered as a error, which will cause the program to collapse
           
           
                                                                                    ~regards GLITCH\n\n\n\n'''
                                                                                    
    for x in msg:
        print(x, end='')
        time.sleep(0.002)
    wait = input('Press any key to continue.....')
introduction()


def add():
    mn.begin()
    wait = input('\n\n\n Press any key to continuee.....')
    opt()

def creator():
    msg='''
            ISP DATA COLLECTION ANALYSIS MADE BY  : GLITCH
            ROLL NO                               : ***
            SCHOOL NAME                           : *****
            SESSION                               : 20**-**
            
                      THANKYOU FOR REVIEWING MY PROJECT
                      \n\n\n
                '''
    for x in msg:
        print(x, end='')
        time.sleep(0.002)

    wait = input('Press any key to exit.....')

#dataframe
def data():
    csv__data=pd.read_csv('data.csv')
    print("DATA MANAGEMET")
    print('*'*40)
    print("1.CLIENT BROWSING HISTORY")
    print("2.WEBSITE VISIT COUNT")
    print("3.TOTAL DATA COUNT")
    print("4.EXIT TO MAIN MENU")
    wrn.warn('ENTER THE INDEX NO: OF YOUR CHOICE ONLY!',DeprecationWarning)
    df_data=int(input("ENTER YOUR CHOICE:"))
    print()
    if df_data==1:
        print()
        title="CLINT BROWSING HISTORY"
        print(title)
        print('*'*40)
        print(csv__data)
        wait = input('\n\n\n Press any key to continuee.....')
        data()

    if df_data==2:
        print()
        title="WEBSITE VIEW COUNT"
        print(title)
        print('*'*40)
        DF=csv__data.pivot_table(columns=['DOMAIN'],aggfunc='size')
        print(DF)
        wait = input('Press any key to continue.....')
        data()

    if df_data==3:
        print()
        title="TOTAL DATA COUNT"
        print(title)
        print('*'*40)
        c=len(csv__data.axes[0]) 
        print(c)
        wait = input('Press any key to continue.....')
        data()
    
    if df_data==4:
        print()
        wait = input('Press any key to continue.....')
        opt()     

#graph
def graph():
    csv__data=pd.read_csv('data.csv')
    print(" GRAPHICAL DATA MANAGMENT")
    print('*'*40)
    print("1.DOMAIN TIME")
    print("2.WEB DATA USEAGE")
    print("3.EXIT TO MAIN MENU")
    wrn.warn('ENTER THE INDEX NO: OF YOUR CHOICE ONLY!',DeprecationWarning)
    A=int(input("ENTER YOUR CHOICE:"))
    print()
    if A==1:
          print()
          plt.xlabel("DOMAINS --->")
          plt.ylabel("TIME ---->")
          plt.title("TIME SPEND IN DOMAINS")
          plt.grid(True)
          k=csv__data.groupby('DOMAIN')
          x=csv__data['DOMAIN'].unique()
          y=k['DOMAIN'].count()
          plt.bar(x,y)
          plt.show()

          wait = input('Press any key to continue.....')
          graph()
    if A==2:
        print()
        plt.title("WEBSITE DATA USEAGE")
        plt.grid(True)
        k=csv__data.groupby('DOMAIN')
        X=csv__data['WEBSITE'].unique()
        Y=k['DOMAIN'].size()
        plt.xlabel("WEBSITE --->")
        plt.ylabel("DATA USEAGE --->")
        plt.bar(X,Y)
        plt.show()        
        wait = input('Press any key to continue.....')
        graph()
    if A==3:
        print()
        wait = input('Press any key to continue.....')
        opt()     

def opt():
    print("  OPTION MENU")
    print('*'*40)
    print("1.DATA MANAGEMET")
    print("2.GRAPHICAL DATA MANAGMENT")
    print("3.CHECK FOR MORE DATA")
    print("4.EXIT")
    wrn.warn('ENTER THE INDEX NO: OF YOUR CHOICE ONLY!',DeprecationWarning)
    opt_data=int(input("ENTER YOUR CHOICE:"))
    print()
    if opt_data==1:
        data()
    if opt_data==2:
        graph()
    if opt_data==3:
        add()    
    if opt_data==4:
        creator()
opt()    
