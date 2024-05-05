#1. Python List Transformation
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

#Task 1:
grades.sort(reverse=True) 
print(grades)

#Task 2:
import numpy

avg_grade = numpy.average(grades)
print("The average grade is:")
print(avg_grade)

#Task 3:
grades[2]= "Failed"
grades[4]= "Failed"
grades[8]= "Failed"
print(grades)

