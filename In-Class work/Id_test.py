L1 = [1,2,3]
L2 = L1
L2[2] = 5
print(L1[2])

if id(L2)==id(L1):
    print("same id")
