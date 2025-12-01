##################################
# Short loop practice problems   #
# For in-class review            #
# Implement at least 2           #
##################################


def first_even_index(nums):
    """
    return the index of the first even number in nums
    if none exist, return -1
    """
    # hint: use a for-loop with enumerate
    for i, num in enumerate(nums):
        if num % 2 == 0:
            return i
    return -1


def pop_three_letter_words(words):
    """
    pop elements from words until empty and count how many
    have exactly 3 characters
    original list should end empty
    """
    # hint: while-loop + words.pop()
    count = 0
    while words:
        word = words.pop()
        if len(word) == 3:
            count += 1
    return count


def sum_of_squares(n):
    """
    return the sum of squares from 1 to n inclusive
    must build the list of squares using range()
    """
    # hint: list comprehension or building a list then summing
    squares = [i**2 for i in range(1, n + 1)]
    return sum(squares)


def collatz_steps(n):
    """
    return how many Collatz steps it takes for n to reach 1
    A step counts as a Collatz step if n is modified
    collatz rule: if n is even, n = n // 2; if n is odd, n = 3*n + 1
    if n is already 1, return 0
    """
    # hint: standard while-loop structure
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps


def my_map(func, nums):
    """
    return a new list containing func(x) for each x in nums
    """
    # hint: for-loop accumulating into a list
    result = []
    for x in nums:
        result.append(func(x))
    return result


def my_filter(pred, nums):
    """
    return a new list of elements x in nums for which pred(x) is true
    """
    # hint: for-loop with an if-check
    result = []
    for x in nums:
        if pred(x):
            result.append(x)
    return result

def max_value_in_each_row(grid):
    """
    part of later in-class activity

    return a new list of the element 
    with the max value in each row
    for example, for this grid

    grid = [[5, 0, 2],
            [1, 2, 0],
            [10, 2, 0],
    this function would return
    [5, 2, 10]
    """
    # hint: nested loops 
    result = []
    for row in grid:
        if not row:
            continue
        max_val = row[0]
        for val in row:
            if val > max_val:
                max_val = val
        result.append(max_val)
    return result


if __name__ == '__main__':
    pass
    # sample informal tests. Uncomment to run

    print(first_even_index([1, 3, 5, 8, 10]))
    # expected: 3

    words = ["cat", "hi", "dog", "sun", "ok"]
    print(pop_three_letter_words(words))
    # expected: 3   # "cat", "dog", "sun"

    print(sum_of_squares(5))
    # expected: 55

    print(collatz_steps(6))
    # expected: 8

    print(my_map(lambda x: x * 2, [1, 2, 3]))
    # expected: [2, 4, 6]

    print(my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))
    # expected: [2, 4]

    # print(
    grid = [[5, 0, 2],
            [1, 2, 0],
            [10, 2, 0]]
    print(max_value_in_each_row(grid))
    # expected: [5, 2, 10]

