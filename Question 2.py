dog = dict()                                       # Created Empty dog Dictionary
dog["name"] = "Pomeranian"                         # Adding name of dog
dog["colour"] = "White"                            # Adding Colour of dog
dog["breed"] = "Spitz type"                        # Adding breed type
dog["legs"] = 4                                    # Adding Dogs legs
dog["age"] = 6                                     # Adding dog age
print(dog)                                         # Printing dog dictionary

student = dict()                                   # Created empty student dictionary
student["first_name"] = "Karthik"                  # Adding First Name
student["last_name"] = "Kothakapu"                 # Adding Last Name
student["gender"] = "Male"                         # Adding Gender
student["age"] = 27                                # Adding Age
student["marital status"] = "Single"               # Adding Marital Status
student["skills"] = ["Java", "C", "Python"]        # Adding Student Skills
student["country"] = "USA"                         # Adding Country
student["city"] = "Leawood"                        # Adding City
student["address"] = "2104 west, 138th street, Leawood" # Adding Student Address
print(student)                                          # Printing Student Details
len1 = len(student)                                     # Finding length of student dictionary
print(len1)                                             # Printing length of student dictionary
print(student["skills"])                                # Printing of student skills
print(type(student["skills"]))                          # Printing type of student skills
student["skills"].extend(["Machine Learning", "AI", "DBMS"]) # Modifying Student Skills
print(student['skills'])                                     # Printing skills of student dictionary
print(student.keys())                                        # Printing student dictionary keys as list
print(student.values())                                      # Printing the Student dictionary vales as list