pairs = [("--.", "G"), (".-..", "L"), ("---", "O"), (".--", "W")]

target = "G"
hits = list(filter(lambda p: p[1] == target, pairs))
print("hits =", hits)
print("len =", len(hits))
print("first pair =", hits[0] if hits else None)
print("the code =", hits[0][0] if hits else "?")
      
