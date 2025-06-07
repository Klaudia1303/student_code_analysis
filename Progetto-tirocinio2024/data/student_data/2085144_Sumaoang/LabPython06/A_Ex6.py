numeraleAlieno = "349776123345679876543234567876543234569055"
numeroTerrestre = 9510990939794952322311710154344301747012051743844839


def decimale(digit: str) -> int:

    if(digit.isdigit()):
        return int(digit)
    else:
        return 10 + ord(digit.lower()) - ord('a')

def to_decimal(digits : list, base : int) -> int:

   nDecimale = 0

   for i, c in enumerate(digits[::-1]):
        nDecimale += decimale(c) * base ** i

   return nDecimale


base = 1
condizione = False
while not condizione:
    if base ** (len(numeraleAlieno) + 1) > numeroTerrestre:
        if to_decimal(numeraleAlieno, base) == numeroTerrestre:
            condizione = True
    base += 1

print(base - 1)
