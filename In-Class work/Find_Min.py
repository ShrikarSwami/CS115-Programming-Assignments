def my_sum (lst):
    if len(lst)==0:
        return 0
    return lst [0] + my_sum (lst[1:])

def find_min(lst):
    small=0
    if len(lst)==1:
        return lst[0]
    if len(lst)!=1:
        first = lst[0]
        rest = lst[1:]
        if first<lst[1]:
            return first
        else:
            return find_min(lst[1:])


print(find_min([6,4,66,7]))
