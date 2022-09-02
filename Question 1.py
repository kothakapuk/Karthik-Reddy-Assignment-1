ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]    # Student ages list
print(ages)         # Printing student ages
ages.sort()         # Sorting the Ages
print(ages)         # Printing sorted student ages list
a = min(ages)       # Finding the min ages and storing in Variable a
b = max(ages)       # Finding the max ages and  Storing in Variable b
print(a)            # Printing value stored a
print(b)            # Printing value stored b
ages.append(a)      # Adding the min values to list
print(ages)         # Printing the ages list
ages.append(b)      # Adding max values to list
print(ages)         # Printing the ages list
c = len(ages)       # Finding length of list
print(c)            # Printing the length
d = (c-1)//2        # Finding the floor division
print(d)            # Printing value of d
median1 = (ages[d] + ages[d+1])/2    # Finding the median
print(median1)                       # Printing median value
sum1 = sum(ages)                     # Finding sum of ages
print(sum1)                          # Printing sum of ages
avg = sum1/c                         # Finding Average
print(avg)                           # Printing Average
range1 = b-a                         # Finding Range
print(range1)                        # Printing Range
