lastseen = input("The door last passed through : ")
ctrans = input("The location where the RFid is transmitting data from : ")
pthere = input("Is the same person there? (Y/N) ")
if lastseen == ctrans and pthere == "Y":
    print("The student is still in "+ ctrans+ ".")
elif lastseen == ctrans and pthere == "N":
    print("The student is no longer in "+ ctrans+ ".")
else:
    print("This is not a valid input.")