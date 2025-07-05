##RUN IN TERMUX⤵️##  
# python ~/storage/shared/python/cowsaydate.py  

import cowsay  
import random  
import os  

def show_intro():  
    cowsay.cow("Welcome to  Cowsay-Club!")  
    input("type enter to progress")  

    cowsay.cow("I am the Club host and i am here to show you around.")  
    input("type enter to progress")  

    cowsay.cow("Who do you wanna talk with first?")  
    print("1. Luna")  
    print("2. Max")  
    print("3. Charlie")  
    print("4. Bella")  
    print("5. Milo")  

def choose_date():  
    choice = int(input("enter the number of your date: "))  
    if choice == 1:  
        luna()  
    else:  
        cowsay.cow("too bad! Harry just happened to be bad at python so its lunas turn instead!")  
        input("type enter to progress")  
        luna()  

def luna():  
    print("Luna")  
    os.system("cowsay -f flaming-sheep    HELP")  
    # cowsay.flaming_sheep("HELP")  
    input("type enter to progress")  

    os.system("cowsay -f flaming-sheep     HHEEEEELPP")  
    # cowsay.flaming_sheep("HHEEEEELPP")  
    input("type enter to progress")  

    print("1. Help")  
    print("2. Do nothing")  
    choice = int(input("what do you do:"))  

    if choice == 1:  
        os.system("cowsay -f sheep thx")  
        input("type enter to progress")  
        os.system("cowsay -f sheep k by")   
        print("Luna left")           
        input("NEXT")  
        max()  
    else:  
        os.system("cowsay -f flaming-sheep lmao")  
        input("type enter to progress")  
        print("Luna has turned into ash") 
        input("NEXT")  
        max()  

def max():  
    print("Max")  
    os.system("cowsay -f stimpy Im max")  
    input("type enter to progress")    
    os.system("cowsay -f stimpy Im max")  
    input("type enter to progress")  
    os.system("cowsay -f stimpy Im m-")   

    print("1. You are max.")  
    print("2. shut up")  
    choice = int(input("what do you do:"))  

    if choice == 1:  
        os.system("cowsay -f stimpy ...")  
        input("type enter to progress")  
        os.system("cowsay -f stimpy Im max :）")
        input("type enter to progress")  
        print("Max left happily")  
        input("NEXT")  	
        charlie()
    else:  
        os.system("cowsay -f stimpy ...") 
        input("type enter to progress")   
        os.system("cowsay -f stimpy im max.. :（")  
        input("type enter to progress")  
        print("Max dissolved")  
        input("NEXT")  
        charlie()

def charlie():
    print("Charlie")
    os.system("cowsay -f elephant Hello, Im Charlie")
    input("type enter to progress")  
    
    print("1. You seem to be the most normal around here.")  
    print("2. Nice trunk you have (snabel på svenska)")  
    choice = int(input("what do you do:"))  

    if choice == 1:  
        os.system("cowsay -f elephant WHAT DID YOU SAY ABOUT MAH MOTHA")    
        input("type enter to progress")      
        print("1. Snake.")     
        input("what do you do:")  
        os.system("cowsay -f elephant ??")    
        input("type enter to progress") 
        os.system("cowsay -f elephant-in-snake *muffle*! *muffle*!")    
        input("type enter to progress")  
        print("Charlie was turned into poo")  	
        input("NEXT")  
        bella()
    else:  
        os.system("cowsay -f elephant  Thanks!") 
        input("type enter to progress") 
        os.system("cowsay -f elephant  Oh wait! need to go!")
        print("1. Bye!")     
        input("what do you do:")  
        print("Charlie ran away")   
        input("NEXT")   
        bella() 
        
def bella():
    print("Bella :）")	
    os.system("cowsay -f blowfish  I want a cheeseroll.")
    input("type enter to progress")   
    os.system("cowsay -f blowfish  CHEESEROLL CHEESEROLL CHEEESSEEEEHH-RRROOOOOLLEEEEEHHH")
    input("type enter to progress") 
    os.system("cowsay -f blowfish Do you want to hear my latest song?")
    
    print("1. Yes")  
    print("2. No")  
    choice = int(input("what do you do:"))  

    if choice == 1:  
        os.system("cowsay -f blowfish ♫ Cheeseroll, Cheeseroll , CHEESEROLL, CHHEEESSEERROOLLLL, CHEES-RU5YGYJY2H4U1, G4QH3YH24I1B2TJYR ♫")
        input("type enter to progress") 
        os.system("cowsay -f blowfish ♫ KRLGJRQI2RKXB1EKCJ ♫")
        input("type enter to progress") 
        print("Bella blew up into thousands... Cheeserolls??")
        input("NEXT")
    else:
        os.system("cowsay -f blowfish  Cheeseroll :（")
        input("type enter to progress") 
        print("Bella took a giant cheeseroll and flew away on it")   
        input("NEXT")   	

# Game loop  
show_intro()  
choose_date()