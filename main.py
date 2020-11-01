card_input = input('Please enter your level : ')
card_number = input('Please enter card number : ')
verify = 0
kicker = 0
from os import system, name
from time import sleep
def clear():
    _ = system('cls')
while kicker < 3:
    if card_input == 'A':
        print("Administrator")
        face_scan = input("Face id received : ")
        if face_scan == card_number:
            name = input("Please enter your name: ")
            print("Welcome " + name + ", you have been registered")
            verify = 1
            iaccess = "A"
        else:
            print("The card is not matching your face. Please try again.")
            kicker = kicker + 1

    elif card_input == 'T':
        print("Teacher")
        face_scan = input("Face id received : ")
        if face_scan == card_number:
            name = input("Please enter your name: ")
            print("Welcome " + name + ", you have been registered")
            verify = 1
            iaccess = "T"
        else:
            print("The card is not matching your face. Please try again.")
            kicker = kicker + 1

    elif card_input == 'S':
        print("Student")
        face_scan = input("Face id received : ")
        if face_scan == card_number:
            name = input("Please enter your name: ")
            print("Welcome " + name + ", you have been registered")
            verify = 1
            iaccess = "S"
        else:
            print("The card is not matching your face. Please try again.")
            kicker = kicker + 1
    else:
        print("This is not a valid level. Please try again.")
        kicker = kicker + 1
if kicker == 3:
    print ("You have failed too many times. ")
    quit ()
idkman = 0
while idkman == 0:
    function = int(input(" 1)Check Internet Access What would you like to do? "))
    if function == 1:
        print("Checking internet access level")
        if iaccess == 'A':
            print("Administrator Internet Access")
            sleep(10)
            clear()
        elif iaccess == 'T':
            print("Teacher Internet Access")
            sleep(10)
            clear()
        elif iaccess == 'S':
            print("Student Internet Access")
            sleep(10)
            clear()
    elif function == 2:
        print("Start pollution sensors")
        plevel = int(input("Please input outside pollution level ppm: "))
        if 0 <= plevel <= 350:
            print("The outside has a pollution level of " + str(plevel) + " ppm. It is very safe to go out. ")
            sleep(20)
            clear()
        elif 350 <= plevel <= 1000:
            print("The outside has a pollution level of " + str(plevel) + " ppm. It is safe to go out. ")
            sleep(20)
            clear()
        elif 1000 <= plevel <= 2000:
            print("The outside has a pollution level of " + str(plevel) + " ppm. It is advised to not stay out for too long. ")
            sleep(20)
            clear()
        elif 2000 <= plevel <= 5000:
            print("The outside has a pollution level of " + str(plevel) + " ppm. It is advised to take a mask. ")
            sleep(20)
            clear()
        elif 5000 <= plevel <= 40000:
            print("The outside has a pollution level of " + str(plevel) + " ppm. It is advised not to go out. ")
            sleep(20)
            clear()
        elif 40000 < plevel:
            print("The outside has a pollution level of " + str(plevel) + " ppm. Please do not go out. You will die. ")
            sleep(20)
            clear()
        else:
            print("This is not a valid level.")
            sleep(10)
            clear()
    elif function == 3:
        quit()
    else:
        print ("That is not valid input")
        sleep(10)
        clear()

