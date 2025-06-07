s = input ("inserire la stringa s: ")
i = 0
verifica = 0
carattereM = 0
while i < len(s):
    conta = 0
    j = 0
    while j < len(s):
        if ( s[i] == s[j]):
            conta = conta + 1
        j = j + 1
        if ( verifica <= conta):
            verifica = conta
            carattereM = s[i]
    i = i + 1
print ("il carattere ripetuto più volte nella stringa s è:", carattereM)
