studentweightslist = list()                                 # Created an empty student weights list
N = int(input(" Enter Number Of Students"))                 # Reading the number of students input from user
for i in range(N):                                          #Running a for loop
    studentweights = float(input("Enter the weight of Student of Student" + str(i+1)))   # Taking the student weights in lbs from user
    studentweightslist.append(studentweights*0.453592)                                   # converting weights in kgs and appending them
studentweightslistwithprecision = ['%.2f' % elem for elem in studentweightslist]         #  converting student weights list to list with 2 decimal
print(studentweightslistwithprecision)                                                   # Printing the student weights in kgs with 2 decimal places

