##RUN IN TERMUX⤵️##  
# python ~/storage/shared/python/cowsaydate.py  

import cowsay  
import random  
import os  

kills = 0

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
    global kills
    print("Luna")  
    os.system("cowsay -f flaming-sheep    HELP")  
    input("type enter to progress")  

    os.system("cowsay -f flaming-sheep     HHEEEEELPP")  
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
        kills = kills + 1
        print("Luna has turned into ash") 
        input("NEXT")  
        max()  

def max():  
    global kills
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
        kills = kills + 1
        print("Max dissolved")  
        input("NEXT")  
        charlie()

def charlie():
    global kills
    print("Charlie")
    os.system("cowsay -f elephant Hello, Im Charlie")
    input("type enter to progress")  

    print("1. You seem to be the most normal around here.")  
    print("2. Nice trunk you have")  
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
        kills = kills + 1
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
    global kills
    print("Bella")	
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
        kills = kills + 1
        print("Bella blew up into thousands... Cheeserolls??")
        input("NEXT")
        milo()
    else:
        os.system("cowsay -f blowfish  Cheeseroll :（")
        input("type enter to progress") 
        print("Bella took a giant cheeseroll and flew away on it")   
        input("NEXT")
        milo()

def milo():
    global kills
    print("Milo")
    os.system("cowsay -f stegosaurus Gigidi-gagidi-go.") 
    input("type enter to progress")
    os.system("cowsay -f stegosaurus That is my very own greeting.") 
    input("type enter to progress")
    os.system("cowsay -f stegosaurus Would you like a cup of tea?") 

    print("1. Aye")  
    print("2. Not bloody likely")  
    choice = int(input("what do you do:"))  

    if choice == 1:  
        os.system("cowsay -f stegosaurus The bees knees!") 
        input("type enter to progress")
        os.system("cowsay -f stegosaurus ...")
        input("type enter to progress") 
        os.system("cowsay -f stegosaurus *slurp*") 
        input("type enter to progress")
        os.system("cowsay -f stegosaurus ...") 
        input("type enter to progress")
        os.system("cowsay -f stegosaurus cheers for the cuppa!")
        input("type enter to progress")
        os.system("cowsay -f stegosaurus ... oh wait.")
        input("type enter to progress")
        kills = kills + 1
        print("Milo forgot he was super allergic to tea-leaves.") 			
        input("NEXT") 
        day2()     
    else:    
        os.system("cowsay -f stegosaurus No cup of tea? Blimey, youre missing out mate!")
        input("type enter to progress")
        print("Milo yomped away") 			
        input("NEXT")   
        day2()
        
def day2():     
    global kills
    print(".########.....###....##....##..#######.")   
    print(".##.....##...##.##....##..##..##.....##")    
    print(".##.....##..##...##....####..........##")
    print(".##.....##.##.....##....##.....#######.")
    print(".##.....##.#########....##....##.......")
    print(".##.....##.##.....##....##....##.......")
    print(".########..##.....##....##....#########")
    input("type enter to progress")  
    os.system("cowsay Hi, its me again!")
    input("type enter to progress") 

    if kills == 5:
        os.system("cowsay -t uuhh.. so the club has been a little..") 
        input("type enter to progress")  
        os.system("cowsay -p empty.. lately...") 
        input("type enter to progress")  
        os.system("cowsay -t sooo... uhhh...") 
        input("type enter to progress") 
        os.system("cowsay -p ill give the ownership to you..") 
        input("type enter to progress")  
        print("The Clubhost ran away in fear") 
        genocide()
    elif kills > 0:
        os.system("cowsay Some people have left the club this week.") 
        input("type enter to progress")    
        os.system("cowsay -t probably because they have better things to do..") 
        input("type enter to progress") 
        os.system("cowsay anyways, did you find anybody you like?") 
        input("type enter to progress")   
        os.system("cowsay -t too bad, Harry sucks at python..") 
        input("type enter to progress") 
        os.system("cowsay Maybe we will see a sequel to this python/terminal game?") 
        input("type enter to progress") 
        os.system("cowsay -e ^^ OK! bye!")
        input("type enter to progress")  
        neutral()
    else:
        os.system("cowsay did you find anybody you like?") 
        input("type enter to progress")   
        os.system("cowsay -t too bad, Harry sucks at python..") 
        input("type enter to progress") 
        os.system("cowsay Maybe we will see a sequel to this python/terminal game?") 
        input("type enter to progress") 
        os.system("cowsay -e ^^ OK! bye!")
        input("type enter to progress") 
        pacifist()        

def genocide():
    print(".########.##....##.########.")
    print(".##.......###...##.##.....##")            
    print(".##.......####..##.##.....##")
    print(".######...##.##.##.##.....##")
    print(".##.......##..####.##.....##")
    print(".##.......##...###.##.....##")
    print(".########.##....##.########.")
    print("")
    print("You got the genocide ending!")
    print("Run the start command to play again and try to get the other endings.") 

def neutral():
    print(".########.##....##.########.")
    print(".##.......###...##.##.....##")
    print(".##.......####..##.##.....##")
    print(".######...##.##.##.##.....##")
    print(".##.......##..####.##.....##")
    print(".##.......##...###.##.....##")
    print(".########.##....##.########.")
    print("")
    print("You got the neutral ending!")
    print("Run the start command to play again and try to get the other endings.")      

def pacifist():
    print(".########.##....##.########.")
    print(".##.......###...##.##.....##")
    print(".##.......####..##.##.....##")
    print(".######...##.##.##.##.....##")
    print(".##.......##..####.##.....##")
    print(".##.......##...###.##.....##")
    print(".########.##....##.########.")
    print("")
    print("You got the pacifist ending!")
    print("Run the start command to play again and try to get the other endings.")

# Game loop  
show_intro()  
choose_date()