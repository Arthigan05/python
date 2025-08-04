Get_units = int(input("Enter units used"))

if 0 < Get_units: 
    if 0 < Get_units <= 90 :
        Total = Get_units * 7
        print("Your bill is " + str(Total)) 
    else :
        if 90 < Get_units <= 150:
            Total = 90*7 +( Get_units-90)*10
            print("Your bill is " + str(Total)) 
        else :
            if 150 < Get_units <= 300:
                Total = 90 * 7 + 60 *10 + (Get_units-150)* 15
                print("Your bill is " + str(Total)) 
            else:
                if Get_units >300:
                   Total = 90 * 7 + 60 *10 + 150 * 15 + (Get_units - 300)*15
                   Final = Total*103/100
                   print("Your bill is " + str(Final)) 
else :
    print("invalid number")
