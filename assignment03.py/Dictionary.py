
# # #...... student dictionary
# # student={"name":"vivek","age":20,"course":"python","Branch":"cse"}
# # print(student)


# # # ...add and update student dictionary
# # student={"name":"vivek","age":20,"course":"python","Branch":"cse"}
# # student["age"] = 21
# # print(student)


# #,,,,,////
# marks={"math": 85, "science": 90, "english": 88}
# highest_mark = max(marks.values())
# print(highest_mark)

# #...frequency of each character in a string
# text = "hello world"
# char_frequency = {}
# for char in text:
#     if char in char_frequency:
#         char_frequency[char] += 1
#     else:
#         char_frequency[char] = 1
# print(char_frequency)


# #....frequency of each word in a sentence
# sentence = "hello world hello"
# word_frequency = {}
# words = sentence.split()
# for word in words:
#     if word in word_frequency:
#         word_frequency[word] += 1
#     else:
#         word_frequency[word] = 1
# print(word_frequency)



# # store multiple students using a list of dictionaries
# students = [
#     {"name": "vivek", "age": 20, "course": "python", "Branch": "cse"},
#     {"name": "suraj", "age": 22, "course": "java", "Branch": "it"},
#     {"name": "neeraj", "age": 21, "course": "c++", "Branch": "ece"}
# ]
# print(students)


#....,...create a simple phonebook
# phonebook = {
#     "vivek": "123-456-7890",  
#    "suraj": "987-654-3210",
#    "neeraj": "222333-4444-3344"
# }
# print(phonebook)   


#search for student by roll number
# students = [
#     {"roll_number": 1, "name": "vivek", "age": 20, "course": "python", "Branch": "cse"},
#     {"roll_number": 2, "name": "suraj", "age": 22, "course": "java", "Branch": "it"},
#     {"roll_number": 3, "name": "neeraj", "age": 21, "course": "c++", "Branch": "ece"}
# ]
# print(students)




#....student who scored above 80.
students = [
    {"name": "vivek", "marks": 85}, 

    {"name": "suraj", "marks": 75},

    {"name": "neeraj", "marks": 90}

]
high_scorers = [student for student in students if student["marks"] > 80]
print(high_scorers)         



#average marks of students
students = [
    {"name": "vivek", "marks": 85},
    {"name": "suraj", "marks": 75},
    {"name": "neeraj", "marks": 90}
]
average_marks = sum(student["marks"] for student in students) / len(students)
print(average_marks)    
