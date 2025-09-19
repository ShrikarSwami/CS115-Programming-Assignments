def add_student(roster, name):
    """
    Makes a new copy of a roster and adds a student's name 
    to that new copy
    """
    copy = roster
    copy.append(name)
    return copy

original = ["Mateo", "Emma"]
class1 = add_student(original, "Yichen")

print("class 1:", class1)

class2 = add_student(original, "Amir")


print("class 2:", class2)

"""
The code is supposed to print out the list of students plus the new student but the issue is that it is using
the same original list so it just prints the same list twice 
"""
