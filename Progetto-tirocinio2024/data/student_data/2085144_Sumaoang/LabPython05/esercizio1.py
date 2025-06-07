s1 = input("Inserire una stringa:")
s2 = input("Inserire una stringa con la stessa lunghezza:")
i = 0

while i < len(s1):
    while i < len(s2):
        print(s1[i] + s2[i], end = "" )
        i += 1
