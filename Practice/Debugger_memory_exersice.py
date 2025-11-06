original = [ [1,2,3],[4,5,6],[7,8,9]]

method_1 = original
method_2 = original [:]
method_3 = list ( original )

def identit ( x ) :
    return id(x)

method_4 = id ( original )
method_5 = list ( map ( id , original ) )
method_6 = list ( map ( lambda row : row , original ) )
method_7 = list ( map ( lambda row : id ( row ) , original ) )
method_8 = list ( map ( lambda row : row [:] , original ) )

print("Orignal ID: " + str(identit(original)))
print("Orignal ID: " + str(identit(original[0])))
print()
print(4)
print(identit(method_4))
print(identit(method_4))

print(5)
print(identit(method_5))
print(identit(method_5[0]))

print(6)
print(identit(method_6))
print(identit(method_6[0]))

print(7)
print(identit(method_7))
print(identit(method_7[0]))




