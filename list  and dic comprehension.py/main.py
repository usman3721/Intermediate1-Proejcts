
import pandas as pd
from random import randint

# numbers=[1,2,3]
# new_list=[]
# for n in numbers:
#     add_1=n+1
#     new_list.append(add_1)

#LIST COMPREHENSION
# new_list=[n+1 for n in numbers]
# print(new_list)

#String as list
# name="Usman"
# letter_list=[letter for letter in name]
# print(letter_list)


#Range as list
# new_list=[num*2 for num in range(1,5)]
# print(new_list)

#Conditional list comprehension
names=["usman", "jaabir", "yuusuf", "goih", "fatai" ]
# short_names=[name for name in names if len(name) < 5]
# print(short_names)

# greaterThanFive=[name.upper() for name in names if len(name) > 5]
# print(greaterThanFive)


# numbers=[1,1,2,3,5,8,13,21,34,55]
# squared_numbers=[n*n for n in numbers]
# squared_numbers=[n**2 for n in numbers]
# print(squared_numbers)

# result=[num for num in numbers if num%2==0]
# print(result)



#HARD EXERCISE
# with open("file2.txt") as file1:
#     print(file1)
    # read1=file1.readlines()    
# with open("/Users\hp\Desktop/100DaysOfCode by Angela Yu\list  and dic comprehension.py/file1.txt") as file2:
#     read2=file2.readlines()
# result=[int(num.strip()) for num in read1 if num in read2]
# result=[int(num) for num in read1 if num in read2]
# print(result)
# /Users\hp\Desktop/100DaysOfCode by Angela Yu\list  and dic comprehension.py/file2.txt"
# print(file2)
# result=[num for num in file1 if num in file2]
# print(result)



#DICTIONARY COMPREHENSION
# student_score={student:randint(1,100) for student in names}
# passed_student={student:score for (student,score) in student_score.items() if score >=60 }
# print(passed_student)


# sentence="What is the Airspeed Velocity of an Unladen Swallow?"
# splitted=sentence.split()
# for word in splitted:
#     print(word) , print(len(word))  
# result={word:len(word) for word in sentence.split()}
# print(result)




# weather={
#     "Monday": 12,
#     "Tuesday":14,
#     "Wednesday":15,
#     "Thursday":14,
#     "Friday":21,
#     "Saturday":22,
#     "Sunday": 24


# }
# weather_f={days:temp_c*9/5+32 for (days,temp_c) in weather.items() }
# print(weather_f)





#LOOPING THRIUGH PANDAS DATAFRAME
student={
    "student":["Angela", "james","lily"],
    "score":[56, 76, 98]
}

student_data_frame=pd.DataFrame(student)
# print(student_data_frame)
for (key,value ) in student_data_frame.items():
    print(value)


# looping through rows of a data frame
for (index,row) in student_data_frame.iterrows():
    if (row.student)=="Angela":
        print(row.score)



#NATO PHONETIC OBJECT
