pairs = [("--.", "G"), (".-..", "L"), ("---", "O"), (".--", "W")]

def letter_to_code(letter, pairs):
    hits = list(filter(lambda p: p[1] == letter, pairs))
    return hits[0][0] if hits else None  # None means not found

print(letter_to_code("L", pairs))
print(letter_to_code("Z", pairs))
