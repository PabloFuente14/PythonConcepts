matrix = [[col for col in range(5)] for row in range(5)]
print(matrix)

#Create a list comprehension that generates a list of squares of numbers from 1 to 10.
squares = [i**2 for i in range(1,11)]
print(squares)

#Given the list words = ['apple', 'banana', 'cherry', 'date'], create a list comprehension that converts all words to uppercase.
words = ['apple', 'banana', 'cherry', 'date']
words_converted = [i.upper() for i in words]
print(words_converted)

#Create a list comprehension that generates a list of even numbers from 1 to 20.
even_numbs = [i for i in range(1,21) if i%2 ==0]
print(f"Even nums: {even_numbs}" )

#Given the list numbers = [5, 8, 12, 15, 20, 25, 30], create a list comprehension that replaces numbers divisible by 5 with "Divisible by 5", and keeps the other numbers as they are.
numbers = [5, 8, 12, 15, 20, 25, 30]
replacing_list = ["Divisible by 5" if i%5 == 0 else i for i in numbers]
print(replacing_list)

#Given the list temperatures = [32, 40, 50, 65, 72, 85, 90, 100], create a list comprehension that replaces temperatures greater than or equal to 85 with the string "Hot", and keeps the other temperatures as they are.
temperatures = [32, 40, 50, 65, 72, 85, 90, 100]
hot_temps = ["Hot" if i >= 85 else i  for i  in temperatures]
print(f"Hot temps: {hot_temps}")

#You are given the list of dictionaries, where each dictionary contains information about students and their grades:
# students = [
#    {'name': 'Alice', 'grade': 85},
#    {'name': 'Bob', 'grade': 58},
#    {'name': 'Charlie', 'grade': 90},
#    {'name': 'David', 'grade': 72},
#    {'name': 'Eva', 'grade': 65}
#]
#Create a list comprehension that:
#Replaces students with grades less than 60 with the string "Fail".
#Replaces students with grades between 60 and 75 (inclusive) with "Pass".
#Keeps students with grades higher than 75 unchanged (i.e., retains the original dictionary).
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 58},
    {'name': 'Charlie', 'grade': 90},
    {'name': 'David', 'grade': 72},
    {'name': 'Eva', 'grade': 65} ]
evaluations = [{'name': i['name'] , 'grade': "fail"} if i['grade'] < 60 else {'name': i['name'] , 'grade': "Pass"} if i['grade'] >=60 and i['grade']<= 80 else i for i in students]
print(evaluations)

#In the same list comprehension, instead of just replacing "Fail" or "Pass", modify the dictionary by adding a key 'status' and set its value to "Fail" or "Pass" accordingly. 
# Keep the dictionary unchanged for grades above 75.
evaluations1 = [{'name': student['name'], 'grade': student['grade'] , 'status': 'fail'} if student['grade']<60 else {'name': student['name'], 'grade': student['grade'] , 'status': 'pass'} if student['grade'] >=60 and student['grade'] <=80 else {'name': student['name'], 'grade': student['grade']} for student in students]

#cleaner code with the **. This packs all the key:value paris in the dict and spreads them into the new dict
evaluations2 = [{**student, 'status':'fail'} if student['grade']<60 else {**student, 'status':'pass'} if student['grade'] >=60 and student['grade'] <=80 else {**student} for student in students ]
print(evaluations1)
print(f"\n {evaluations2}")
