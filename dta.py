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

#cryptography  
            
#tracks 
musicfile1 = "/Users/twiggygarcia/Documents/Coding and Scripts/dta program/want to give you time gtr.mp3"
#removes white spaces to 
musicfile1 = musicfile1.replace(" ", "%20")
#tracks
musicfile2 = "/Users/twiggygarcia/Documents/Coding and Scripts/dta program/01 Find a way(DL mix).mp3"
musicfile2 = musicfile2.replace(" ","%20")
musicfile3 = "/Users/twiggygarcia/Documents/Coding and Scripts/dta program/Day Dream.mp3"
musicfile3 = musicfile3.replace(" ","%20")
musicfile4 = "/Users/twiggygarcia/Documents/Coding and Scripts/dta program/Kount to 135.aif"
musicfile4 =musicfile4.replace(" ","%20")

#menue that lets you choose a track to play        
ans=True
while ans:
    print("""
    1.Want To Give You Time
    2.Find A Way
    3.Day Dream
    4.Kount to 135
    5.Exit/Quit
    """)
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
 





      


    






