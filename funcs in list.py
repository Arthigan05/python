'''Sub= ["Maths" , "Tamil" , " Science"]

Sub[3] = "IT"
print(Sub)

Subject= ["Maths" , "Tamil" , " Science"]
Subject.append("IT")
print(Subject) 

Subject= ["Maths" , "Tamil" , " Science"]
Subject.insert(2,"IT")
print(Subject) 

Subject= ["Maths" , "Tamil" , " Science"]
Subject.extend(["It", "Physics", "Chemistry"])
print(Subject) 

Subject.pop(2)
print(Subject) 

Subject.pop()  #last value out
print(Subject)  

Subject= ["Maths" , "Tamil" , " Science"]
if "Math" in Subject:
    Subject.remove("Math")

print(Subject)

if "Maths" in Subject:
    Subject.remove("Maths")

print(Subject) 

Subject= ["Maths" , "Tamil" , " Science"]
Subject.clear()
print(Subject) 

Subject= ["Maths" , "Tamil" , " Science"]
print(Subject.index("Tamil"))
#print(Subject.index("English"))
print(Subject.find("Tamil")) #No find fucntion in list 

Subject= ["Maths" , "Tamil" , " Science"]
Subject.sort() #sorts in alphabetical order
print(Subject) 

Subject= ["Maths" , "Tamil" , " Science" , "IT"]
Subject.reverse()
print(Subject) 

Subject= ["Maths" , "Tamil" , " Science" , "IT"]
Subject.sort(reverse = True)
print(Subject) 

Marks = [ 30 , 50, 68, 73, 80 , ]

print(max(Marks))
print(min(Marks))
print(sum(Marks))

MarksD = Marks.copy()
print(MarksD)

MarksD = Marks
print(MarksD)


MarksD[2] = 45
print(MarksD)
print(Marks) '''











