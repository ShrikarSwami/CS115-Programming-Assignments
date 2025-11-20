# === CS 115 Lab 10 ===
# Fill in your name and the Stevens Honor Code pledge on the following lines.
# Failure to fill this in will result in deducted marks.
#
# Name: Shrikar Swami
#
# Pledge:I pledge my honor that I have abided by the Stevens Honor System.
#
# === CS 115 Lab 10 ===
class Employee:
    def __init__(self, name, eid):
        self.name = name #This defines an employees name
        self.id = eid #This defines their ID
        self.manager = None #This defines there manager status which is subject to change!
        self.salary = 0
        

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

    def give_raise(self, new_salary):
        #This raises the empoyee's salary to new_salary if it is higher then the current salary then it decrease
        #Also if the employee earns more than their manager then then the manger must also be given a raise to the same salary
        if new_salary <= self.salary: #do nothing if this would not increase salary
            return
        self.salary = new_salary #Give this employee the raise

        if self.manager is not None and self.salary > self.manager.salary: #The manager cannot be earning less than their employees
            self.manager.give_raise(self.salary)

class Mentor(Employee):
    #A mentor is an employee who can mentor another employee or their mentee
    def __init__(self, name, eid):
        super().__init__(name, eid)
        self.mentee = None

    def assign_mentee(self, employee):
        #Assign a mentee to this mentor
        if employee is not None and employee.manager is not self: #Cannot assign someone under you as a mentee
            self.mentee = employee

    def recommend(self): #This function recommends a mentee for a prompotions
        if self.mentee is None:
            return
        mentee_depth = self.mentee.org_depth()
        mentor_depth = self.org_depth()

        if mentee_depth >= mentor_depth + 2:
            self.mentee.promote()

#The best class
class Embezzler(Employee):
    #Embezzler is a special employee who can double any riase they get 
    def give_raise(self, new_salary):
        if new_salary <= self.salary:
            return
        normal_increase = new_salary - self.salary
        actual_increase = 2 * normal_increase

        new_salary_for_embezzler = self.salary + actual_increase

        self.salary = new_salary_for_embezzler

        if self.manager is not None and self.salary > self.manager.salary:
            self.manager.give_raise(self.salary)

class Manager(Employee):
    def __init__(self, name, eid):
        super().__init__(name, eid)
        self.reports = []

    def assign(self, employee):
        old_manager = employee.manager #assign this manager as the employee manager but if they had an old one remove it
        super().assign(employee)
        if employee not in self.reports:
            self.reports.append(employee)
        if isinstance(old_manager, Manager) and employee in old_manager.reports:
            old_manager.reports.remove(employee)

    #Reassign all of this manager's reports to another employee.
    def reassign(self, new_manager):
        if not self.reports:
            return

        emp = self.reports.pop()

        if isinstance(new_manager, Manager):
            new_manager.assign(emp)
        else:
            emp.manager = new_manager

        self.reassign(new_manager)
        
    
        


