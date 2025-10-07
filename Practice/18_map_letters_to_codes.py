pairs = [("--.", "G"), (".-..", "L"), ("---", "O"), (".--", "W")]
def letter_to_code(letter, pairs):
    hits = list(filter(lambda p: p[1] == letter, pairs))
    return hits[0][0] if hits else "?"

word = "Glow"
letters = list(word.upper())
codes = list(map(lambda ch: letter_to_code(ch, pairs), letters))
print(letters)
print(codes)
