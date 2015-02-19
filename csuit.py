# Libraries 
import os
import time

# Colors
class bg:
    input = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    option = '\033[93m'
    fail = '\033[91m'
    end = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'


# Banner
def banner():
    print("\n"+bg.end+bg.green+"##################################################################################")
    print("#                                                                                #")
    print("#"+bg.underline+bg.bold+bg.input+"\t\t\t   Hash Craking Suite by @SalvaCorts   "+bg.end+bg.green+"                  #")
    print("#                                                                                #")
    print("#                                                                                #")
    print("#                                                                                #")
    print("#"+bg.end+bg.bold+"\t\t\t\t·HASH IDENTIFICATION:"+bg.end+bg.green+"                            #")
    print("#                                                                                #")
    print("#"+bg.option +"\t[1]"+bg.blue+"Hash Type"+bg.end+bg.green+"                                                             #")
    print("#                                                                                #")
    print("#                                                                                #")
    print("#                                                                                #")
    print("#"+bg.end+bg.bold+"\t\t\t\t·HASH CRACKING:"+bg.end+bg.green+"                                  #")
    print("#                                                                                #")
    print("#"+bg.option+"\t[2]"+bg.blue+" Online Crack\t"+bg.option+"[3]"+bg.blue+" Dictionary Crack\t"+bg.option+"[4]"+bg.blue+" Bruteforce"+bg.end+bg.green+"           #")
    print("#                                                                                #")
    print("#                                                                                #")
    print("#                                                                                #")
    print("#"+bg.end+bg.bold+"\t\t\t\t·MISCELLANEOUS:"+bg.green+"                                  #")
    print("#                                                                                #")
    print("#"+bg.end+bg.option+"\t[5]"+bg.blue+" List Dictionaries\t"+bg.option+"[6]"+bg.blue+" Install tools"+bg.option+"\t[7]"+bg.blue+" Exit"+bg.green+"                 #")
    print("#                                                                                #")
    print("##################################################################################\n"+bg.end)

# Ask if finish
def finish():
    finish = input(bg.input+"\n [+] "+bg.blue+"Finish?(y/n)  >> "+bg.end)
    finish = str(finish)
    if (finish == "y"):
        main()
    else:
        while True:
            finish = input(bg.input+"\n [+] "+bg.blue+"Finish?(y/n)  >> "+bg.end)
            finish = str(finish)
            if finish == "y":
                main()
            else:
                continue

# Online Crack
def online():   
    os.system("clear")
    hash = input(bg.input+"\n [+] "+bg.blue+"Hash? >> "+bg.end)
    hashType = input(bg.input+"\n [+] "+bg.blue+"Hash Encryption? >> "+bg.end)
    hashType = str(hashType)
    os.system("python2 tools/online.py "+hashType+" -h"+" '"+hash+"'")
    
# List Dictionaries
def dics():
    os.system("clear")
    print("\n"+bg.option+"#########################################################################"+bg.end+bg.bold+"\n")
    os.system("ls -la dics/")
    print("\n"+bg.option+"#########################################################################"+bg.end)
    print("\n")
    
# Hash Type
def HashType():
    os.system("clear")
    os.system("python2 tools/hashid.py")
    
# Dictionary Crack
def dictionary():
    # Use JTR!
    os.system("clear")

def bruteforce():
    # Use JTR!
    os.system("clear")

# Install Tools
def install():
    # Install Hash Identifier
    print(bg.end+bg.option+"\n [*] Installing Hash Identifier"+bg.end)
    os.system("cd tools && wget https://hash-identifier.googlecode.com/files/Hash_ID_v1.1.py && mv Hash_ID_v1.1.py hashid.py")
    
    # Install Find My Hash
    print(bg.end+bg.option+"\n [*] Installing Find My Hash"+bg.end)
    os.system("cd tools && wget https://findmyhash.googlecode.com/files/findmyhash_v1.1.2.py && mv findmyhash_v1.1.2.py online.py")
    
    # Install John The Ripper
    print(bg.end+bg.option+"\n [*] Installing John The Ripper"+bg.end)
    os.system("sudo pacman -S john") # Archlinux
    os.system("sudo apt-get install john") # Ubuntu
    os.system("sudo yum install john") # Fedora
    
    # Everything Done
    print(bg.end+bg.option+"\n\n\n [*] Everything have been installed!"+bg.end)
    
# Main
def main():
    os.system("clear")
    def init():
        banner()
        option = input(bg.input+" [+] "+bg.blue+"Option?  >> "+bg.end)
        option = option.lower() # Convert user input to LowCase
        option = str(option)
        if (option == "1"): # Hash Type
            HashType()
            finish()
        elif (option == "2"): # Online Crack
            online()
            finish()
        elif (option == "3"): #  Dictionary Crack
            dictionary()
            finish()
        elif (option == "4"): #  Bruteforce Crack
            bruteforce()
            finish()
        elif (option == "5"): # List Dictionaries
            dics()
            init()
        elif (option == "6"): # Install Tools
            install()
            finish()
        elif (option == "7"): # Exit
            os.system("clear")
            print(bg.option+"\n Happy Hacking!"+bg.end)
            time.sleep(1)
            os.system("clear")
            exit()
        else:
            os.system("clear")
            print(bg.fail+"\n [!] Type 1, 2, 3, 4, 5 or 6\n"+bg.end)
            time.sleep(1.5)
            main()
    init()

# Start
main()