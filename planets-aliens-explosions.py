#CMPT 120 D100
#SHAYNA GROSE
#STUDENT ID: 301308729
#PLANETS, ALIENS and EXPLOSIONS



#CHOOSING WHICH FILE TO OPEN
def choosing_board(board):
        if board=="d":     #default board
            the_file = "PlanetsData1.txt"
        else:
            the_file=board    #user can choose another board
        return the_file


#OPENING FILE
def read_string_list_from_file(the_file):

   
    fileRef = open(the_file,"r") # opening file to be read
    localList=[]
    for line in fileRef:
        string = line[0:len(line)-1]  # eliminates trailing '\n'
                                      # of each line 
                                    
        localList.append(string)  # adds string to list
        
    fileRef.close()
    '''
    #........
    print ("\n JUST TO TRACE, the local list of strings is:\n")
    for element in localList:
        print (element)
    print ()
    #........
    '''
    return localList


#CONVERTING TO LIST
def convert_to_individual(listStrings):
    planetdata=""
    for i in range(len(listStrings)):
        planetdata=planetdata+listStrings[i]+"-"
    planetdata=planetdata.split("-")
    planetdata.remove("")           #removing dashes and spaces
    return planetdata


#VALIDATING Y/N INPUT       
def valid_input_yes_no(answer):
    if answer == "y" or "n":
        answer=answer
    while answer != "y" and answer!="n":
       answer=input(("What you typed was not expected, please try again: "))
    return answer

#VALIDATING D/T INPUT
def valid_input_d_t(user):    #for rolling or typing next position
        if user== "d" or "t":
                user=user
        while user != "d" and user !="t":
                user=input(("What you typed was not expected, please try again: "))
        return user


#VALIDATING NUMBER INPUT
def valid_input_numbers(number,accepted): #accpeted is a range specified             
        while number.isalpha():           #for each individual validation
            number=input("What you typed was not a number, please try again: ")
        while number.isdigit() and (int(number) in accepted)==False:
                    number=input("What you typed was not expected, please try again: ")
        return int(number)


#CREATING CIVLEVEL LIST
def make_civlevel_list(planetdata):  #taking every 3rd element starting from 0 
    civ_level=[]                     #which corresponds to the civ levels
    for i in range(0,len(planetdata),3):
        civ_level.append(planetdata[i])
    return civ_level



#CREATING FUEL LIST
def make_fuel_list(planetdata):
    fuel=[]
    for i in range(1,len(planetdata),3):  #taking every 3rd elements starting at 1
        fuel.append(planetdata[i])        #which corresponds to the fuel
    return fuel


#CREATING ROCK LIST
def make_rocks_list(planetdata):
    rocks=[]
    for i in range(2,len(planetdata),3):  #taking every 3rd element starting from 2
        rocks.append(int(planetdata[i]))   #which corresponds to the rocks
    return rocks


#CREATES BOARD
def create_lists_board(p_civlevel,a_pos,python_pos):
    astro=""
    python_p=""
    print("    ","Planet#","      ","CivLevel","  ","Fuel","  ","Rocks")
    for i in range(len(p_civlevel)):
        if i==a_pos:
            astro="<--- Astronaut"             #creates the board from individual lists
        else:                                   #only prints python planet if user wants it
            astro=""
        if i==python_pos:
            if i !=0:
                python_p="<=== PythonPlanet"
        else:
            python_p=""
        print("\t",i,"\t","\t",p_civlevel[i],"\t",p_fuel[i],"\t",p_rocks[i],"\t",astro,python_p)
        
    print()


#DISPLAYS BOARD
def show_board(title,turn):
    print("\nShowing board..."+title+str(turn))
    print("\n The board at this point contains...")    #displays the board for every turn
    create_lists_board(p_civlevel,a_pos,python_pos)     #calls the function above to create the new board each turn
    
     


#DISPLAYS ASTRONAUTS INFO
def show_astronaut(turn,a_name,a_pos,a_fuel,a_rocks,a_alive):    #shows astronauts name, civlevel, fuel and rocks
    if str(turn).isdigit():
        print("Showing astronaut ... about to do turn num: ",turn )
    else:
        print("Showing astronaut at:",turn)
    print()
    print("The astronaut", a_name,"has civilization level", a_civlevel)
    print("They are currently in position: ",a_pos)  
    print("They currently have: ",a_fuel,"fuel litres")
    if str(turn).isdigit():
        print("and have collected until and including this turn", a_rocks, "rock specimens")
    else:
        print("and collected during the whole game", a_rocks,"rock specimens")
    print()
    if a_alive==True:
            print("You are....alive")
            if str(turn).isdigit():
                    print("and ready to keep moving!")
            else:
                    print("but you cannot move anymore since the game has ended!")
    elif a_alive==False:
            print("You are....dead")
            print("so you cannot move anymore and the game is over.")
    


    
#ROLLING DIE OR TYPING
def roll_die(a_pos,num_planets,p_civlevel):
    roll=input("Roll die, or type your next position? (d/t): ")   #user can choose to roll(d) or type(t)
    roll=valid_input_d_t(roll)
    print()
    if roll=='d':
        global die
        die = r.randint(1,6)
        print("the die was... ",die)
        print("The astronaut was previously in position...",a_pos)  #advances the board circularly
        leng=len(p_civlevel)
        a_pos=(a_pos+die)%leng
        print("The astronaut is now in position...",a_pos)
    elif roll=='t':
        print("The astronaut was previously in position...",a_pos)
        a_pos=int(input("Where would you like to go? (0.."+str(num_planets)+") "))
        print("The astronaut is now in position...",a_pos)
    return a_pos


#CHECKING IF ASTRONAUT HAS REACHED PYTHON PLANET
def python_planet_reached(a_pos,python_pos):
        if int(a_pos)==int(python_pos):     #every time th astronaut moves this checks
                python_planet=True          #if they've landed on pytho planet
        else:
                python_planet=False
        return python_planet



        

#INTERACTING WITH ALIENS/CHANGING FUEL
def interacting_aliens(a_civlevel,a_pos,p_civlevel,a_fuel):  
    global p_fuel
    if int(p_fuel[a_pos])!=0:
        print("There are aliens in this planet!!")
        print("With civilization level...",p_civlevel[a_pos])
        
        if a_civlevel<int(p_civlevel[a_pos]):
              loss=r.randint(1,int(a_fuel))
              a_fuel=int(a_fuel)-loss
              print("Uh Oh! The aliens are more civilized than the astronaut!")
              print("You lost", loss, "fuel litres.")
              
        if a_civlevel==int(p_civlevel[a_pos]):
              loss=r.randint(1,int((a_fuel)/2))
              print("The aliens are equally as civilized as the astronaut!")
              print("But you lost",loss,"fuel litres")
              a_fuel=int(a_fuel)-loss
        
        if a_civlevel>int(p_civlevel[a_pos]):
              gain=r.randint(1,int(p_fuel[a_pos]))
              a_fuel=int(a_fuel)+gain
              p_fuel[a_pos]= int(p_fuel[a_pos])-gain
              print("Great! The astronaut is more civilized than the aliens!")
              print()
              print("You gained",gain,"fuel litres!")
              print("The planet now has",p_fuel[a_pos], "fuel litres")
              
        print("You now have", a_fuel,"fuel litres.")
        
    else:
        print("There is no fuel on this planet!")
        a_fuel=a_fuel
    return a_fuel


#GAINING ROCKS
def collecting_rocks(a_rocks,p_rocks):
    if int(a_fuel)>0:
            if int(p_rocks[a_pos])>0:
                print("Woohoo! There are", p_rocks[a_pos],"rocks on this planet!")
                rock_gain=(int(p_rocks[a_pos])//3)
                a_rocks.append(rock_gain)
                p_rocks[a_pos]=int(p_rocks[a_pos])-rock_gain
            else:
                    print("Too bad! There are no rocks on this planet!")
                    rock_gain=0
                    a_rocks.append(rock_gain)
            print("You collected",rock_gain,"rocks")
            print("Your rock collection is now:",a_rocks)
            print()
            print("The planet now has",p_rocks[a_pos],"rocks")
    return a_rocks



#MILD EXPLOSIONS
def mild_explosion(a_pos,p_civlevel,prop_exp,turn,p_rocks):
    end=int(len(p_civlevel))*int(prop_exp)
    exp_pos=r.randint(1,end)
    if exp_pos<len(p_civlevel):
        print("Oooh a mild explosion is happening on planet #",exp_pos,"!!!")
        print("The board will now have more rock specimens!")
        global num_explosions
        num_explosions=num_explosions+1
        for p in range(1,exp_pos):
            p_rock_gain=0
            for i in range(p,exp_pos+1):
                p_rock_gain=int(p_rock_gain)+int(p_rocks[i])
            p_rocks[p]=int(p_rock_gain)
        print()
        show_board("after mild explosion, still on turn num: ", turn)
        print()
    return p_rocks



#AMAZING EXPLOSIONS
def amazing_explosions(a_pos,p_civlevel,prop_exp,turn,p_rocks,p_fuel,num_planets):
    end=int(len(p_civlevel))*int(prop_exp)
    exp_pos=r.randint(1,end)
    if exp_pos<len(p_civlevel):
        print("Oooh an AMAZING explosion is happening on planet #",exp_pos,"!!!")
        print("The board will now have more rock specimens, and this planet will disappear!")
        if exp_pos!=a_pos:
                print("Thankfully the astronaut was not on planet", exp_pos,", so he is okay!")
        global num_explosions
        num_explosions=num_explosions+1
        for p in range(1,exp_pos):
            p_rock_gain=0
            for i in range(p,exp_pos+1):
                p_rock_gain=int(p_rock_gain)+int(p_rocks[i])
            p_rocks[p]=int(p_rock_gain)
        num_planets=num_planets-1
        p_rocks.remove(p_rocks[exp_pos])
        p_civlevel.remove(p_civlevel[exp_pos])
        p_fuel.remove(p_fuel[exp_pos])
        print()
        global a_alive
        global python_pos
        if exp_pos==python_pos:
                python_p=""
                python_pos=100  #some number outside the board, so it cannot be reached
                print("The planet that disappeared was python planet!! Oh well, keep playing.")
        elif python_pos>exp_pos:
                python_pos=python_pos-1
        if exp_pos==a_pos:
                a_alive=False
                print("Oh no! You are on planet #",exp_pos,"so you died!")
        elif a_pos>exp_pos:
                a_pos=a_pos-1
                
        else:
                show_board("after AMAZING explosion, still on turn num: ", turn)
        print()
    return num_planets,p_rocks,p_civlevel,p_fuel,a_pos,a_alive,python_pos

#END OF GAME RESULTS
def end_of_game_results(games,turn,python_planet,num_explosions):
        print("The game number", games,"just took place")
        show_board("end of game","")
        turn="end of game"
        if python_planet==True:
            show_astronaut(turn,a_name,a_pos,a_fuel,a_rocks,a_alive)
            print("You also reached PythonPlanet, so you won!!")
        elif a_alive==False:
            show_astronaut(turn,a_name,a_pos,a_fuel,a_rocks,a_alive)
        print(num_explosions,"explosions took place, adding rocks to various planets.")
        print()


#ROCK LIST TO BINARY      
def rock_list_to_binary(p_rocks):
    binary_lst=[]
    for i in range(len(p_rocks)):
        if int(p_rocks[i])%2==0:
            binary_lst.append(0)
        if int(p_rocks[i])%2==1:
            binary_lst.append(1)
    return binary_lst
    

#CONVERTING BINARY TO DECIMAL FOR FINAL NUMBER DISPLAY
def convert_binary_to_10(binary_lst):
    total=0
    for i in range(0, len(binary_lst)):
        decimal=(binary_lst[i])*pow(2,(len(binary_lst)-1-i))
        total=total+int(decimal)
    return total






##########################################################################################            
####################################### TOP LEVEL ########################################
##########################################################################################

import random as r


#WELCOME MESSAGE
print()
print("Welcome to the Planet, Aliens and Explosions Game! I hope you have fun!")
print("="*72)

print()
print()
play=input("Do you want to play? (y/n): ")
play=valid_input_yes_no(play)
print()
print()


global num_explosions
games=0
games_won=0


#PLAYER WANTS TO PLAY/GAME BEGINS

while play=="y":
#user wants to play

    #INITIALIZING VALUES FROM BOARD USER CHOOSES
    board=input("Type the name of board file including '.txt' or type d for default: ")

    #user chooses file 
    the_file=choosing_board(board)
    
    #file is opened
    listStrings = read_string_list_from_file(the_file)

    #file is converted into list
    planetdata=convert_to_individual(listStrings)           

    #individual lists are made
    p_civlevel=make_civlevel_list(planetdata)

    p_fuel=make_fuel_list(planetdata)

    p_rocks=make_rocks_list(planetdata)

    num_planets=len(p_civlevel)-1


    



####### BEGIN GAME ########
    
#RESETTING INITIAL VALUES FOR EACH GAME
    
    turn=""
    a_pos=""
    python_pos=""
    
    

    
    #COLLECTING INFO FROM USER
            
    show_board("just created",turn)

    print()
    print("Data for astronaut/player")
    print()

    #NAME AND CIVLEVEL
    a_name=input("What is your name? ")
    a_civlevel=input("What is your civilization level (0..3)? ")
    a_civlevel_range=list(range(4)) #the accepeted values for civlevel
    a_civlevel=valid_input_numbers(a_civlevel,a_civlevel_range)

    #INITIAL FUEL
    print()
    a_fuel=input("What is your initial amount of fuel (10..50)? ")
    a_fuel_range=list(range(10,51)) #accpeted values for fuel
    a_fuel=valid_input_numbers(a_fuel,a_fuel_range)


    #NUM TURNS
    print()
    tot_turns=input("How many turns would you like to play this game? (1..10) ")
    tot_turns_range=list(range(11))  #accpeted values for num turns
    tot_turns=valid_input_numbers(tot_turns,tot_turns_range)
    print()

    #PYTHON PLANET
    python_pos=input("Which planet shall be Python Planet (0.."+str(num_planets)+"), 0 no effect:")
    python_pos_range=list(range(num_planets+1))
    python_pos=valid_input_numbers(python_pos,python_pos_range)
    print()


    #EXPLOSIONS
    amaz_explosions=input("Would you like there to be Amazing explosions? (y/n): ")
    amaz_explosions=valid_input_yes_no(amaz_explosions)

    prop_exp_range=list(range(1,6))
    
    if amaz_explosions=="n":  #user doesnt want amazing explosions, but can choose to have mild
            mild_exp=input("Would you like there to be mild explosions? (y/n): ")
            if mild_exp=="y":
                print()
                prop_exp=input("Proportion of explosions? (1..5) ")
                prop_exp=valid_input_numbers(prop_exp,prop_exp_range)
    else:   #user wants amazing explosions so no mild ones happen
            prop_exp=input("Proportion of explosions? (1..5) ")
            prop_exp=valid_input_numbers(prop_exp,prop_exp_range)
            



    
    #### INITIALIZING FIRST TURN ####
    a_alive=True
    a_pos=0  #user starts on planet 0
    a_rocks=[]
    turn=1
    next_turn="y"
    python_planet=False
    num_explosions=0
    

    
        ######TURN OCCURING######
        
    while a_alive==True and turn<=tot_turns and a_fuel>0 and (python_planet==False): 
    #conditions for user to continue playing
        
        
        show_board("about to do turn num:",turn)
        
        show_astronaut(turn,a_name,a_pos,a_fuel,a_rocks,a_alive)
        print()


        if amaz_explosions=="y":
                amazing_explosions(a_pos,p_civlevel,prop_exp,turn,p_rocks,p_fuel,num_planets)
        else:
                if mild_exp=="y":
                    mild_explosion(a_pos,p_civlevel,prop_exp,turn,p_rocks)

        if a_alive==True:  #if astronaut is still alive after explosions, turn continues
                a_pos=roll_die(a_pos,num_planets,p_civlevel)

                if python_pos!=0:
                        python_planet=python_planet_reached(a_pos,python_pos)
                        #checking if user is on python planet

                    
                if python_planet==False: #if they are not turn continues
                    print()
                    print()

                    a_fuel=interacting_aliens(a_civlevel,a_pos,p_civlevel,a_fuel)
                    #interacting with aliens, gaining/losing fuel
                    print()
                    print()

                    collecting_rocks(a_rocks,p_rocks)

                    turn=turn+1 

                    print()
                    



    #END OF GAME MESSAGE#   #AFTER TURN WHLE LOOP#

    #figuring out why the game ended
    print()
    if a_fuel<=0:
        print("Game over! You ran out of fuel and are stranded!")
    elif turn>tot_turns:
        print("Game over! You do not have any turns left!")
    elif a_alive==False:
        print("Oh no! The astronaut is dead! Game over!")
    elif python_planet==True:
        print("WOOHOO! You won the game by reaching Python Planet!!!!")
        games_won=games_won+1

        

    games=games+1
    print()
    
    print("END OF GAME RESULTS")
    print()

    end_of_game_results(games,turn,python_planet,num_explosions)

    
    
    #does the user want to play again
    play=input("Would you like to play again? (y/n): ")
    play=valid_input_yes_no(play)
    print()
    print()
    




#RESULTS OF ALL GAMES
#if user does not want to play again

print()
print("*** END OF ALL GAMES RESULTS ***")
print()

print("The user played", games, "games in total")
print("of those, the astronaut won", games_won)
print()


print("To conclude, the program will do a conversion from binary to decimal,")
print("using the list of rock specimens in the last game board as the source!")
print()

print("  List with rock specimens: ", p_rocks)
binary_lst=rock_list_to_binary(p_rocks)
print("  Corresponding Binary: ", binary_lst)
total=convert_binary_to_10(binary_lst)
print()
print("which converted to decimal is: ", total)

print()
print()
print("Thank you for playing the Planets, Aliens and Explosions Game! Come back soon!")
print("Goodbye... :)")
print("="*80)





    
      
