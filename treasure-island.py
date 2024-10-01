print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You have arrived at a crossroads. Which direction would you like to go? ' 
                'Please type "left" or "right".\n').lower()

if choice1 == "left":
    choice2 = input('You have come to a beautiful, crystal blue lake. There is an island in the middle, and a dock nearby. Would you like to wait for a boat, or try to swim across?'
                    'Type "wait" to wait for a boat.'
                    'Type "swim" to swim across.\n').lower()

    if choice2 == "wait":
        choice2 = input("Soon enough, a ferryman comes and whisks you onto his boat. He\'s a chatty fellow, telling you all about the nearby area before dropping you off at a clearing on the island")
        choice3 = input('Looking around the clearing, you notice a building with three coloured doors; red, blue, and yellow. Which door will you go through?'
                        'Which colour will you choose?\n').lower()
        if choice3 == "red":
            print("No sooner do you enter the red door does it lock behind you.' "
                  "A pillar of flames ignites, surrounding you immediately. GAME OVER")
        elif choice3 == "yellow":
            print("You've come this far... surely yellow means good luck, right? You enter the door... and find heaps and heaps upon treasure! YOU WIN!")
        elif choice3 == "blue":
            print("Blue is a vibrant colour, full of life... Surely this must be the right door! As you enter, you notice the smell of wet beasts... They're very hungry, and you're very delicious. GAME OVER")
        else:
            print("That colour doesn\'t exist! A wizard pops out of no where and turns you to dust... At least you look cool blowing in the wind now. GAME OVER")

    else:
        print("You dive into the water, confident about your swimming abilities... but suddenly you get a leg cramp! As you fall to the floor of the lake you think to yourself that you really should have stretched first... GAME OVER!")

else:
    print("You decide to go right. No sooner do you make your decision and set one foot forward do you fall in a trap. Laying there clutching your ankle - which you are almost sure is broken - you hear a neerdowell mumble something about catching a hairless bear... GAME OVER")