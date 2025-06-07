from pickle import FALSE


s = input("inserisci la stringa: ")
n = int(input("inserisci l'intero: "))
i = 0
temp = False
while i+n<len(s):
    if s[i] == s[i+n]:
        temp = True
    i+=1
print(temp)