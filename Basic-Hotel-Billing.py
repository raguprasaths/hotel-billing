#basic hotel billing
print("select menu")
menu=int(input("1.COFFEE \n2.TEA \n3.COLD COFFEE \n4.MILK SHAKE \n5.BOURBON COFFEE\n"))

if menu==1:

    q=int(input("you select a coffee enter your quantity"))
    price = 10
    total = q*price
    print("Total amount:",total)
elif menu==2:
    q = int(input("you select a TEA enter your quantity"))
    price = 15
    total = q*price
    print ("Total amount:",total)
elif menu == 3:
    q = int(input("you select a COLD COFFEE enter your quantity"))
    price = 20
    total = q*price
    print ("Total amount:",total)
elif menu == 4:
    q = int(input("you select a MILK SHAKE enter your quantity"))
    price = 25
    total = q*price
    print ("Total amount:",total)
elif menu == 5:
    q = int(input("you select a BOURBON COFFEE enter your quantity"))
    price = 35
    total = q*price
    print ("Total amount:",total)
else:
    print("invalid ")
