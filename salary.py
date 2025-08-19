''' tax 
 50 000 3
 50 000 to 100 000 5
 100 000 to 300 000 8
 1000000 10 '''


salary = [1000067, 2000078, 3000009, 5000090, 70000067, 5000008, 1000000, 2000000, 2000800,200000,500000, 1007000]
month = [1,2,3,4,5,6,7,8,9,10,11,12]
monthName = ["January", "February", "March", "April","May","June","July","August","September", "October", "November", "December"]
tax = [0,0,0,0,0,0,0,0,0,0,0,0]
net_salary = [0,0,0,0,0,0,0,0,0,0,0,0]

'''for i in salary:
    if i <= 50000:
        tax = i * 0.03
    elif i > 50000 and i <= 100000:
        tax = i * 0.05
    elif i > 100000 and i <= 300000:
        tax = i* 0.08
    elif i > 300000:
        tax = i * 0.1
    
    
    print(month, salary , tax, net_salary) '''
Total_salary = 0
print(f"monthName        salary          tax     net_salary ")
for i in month:
    if salary[i-1]<= 50000:
        tax[i-1]=int(salary[i-1]*0.03)
    elif salary[i-1]> 50000 and salary[i-1] <= 100000:
        tax[i-1]=int(salary[i-1]*0.05)
    elif salary[i-1]> 100000 and salary[i-1] <= 300000:
        tax[i-1]=int(salary[i-1]*0.08)
    elif salary[i-1] > 300000:
        tax[i-1]=int(salary[i-1]*0.1)
    net_salary[i-1]= salary[i-1] - tax[i-1]
    Total_salary = Total_salary+net_salary[i-1]
    
    
    print(f"{monthName[i-1]:<10}  {salary[i-1]:>12} {tax[i-1]:>10} {net_salary[i-1]:>12} ")
print(Total_salary)
    
    
    
    

    
    

        
         
