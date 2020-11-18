import time 
from time import sleep
from playsound import playsound
from tqdm import tqdm
from cryptography.fernet import Fernet
import os




print('''
██████╗ ███████╗ █████╗ ████████╗██╗  ██╗    ████████╗ ██████╗      █████╗ ██████╗ ████████╗    
██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║  ██║    ╚══██╔══╝██╔═══██╗    ██╔══██╗██╔══██╗╚══██╔══╝    
██║  ██║█████╗  ███████║   ██║   ███████║       ██║   ██║   ██║    ███████║██████╔╝   ██║       
██║  ██║██╔══╝  ██╔══██║   ██║   ██╔══██║       ██║   ██║   ██║    ██╔══██║██╔══██╗   ██║       
██████╔╝███████╗██║  ██║   ██║   ██║  ██║       ██║   ╚██████╔╝    ██║  ██║██║  ██║   ██║       
 ═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝       ╚═╝    ╚═════╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       
                                                                                                
                             this is a software program to play demos
                                     
                                     
                    
''')


            
# tracks file paths 
musicfile1 = "want to give you time gtr.mp3"
#filename = musicfile4

#removes white spaces to 
#musicf5ile1 = musicfile1.replace(" ", "%20")
# tracks
musicfile2 = "01 Find a way(DL mix).mp3"

musicfile3 = "Day Dream.mp3"

musicfile4 = "Kount to 135.mp3"

musicfile5 = "carstartgarage.mp3"

'''   
# cryptography  
# this secion will check for the user input and have a functions to 
# decrypt and encrypt track selection before and after play 
def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open("/Users/twiggygarcia/dta-/key.key", "rb").read()
    #write_key()
    key = load_key()
key = load_key()    
def encrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    f = Fernet(key)

    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()   

# encrypt data
    encrypted_data = f.encrypt(file_data)

 # write the encrypted file
    with open(filename, "wb") as file:
        file.write(encrypted_data)
    
def decrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)        
    return open("/Users/twiggygarcia/dta-/key.key", "rb").read()

def ect1():
    file = musicfile1
    encrypt(file, key) 
def dct1():
    file = musicfile1
    decrypt(file, key)

def ect2():
    file = musicfile2
    encrypt(file, key) 
def dct2():
    file = musicfile2
    decrypt(file, key)

def ect3():
    file = musicfile3
    encrypt(file, key) 
def dct3():
    file = musicfile3
    decrypt(file, key)

def ect4():
    file = musicfile4
    encrypt(file, key)
def dct4():
    file = musicfile4
    decrypt(file, key)
    
def ect5():
    file = musicfile5
    encrypt(file, key) 
def dect5():
    file = musicfile5    
    decrypt(file, key)

'''

# menu that lets you choose a track to play        
ans=True
while ans:
    print("""
    1.Want To Give You Time
    2.Find A Way
    3.Day Dream
    4.Kount to 135
    5.Test
    6.Exit/Quit
    """)
# this code checks for user input and call the corresponding music file      
    ans=input("""
    What track would you like to play? """)
    if ans=="1":
      print(""""\n 
      Playing - want to give you time""")
      musicfile1 = musicfile1.replace(" ", "%20")
      playsound(musicfile1)
      musicfile1 = musicfile1.replace("%20", " ")   
     # sleep(10)
     # ect1()
      
    elif ans=="2":
      print("\n Playing - Find A Way")
     # dct2()
      musicfile2 = musicfile2.replace(" ","%20")
      playsound(musicfile2)
      sleep(10)
      #musicfile2 = musicfile2.replace("%20", " ")
     # ect2()
      
    elif ans=="3":
      print("\n Playing - Day Dream")
    #  dct3()
      musicfile3 = musicfile3.replace(" ","%20")
      playsound(musicfile3)
     # sleep(10)
      #musicfile2 = musicfile2.replace("%20", " ")
      #ect3()
      
    elif ans=="4":
      print("\n Playing - Kount to 135")
      #dct4()
      musicfile4 = musicfile4.replace(" ","%20")
      playsound(musicfile4)
      #sleep(10)
      #musicfile4 = musicfile4.replace("%20", " ")
      #ect4()
      
      
    elif ans=="5":
      print("\n Playing - test")
      #dect5()
      musicfile5 = musicfile5.replace(" ", "%20")
      playsound(musicfile5)  
      musicfile5 = musicfile5.replace("%20", " ")
      #ect5()
    elif ans=="6":
      print("\n Goodbye") 
      ans = None
    else:
       print("\n Not Valid Choice Try again")
 