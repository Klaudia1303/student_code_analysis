s1 = ''
while len(s1) == 0:
    s1 = input("inserisci s1: ")

s2 = ''
while len(s2) == 0:
    s2 = input("inserisci s2: ")

n = 0
while n <= 0:
    n = int(input("inserisci n: "))

out = ''
for i in range(len(s1)):
     for j in range(len(s2)):
        if s2[j] == s1[i] and j in range(i-n, i+n+1):
            out += s2[j]

print(out)