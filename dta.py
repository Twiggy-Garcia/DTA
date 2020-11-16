import time 
from playsound import playsound
from tqdm import tqdm
from cryptography.fernet import Fernet



print('''
██████╗ ███████╗ █████╗ ████████╗██╗  ██╗    ████████╗ ██████╗      █████╗ ██████╗ ████████╗    
██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║  ██║    ╚══██╔══╝██╔═══██╗    ██╔══██╗██╔══██╗╚══██╔══╝    
██║  ██║█████╗  ███████║   ██║   ███████║       ██║   ██║   ██║    ███████║██████╔╝   ██║       
██║  ██║██╔══╝  ██╔══██║   ██║   ██╔══██║       ██║   ██║   ██║    ██╔══██║██╔══██╗   ██║       
██████╔╝███████╗██║  ██║   ██║   ██║  ██║       ██║   ╚██████╔╝    ██║  ██║██║  ██║   ██║       
 ═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝       ╚═╝    ╚═════╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       
                                                                                                
                             this is a software program to play demos
                                     
                                     (type -h for the help menu)
                    
''')


            
# tracks file paths 
musicfile1 = "/Users/twiggygarcia/Documents/Coding and Scripts/dta program/want to give you time gtr.mp3"
#removes white spaces to 
musicfile1 = musicfile1.replace(" ", "%20")
# tracks
musicfile2 = "/Users/twiggygarcia/Documents/Coding and Scripts/dta program/01 Find a way(DL mix).mp3"
musicfile2 = musicfile2.replace(" ","%20")
musicfile3 = "/Users/twiggygarcia/Documents/Coding and Scripts/dta program/Day Dream.mp3"
musicfile3 = musicfile3.replace(" ","%20")
musicfile4 = "/Users/twiggygarcia/Documents/Coding and Scripts/dta program/Kount to 135.aif"
musicfile4 =musicfile4.replace(" ","%20")


# menu that lets you choose a track to play        
ans=True
while ans:
    print("""
    1.Want To Give You Time
    2.Find A Way
    3.Day Dream
    4.Kount to 135
    5.Exit/Quit
    """)
# this code checks for user input and call the corresponding music file      
    ans=input("What track would you like to play? ")
    if ans=="1":
      print("\n Playing - want to give you time")
      playsound(musicfile1)
    elif ans=="2":
      print("\n Playing - Find A Way")
      playsound(musicfile2)
    elif ans=="3":
      print("\n Playing - Day Dream")
      playsound(musicfile3)
    elif ans=="4":
      print("\n Playing - Kount to 135")
      playsound(musicfile4)
    elif ans=="5":
      print("\n Goodbye") 
      ans = None
    else:
       print("\n Not Valid Choice Try again")
 








    
# cryptography  
# this secion will check for the user input and have a functions to 
# decrypt and encrypt track selection before and after play 
def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
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
    return open("/Users/twiggygarcia/Documents/Coding and Scripts/dta program/key.key", "rb").read()
def dctp():
    if ans==1 :
        


      


    






