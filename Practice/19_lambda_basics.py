pair_G = ("--.", "G")
pair_L = (".-..", "L")

def is_letter_G(pair):
    return pair[1] == "G"

is_letter_G_lambda = lambda p: p[1] == "G"

print(is_letter_G(pair_G), is_letter_G(pair_L))
print(is_letter_G_lambda(pair_G), is_letter_G_lambda(pair_L))
