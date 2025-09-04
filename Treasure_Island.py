#print(r''' ... ascii art ... ''')   # am scurtat să nu fie prea lung, dar tu îl păstrezi integral
print(r'''
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

end_game = 0    #Suppose that the game had not ended

#.strip eliminate spaces before and after the word and .lower makes every letter in a small one(in C/C++ ch += 32)
first_decision = input("What's your direction, left or right?\n").strip().lower()
ok_first_direction = 0

if first_decision == "left" or first_decision == "right":
    ok_first_direction = 1

while ok_first_direction == 0:
    if ok_first_direction == 0:
        first_decision = input("You should enter a valid one, left or right!\n").strip().lower()
        if first_decision == "left" or first_decision == "right":
            ok_first_direction = 1

if first_decision == "right":
    print("Game over!\n")
    end_game = 1        #We found that the game finished

if end_game == 0:
    second_decision = input("What are you doing, swim or wait?\n").strip().lower()
    ok_second_decision = 0

    if second_decision == "swim" or second_decision == "wait":
        ok_second_decision = 1

    while ok_second_decision == 0:
        if ok_second_decision == 0:
            second_decision = input("You should enter a valid one, swim or wait!\n").strip().lower()
            if second_decision == "swim" or second_decision == "wait":
                ok_second_decision = 1

    if second_decision == "swim":
        print("Game over!\n")
        end_game = 1

if end_game == 0:
    third_decision = input("wich door are you choosing, red, blue or yellow?\n").strip().lower()
    ok_third_decision = 0

    if third_decision == "red" or third_decision == "blue" or third_decision == "yellow":
        ok_third_decision = 1

    while ok_third_decision == 0:
        if ok_third_decision == 0:
            third_decision = input("You should choose a valid one, red, blue or yellow!\n").strip().lower()
            if third_decision == "red" or third_decision == "blue" or third_decision == "yellow":
                ok_third_decision = 1

    if third_decision == "red" or third_decision == "blue":
        print("Game over!\n")
        end_game = 1

if end_game == 0 and third_decision == "yellow":
    print("Congratulations! You are the winner!\n")
    #end_game = 1
