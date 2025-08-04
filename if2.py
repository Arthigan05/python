'''stu_marks = int(input("Enter your marks"))

print(stu_marks)
if stu_marks > 75:
    print("A")
elif stu_marks > 65: 
    print("B")
elif stu_marks > 55:
    print("C")
elif stu_marks >= 45:
    print("D")
elif stu_marks < 45:
    print("Fail")'''
    
'''stu_marks = int(input("Enter your marks"))
if stu_marks<= 100 and stu_marks >=0:
    if stu_marks > 75:
        print("A")
    else :
        if stu_marks > 65:
            print("B")
        else :
                if stu_marks >= 45:
                    print("C")
                else:
                    if stu_marks < 45:
                        print("Fail")
else :
    print("invalid marks")'''
    
    
Get_minutes = int(input("Enter talked minutes"))
if 0 < Get_minutes: 
    if 0 < Get_minutes <= 30 :
        Total = Get_minutes * 2 
        print("Your bill is " + str(Total)) 
    else :
        if 30 < Get_minutes <= 60:
            Total = 30*2 +( Get_minutes-30)*1.5
            print("Your bill is " + str(Total)) 
        else :
            if 60 < Get_minutes <= 120:
                Total = 30 * 2 + 30 *1.5 + (Get_minutes-60)* 1
                print("Your bill is " + str(Total)) 
            else:
                if Get_minutes >120:
                   Total = 30*2 + 30 *1.5 + 60*1 + (Get_minutes - 120)*0.5
                   print("Your bill is " + str(Total)) 
else :
    print("invalid number")

