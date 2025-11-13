# === CS 115 Lab 9 ===
# Fill in your name and the Stevens Honor Code pledge on the following lines.
# Failure to fill this in will result in deducted marks.
#
# Name: Shrikar Swami
#
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
#
# === CS 115 Lab 9 ===
class Employee:
    def __init__(self, name, eid):
        self.name = name #This defines an employees name
        self.id = eid #This defines their ID
        self.manager = None #This defines there manager status which is subject to change!
        

    def assign(self, report):
        report.manager = self #This assigns someone the manager status

    def __eq__(self, other):
        if not isinstance(other, Employee): #This is a base case that checks to make sure the object is an employee
            return NotImplemented #If not it throws an error
        return self.id == other.id and self.name == other.name #This checks to make sure the employee is the same person

    def __str__(self):
        base = f"{self.id}: {self.name}" #This is a print format for people
        if self.manager is not None: #If the person has a manager then 
            base += f" (Managed by {self.manager.id}: {self.manager.name})" #It should mention that 
        return base #Return that text

    def promote(self):
        if self.manager is not None: #this checks if the person is a manager
            self.manager = self.manager.manager #if the person if promote them

    def org_depth(self):
        if self.manager is None: #this checks if the person has a manager and if not they are the peak
            return 1
        return 1 + self.manager.org_depth() #this just keeps doing this until it find out if they have a manager 
    

