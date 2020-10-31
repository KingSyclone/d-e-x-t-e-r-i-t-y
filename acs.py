noofinputs = int(input("Input number of people : "))
studs = int(input("Please input number of students: "))
admin = int(input("Please input number of administrators: "))
teach = int(input("Please input number of teachers: "))
totale = studs + admin + teach
if totale == noofinputs:
    if totale >= 1:
        print("Turn on lights.")
    if studs >= 5 or teach >= 1 or admin >= 1:
        print("Start computer and whiteboard.")
    if totale >= 5:
        print("Start climate acclimatization.")
        temp = int(input("Please input outside temperature in Celsius: "))
        optemp = temp - 22
        if optemp > 0:
            print ("Decrease temperature by "+ str(optemp) +" degrees.")
        elif optemp < 0:
            print("Increase temperature by " + str(-optemp) + " degrees.")
        else:
            print ("Optimum temperature is reached.")
else:
    print ("Total number of entries do not match.")