s=input('stringa ')
while not(s.isalpha()) or (not(s.islower())):
    print(s[0]+s[len(s)-1])
    s=input('stringa ')
print(s[0]+s[len(s)-1])
