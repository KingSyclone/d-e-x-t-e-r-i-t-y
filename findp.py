#Locations database reference here
#if location in database
lastseen = input("The door last passed through : ")
alarm = 0
#activate camera
#can camera see student at location of transmission
#if location in database
ctrans = input("The location where the RFid is transmitting data from : ")
#tell camera to scan
pthere = input("Is the same person there? (Y/N) ")
if lastseen == ctrans and pthere == "Y":
    print("The student is still in "+ ctrans+ ".")
    alarm = 0
elif lastseen == ctrans and pthere == "N":
    print("The student is no longer in "+ ctrans+ ".")
    alarm = 1
else:
    print ("This is not a valid input.")