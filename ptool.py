#!/usr/bin/python3
#pip3 install python-nmap
import nmap
import os

sc = nmap.PortScanner()
print("Checking dependances...")
print(os.system('sudo apt update && apt install pip && apt install nmap && pip3 install python-nmap && apt install git'))
print("All installed!")
print(os.system('clear'))
def pres():
    print(" ________________________________")
    print("|                                |")
    print("|                                |")
    print("|           PTOOL v0.1           |")
    print("|        Made by WrkEagle        |")
    print("|                                |")
    print("|________________________________|")

def main():
    n = input("\n1- Network\n2- Web\n3- Pentest\n\n Make your choice: ")

    if n == '1':
        print(os.system('clear'))
        NETWORK()




#The Network part---------------------------------------------------------------------------
def NETWORK():
    print("*************************************************")
    print("******************|  NetWork  |******************")
    print("*************************************************")
    Nchoice()


def Nchoice():
    nc = input("1- Network scanner\n2- Vulnerabilities Detection\n3- Exploit\n4- Back\nPlease choose a number: ")
    
    if nc == '1':
        print(os.system('clear'))
        nmap()
    
    if nc == '2':
        print(os.system('clear'))
        vuln()
    
    if nc == '3':
        print(os.system('clear'))
        exploit()
    
    if nc == '4':
        print(os.system('clear'))
        pres()
        main()
    
    else : 
        print(os.system('clear'))
        print("Choose only between those things ")
        NETWORK()



def nmap():
    print("*****************| NetScan |*****************")
    ip = input("\nEnter the target's IP address: ")

    #port = input("\nEnter the target's port: ")<------ à utiliser plus tard
    sc.scan(ip, '1-1024')

    print(" \n\n\n/!\  Boss, here are the results!  /!\ ")
    print(sc.scaninfo())
    print(sc[ip]['tcp'].keys())

def vuln():
    print("*****************| VulnScan |*****************")
    ip = input("\nEnter the target's IP address: ")
    print(os.system('nmap -sV --script=vulscan.nse ' +ip))

def exploit():
    print("*****************| Exploit |*****************")
    
    print("Is under construction...")
    exc = input("You only can choose the DDOS hammer by putting 1\nEnter your choice: ")

    if exc == '1':
        print("**********************************************************")
        print("*********************/!\ WARNING /!\**********************")
        print("**********************************************************")
        print("****You are responsible of your acts with this program****")
       # yn = input("Do you want to continue? 1/0: ")
        #if yn == '1' :
        #print(os.system(' python3 hammer.py'))
       # else :
            #print("going back")
           # NETWORK()
    else :
        print("Back to the previous section")
        print(os.system('clear'))
        NETWORK()


#The Pentest part---------------------------------------------------------------------------

def PENTEST():
    print("*************************************************")
    print("******************|  PENTEST  |******************")
    print("*************************************************")
    Pchoice()

def Pchoice():
    nc = input("1- OSINT\n2- Malware Factory\n3- Exploit\n4- Back\nPlease choose a number: ")
    
    if nc == '1':
        nmap()
    
    if nc == '2':
        vuln()
    
    if nc == '3':
        exploit()
    
    if cn == '4':
        main()
    
    else : 
        print("Choose only between those things ")
        PENTEST()







if __name__ == "__main__":
        pres()
        main()
