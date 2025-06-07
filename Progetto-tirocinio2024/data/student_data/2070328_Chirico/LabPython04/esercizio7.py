#trova il carattere che compare più volte nella stringa

s = input("parola = ")
i = 0
n = 0

while i < len(s):
    if s.count(s[i]) >= n:
        n = i
    i = i+1

print(s[n])
