s1 = ""
s2 = "s"

while len(s1) != len(s2):
    s1 = input("1) inserisci due stringhe di lunghezza uguale: ")
    s2 = input("2) inserisci due stringhe di lunghezza uguale: ")

for i in range(len(s1)):
    print(s1[i], s2[i], sep='', end='')
