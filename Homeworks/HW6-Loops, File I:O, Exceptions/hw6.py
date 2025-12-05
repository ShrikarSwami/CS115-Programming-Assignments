'''
#==============================================================================#
#                           CS 115 Homework 6 Report                           #
#==============================================================================#
+------------------------------------------------------------------------------+
| Fill in your name and the Stevens Honor Code pledge on the following lines.  |
| Failure to fill this in will result in deducted marks.                       |
+------------------------------------------------------------------------------+
Name: Shrikar Swami

Pledge: I pledge my honor that I have abided by the Stevens Honor System.
##==============================================================================#
'''
def parse_file(filename):
    # Check if file exists
    try: # Try to open the file
        f = open(filename, 'r') # Open file for reading
    except FileNotFoundError: # If file not found, raise error
        raise ValueError(f"File does not exist: {filename}") # Raise ValueError if file not found
    
    lines = f.readlines() # Read all lines from file
    f.close() # Close the file
    
    # Check if file is empty
    if len(lines) == 0: # If no lines in file
        raise ValueError("File is empty") # Raise ValueError if file is empty
    
    # Parse first line for dimensions
    first_line = lines[0].strip().split() # Split first line into parts
    if len(first_line) != 2: # Check if there are exactly two parts
        raise ValueError("First line does not contain exactly two integers") # Raise ValueError if not exactly two parts
    
    try: # Try to convert dimensions to integers
        m = int(first_line[0]) # Number of columns
        n = int(first_line[1]) # Number of rows 
    except ValueError: # If conversion fails
        raise ValueError("Dimension values are not integers") # Raise ValueError if dimensions are not integers
    
    # Check that dimensions are positive 
    if m <= 0 or n <= 0: # If either dimension is not positive
        raise ValueError("Dimension numbers must be positive integers") # Raise ValueError if dimensions are not positive integers
    
    # Check that we have exactly n rows
    if len(lines) != n + 1: # Check if number of lines matches expected rows
        raise ValueError(f"Expected {n} rows, but got {len(lines) - 1}") # Raise ValueError if row count does not match
    
    # Parse the grid
    grid = [] # Initialize empty grid
    for i in range(1, n + 1): # Loop through each row
        row_str = lines[i].strip().split() # Split row into parts
        
        # Check that row has exactly m integers
        if len(row_str) != m: # Check if number of integers matches expected columns
            raise ValueError(f"Row {i} has {len(row_str)} integers, expected {m}") # Raise ValueError if column count does not match
        
        row = [] # Initialize empty row
        for val_str in row_str: # Loop through each value in the row
            try: # Try to convert value to integer 
                val = int(val_str) # Convert string to integer
            except ValueError: # If conversion fails
                raise ValueError(f"Row {i} contains non-integer value: {val_str}") # Raise ValueError if value is not an integer
            
            # Check that value is positive
            if val <= 0: # If value is not positive
                raise ValueError(f"Row {i} contains non-positive integer: {val}") # Raise ValueError if value is not positive
            
            row.append(val) # Append value to row
        
        grid.append(row) # Append row to grid
    
    return grid # Return the parsed grid


def distances_from(grid): # Compute distance table for grid
    # Handle empty grid case
    if not grid or not grid[0]: # If grid is empty or first row is empty
        return grid # Return empty grid as is
    
    num_rows = len(grid) # Get how many rows we have
    num_cols = len(grid[0]) # Get how many columns we have
    
    # Create distance table with same dimensions as grid, filled with zeros
    dists = [[0] * num_cols for _ in range(num_rows)] # Initialize distance table
    
    # Initialize the starting position
    dists[0][0] = grid[0][0] # The cost to reach (0,0) is just the value at that cell
    
    # Fill first row going left to right
    for x in range(1, num_cols): # Loop through each column in the first row
        dists[0][x] = dists[0][x - 1] + grid[0][x] # Add previous distance to current cell cost
    
    # Fill first column going top to bottom
    for y in range(1, num_rows): # Loop through each row in the first column
        dists[y][0] = dists[y - 1][0] + grid[y][0] # Add distance above to current cell cost
    
    # Fill the rest of the table using dynamic programming
    for y in range(1, num_rows): # Loop through each row
        for x in range(1, num_cols): # Loop through each column
            # The best path to this cell is the minimum of coming from above or left
            dists[y][x] = grid[y][x] + min(dists[y - 1][x], dists[y][x - 1]) # Add current cost to the better path
    
    return dists # Return the completed distance table


def shortest_path(dists, point): # Find shortest path from target point back to (0,0)
    x, y = point # Unpack the target coordinates
    path = [] # Initialize empty path list
    
    # Trace back from target to (0, 0)
    while True: # Keep going until we reach the origin
        path.append((x, y)) # Add current position to the path
        
        # If we're at origin, we're done
        if x == 0 and y == 0: # Check if we reached (0,0)
            break # Exit the loop, we're finished
        
        # Determine which direction to go
        if x == 0: # If we're in the first column
            # First column: can only go up
            y -= 1 # Move up (decrease y)
        elif y == 0: # If we're in the first row
            # First row: can only go left
            x -= 1 # Move left (decrease x)
        else: # Otherwise we can move up or left
            # Compare above and left, choose the smaller distance
            # If equal, prefer going up (y direction)
            if dists[y - 1][x] <= dists[y][x - 1]: # If distance above is smaller or equal
                y -= 1 # Move up
            else: # If distance to the left is smaller
                x -= 1 # Move left
    
    return path # Return the path from target back to origin

