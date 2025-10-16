# === CS 115 Lab 5 ===
# Fill in your name and the Stevens Honor Code pledge on the following lines.
# Failure to fill this in will result in deducted marks.
#
# Name: Shrikar Swami
#
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
#
# === CS 115 Lab 5 ===

def coin_change(coins, total): #This is the function defining line
    """
    if len(coins) == 0 or total<=0: #This is checking if there are any coins or if the total is 0
        return 0
    """
    if total == 0:
        return 0

    if not coins or total<0:
        return 9999
    

    lose_it = (coin_change(coins[1:], total))
               
    """
    if coins[0]>total:
        return lose_it
    """
    use_it=1+coin_change(coins,total-coins[0])
    
        
    return min(use_it, lose_it) #Do this until you get however naby coins needed
    
