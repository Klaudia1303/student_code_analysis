s=input('inserisci stringa: ')
i=0
x=0
while i<len(s):
    y= s.count(s[i])
    if y >= x:
        x=y
        lettera= s[i]
    i+=1
print(lettera)
