def alpha(starter: str, final: str, step: int):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    counter = alphabet.index(starter)
    if starter not in alphabet or final not in alphabet:
        return "starter or final letter is not correct "
    while counter < alphabet.index(final.lower()):
        yield alphabet[counter]
        counter += step


print("abcdefghijklmnopqrstuvwxyz".index("a"))
for item in alpha('a', 'ff', 2):
    print(item)

