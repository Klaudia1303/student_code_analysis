c = input ("inserire un carattere: ")
somma = 0
while somma <= 2:
    s = input ("inserire una stringa: ")
    somma = 0
    i = 0
    while i < len (s):
        if (s[i] == c):
            somma = somma + 1
        i = i + 1
print (somma)
