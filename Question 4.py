it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}    # Created it_companies set
A = {19, 22, 24, 20, 25, 26}                                                              # Created A Set
B = {19, 22, 20, 25, 26, 24, 28, 27}                                                      # Created B set
age = [22, 19, 24, 25, 26, 24, 25, 24]                                                    # Created Age Set
len1 = len(it_companies)                                                                  # Finding the length of it_companies set
print(len1)                                                                               # Printing the length of it_companies set
it_companies.add("Twitter")                                                               # Added Twitter to it_companies
print(it_companies)                                                                       # Printing the it_companies
it_companies1 = {"TCS", "Accenture", "Deloitte", "Wipro", "Infosys", "Cap Gemini"}        # Created Multiple it_companies1 set
it_companies.update(it_companies1)                                                        # Updated it_companies1 set
print(it_companies)                                                                       # Printing the it_companies set
it_companies.remove("Accenture")                                                          # Remove one company from it_companies
print(it_companies)                                                                       # Printing after remove


# Difference between remove and discard is in remove() method it will raise and error


print(A.union(B))                                     # Joining A with B
print(A.intersection(B))                              # Finding A Intersection B
print(A.issubset(B))                                  # Finding whether A Subset of B
print(A.isdisjoint(B))                                # Finding whether A and B are disjoint sets
print(A.union(B))                                     # Joining A With B
print(B.union(A))                                     # Joining B with A
print(A.symmetric_difference(B))                      # Finding Symmetric difference between A and B
A.clear()                                             # Deleting Set A Completely
print(A)                                              # Checking its deleted or not
B.clear()                                             # Deleting Set B Completely
print(B)                                              # Checking its deleted or not
ageset = set(age)                                     # Converting the list to set
print(ageset)                                         # Printing Converted Set
listlen = len(age)                                    # Finding Length of list
print(listlen)                                        # Printing length of list
setlen = len(ageset)                                  # Finding length of set
print(setlen)                                         # Printing length of set
