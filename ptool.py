#!/usr/bin/python3
#pip3 install python-nmap
import nmap
import os

sc = nmap.PortScanner()
print("Checking dependances...")
print(os.system('sudo apt update && apt install pip && apt install nmap && pip3 install python-nmap'))
print("All installed!")
print(os.system('clear'))
print(" ________________________________")
print("|                                |")
print("|                                |")
print("|           PTOOL v1.0           |")
print("|        Made by WrkEagle        |")
print("|                                |")
print("|________________________________|")

def main():
    n = input("1- Network\n2- Web\n3- Pentest\n\n Make your choice: ")

    if n == '1':
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
        nmap()
    
    if nc == '2':
        vuln()
    
    if nc == '3':
        exploit()
    
    if cn == '4':
        main()
    
    else : 
        print("Choose only between those things ")
        NETWORK()



def nmap():
    print("*****************| NetScan |*****************")
    ip = input("\nEnter the target's IP address: ")

    #port = input("\nEnter the target's port: ")
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

#The Pentest part---------------------------------------------------------------------------

def PENTEST():
    print("*************************************************")
    print("******************|  PENTEST  |******************")
    print("*************************************************")







if __name__ == "__main__":
        main()