s = input ("inserire una stringa contenente almeno due caratteri, s: ")
n = int (input ("inserire un numero intero positivo n: "))
for i in range (0, len(s),1):
    if (i+n) <= len(s)-1:
        if s[i] == s[i+n]:
            verifica = True
            break
        else:
            verifica = False
print (verifica)
