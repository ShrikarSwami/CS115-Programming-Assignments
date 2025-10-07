pairs = [("--.","G"),(".-..","L"),("---","O"),(".--","W")]

target = "G"
hits = list(filter(lambda p: p[1] == target, pairs))
print (hits)
print(hits[0][0])
