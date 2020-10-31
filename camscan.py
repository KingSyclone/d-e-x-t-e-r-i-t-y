card_input = input('Please enter your level : ')
card_number = input('Please enter card number : ')
alarm = 0

if card_input == 'A':
    print("Administrator")
    face_scan = input("Face id received : ")
    if face_scan == card_number:
        # search for number in database
        # take name from database
        name = "Null Null"
        print("Welcome " + name + ", you have been registered")
        # send info to database to register
    else:
        print ("The card is not matching your face. You are an impostor.")
        alarm = 1


elif card_input == 'T':
    print("Teacher")
    face_scan = input("Face id received : ")
    if face_scan == card_number:
        # search for number in database
        # take name from database
        name = "Null Null"
        print("Welcome " + name + ", you have been registered")
        # send info to database to register
    else:
        print("The card is not matching your face. You are an impostor.")
        alarm = 1

elif card_input == 'S':
    print("Student")
    face_scan = input("Face id received : ")
    if face_scan == card_number:
        # search for number in database
        # take name from database
        name = "Null Null"
        print("Welcome " + name + ", you have been registered")
        # send info to database to register
    else:
        print("The card is not matching your face. You are an impostor.")
        alarm = 1
else:
    print("This is not a valid level. You are an impostor.")
    alarm = 1