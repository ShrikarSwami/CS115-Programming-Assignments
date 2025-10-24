from math import inf
# === CS 115 Homework 3 ===
# Fill in your name and the Stevens Honor Code pledge on the following lines.
# Failure to fill this in will result in deducted marks.
#
# Name: Shrikar Swami
#
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
#
# === CS 115 Homework 3 ===
def empty(m, n):
    if m==0: #This is a base case that basically will just return an empty list if nothing exists
        return []
    return [[0] * n] + empty(m-1, n) #This is where you create a list based off the number of rows, and the n number of columns using list multiplication

def copy(grid):
    if grid==[]: #This again is a base case that basically returns an empty list if there is nothing 
        return []
    if type(grid)==list: #This checks if the grid is a list and then it recursively does a deep copy
        return [copy(grid[0])] + copy(grid[1:]) #The reason there is a copy for both the first and second object is because if there wasn't it would have both list pointing to the same thing where as this simply replicates it
    else:
        return grid #this also just returns it if the grid isn't a list (another base case)

def increase_row(grid, y, cost):
    if y < 0 or y >= len(grid): #This is a base case for if y is a negative number or if the value is greater than the value of the list
        return
    def add_row(row, i): #I was trying to do it without a helper function but I really could not figure out how because this will allow me to increase each item by whaever the value needed it
        if i == len(row):
            return
        row[i] = row[i] + cost #essentially this should just add the value by the cost (in my test cases i used 10)
        add_row(row, i+1) #Then it should cal upon this to do the same for each item
    add_row(grid[y], 0) #and this is where the function is actually called

def increase_col(grid, x, cost):
    #This one is similar to the first one the main difference isntead of going leftto right row by row I am going up and down by column which is also weirder cuz of the way that lists and handled by python
    def add_col(r): #basically what this function should help us do is add the cost to everycell in the column which again is weirder than doing row because of how python handles them
        if r == len(grid): #base case to make sure there are actually more than one columns
            return
        if 0<= x < len(grid[r]):
            grid[r][x] = grid[r][x] + cost 
        add_col(r+1)
    add_col(0)

def distance_from(grid, x, y):
    #this one to be honest was a struggle because of memoization but I did end up getting the hang of it
    memo = {}

    def solve(rx, cy): #Helper function that should allow for the cheapest path from location x y o location 0 0
        #Out of bounds should return either infinity or and error so it never wins a minimum
        if rx<0 or cy<0:
            return inf#This returns infinity
        if rx == 0 and cy ==0: #Another base case at the origin
            return grid[0][0]
        #This is where the code gets a little finicky because of memoziation
        key = (rx, cy) #I make a key for the current location so it remebers the anwser here
        if key in memo: #If I already been here I can avoid doing the same recursion again
            return memo[key] #I
        best = grid[rx][cy] + min(solve(rx-1, cy), solve(rx, cy-1)) #I want to do the cost of the current cell then look for the cheaperof the two option which is either above me or to the left of me
        memo[key] = best#I then store whateveer that happens to be 
        return best #and finally i return that total cost
    return solve(x,y) #I then start the whole process again until i finsih 
