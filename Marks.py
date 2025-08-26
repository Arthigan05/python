Marks_list = [[50,60 , 70], [30,60,90],[40,60,70]]
Stu_Name = ["H3" , "H2", "H1"]
Total = [0,0,0]
Average = [0,0,0]
Stu_Number = [1,2,3]
result = [0,0,0]


print(f"Student Name  Physics   Maths    Chemistry  Total  Average  Result")
for i in Stu_Number:
    p = (Marks_list[0][i-1], Marks_list[1][i-1],Marks_list[2][i-1])
    Total = Marks_list[0][i-1] + Marks_list[1][i-1] + Marks_list[2][i-1]
    Average = (Marks_list[0][i-1] + Marks_list[1][i-1] + Marks_list[2][i-1])/3
    Average = int(Average)
    if Average >= 75:
        result = "A"
    elif Average <75 and Average >= 65:
        result = "B"
    elif Average < 65:
        result = "C"
    
    print(f"{Stu_Name[i-1]:<12} {Marks_list[0][i-1]:>8} {Marks_list[1][i-1]:>8} {Marks_list[2][i-1]:>8} {Total:>8} {Average:>8} {result:>8}")

    
    
    
    
    

