s1 = input("inserisci una stringa: ")
s2 = input("inserisci un'altra stringa: ")
n = int(input("inserisci un numero intero: "))

s = ""

for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            if i <= (j + n) and i >= (j - n):
                if s.count(s1[i]) == 0:
                    s = s + s1[i]
print(s)
                
