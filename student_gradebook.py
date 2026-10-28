students  = {
"Alice" : 85,
"Rose" : 92,
"Luke" : 78,
"Mike" : 95,
"Emma" : 88
}

total = 0 

for score in students.values():
    total += score
    average = total / len(students)

print("STUDENT GRADE BOOK")
print("The class average is :", round(average,2))

highest = max(students.values())
lowest = min(students.values())

for name, score in students.items () :
    if score == highest:
        print("The student who got the highest score in the class",name,"-", score)
    if score == lowest :
        print ("the student who has gotten the lowest score",name,"_", score)

search_name = input("enter student name: ").strip()
for name in students: 
    if name.lower() == search_name.lower():
        search_name = name 
        break
score = students.get(search_name)
if score is not None: 
    print(search_name,"'s score is  - ",score)
else : 
    print("This student is not found in this gradebook")
