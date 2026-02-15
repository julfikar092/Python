#Task 1: Student Dictionary Management


#1- Create a dictionary named 'student' with keys: name, age, department, cgpa, is_active.
student={
    "name":"Julfikar Rahman", 
    "age": 32, 
    "department" : "Sofware Engineering", 
    "cgpa": 3.43, 
    "is_active":True 
}

#2. Print the full dictionary, student name, all keys, and all values.
print(student)

print("\nName of the student is: ",student["name"])

print("\nAll the keys are:")
for k in student.keys():
    print(k)
   
print("\nAll the values are:")
for v in student.values():
    print(v)

""" 
output: 

name : Julfikar Rahman
age : 32
department : Sofware Engineering
cgpa : 3.43
is_active : True

Name of the student is:  Julfikar Rahman

All the keys are:
name
age
department
cgpa
is_active

All the values are:
Julfikar Rahman
32
Sofware Engineering
3.43
True

"""

#3. Update cgpa and add a new key 'semester'.

student["cgpa"] = 3.63
student['semester'] = '5th'

print(student)

"""  
output: 

{'name': 'Julfikar Rahman', 'age': 32, 'department': 'Sofware Engineering', 'cgpa': 3.63, 'is_active': True, 'semester': '5th'}

"""

#4. Use a for loop to print all key-value pairs in format: key : value.

for key,value in student.items():
    print(f"{key} : {value}")

"""  
output: 

name : Julfikar Rahman
age : 32
department : Sofware Engineering
cgpa : 3.63
is_active : True
semester : 5th

"""


#Task 2: Set Operations Program

#1. Create two sets A = {1,2,3,4,5} and B = {4,5,6,7,8}.
A = {1,2,3,4,5}
B = {4,5,6,7,8}

#2. Perform and print: Union, Intersection, Difference (A - B).

print("Union of A and B: ",A.union(B))
print("Intersection of A and B: ",A.intersection(B))
print("Difference of A and B: ",A.difference(B))

"""
output: 

Union of A and B:  {1, 2, 3, 4, 5, 6, 7, 8}
Intersection of A and B:  {4, 5}
Difference of A and B:  {1, 2, 3}

"""
#3. Add two new elements to A and remove one element.
B_new = {9,15}
A.update(B_new)
print("After adding new set of two values with A: ",A)

A.remove(5)
print("Set A after removing 5: ",A)

""" 
output: 

After adding new set of two values with A:  {1, 2, 3, 4, 5, 9, 15}
Set A after removing 5:  {1, 2, 3, 4, 9, 15} 

"""

#4. Check if 3 exists in A.

if 3 in A:
    print("Yes 3 exists in set A")
else:
    print("3 is not exists in set A")

""" 
Output:

Yes 3 exists in set A

 """


#Task 3: Grade & Eligibility System

mark = int(input("Enter the number: "))
if(mark>= 80):
    print("A+")
elif(mark>=70 and mark<=79):
    print("A")
elif(mark>=60 and mark<=99):
    print("A-")
else:
    print("Fail")

""" 
output: 

Enter the number: 96
A+

Enter the number: 33
Fail

"""

#Task 4: Loop Practice

""" 
output: 



"""

#Task 5: List Comprehension & Nested Loop

""" 
output: 



"""