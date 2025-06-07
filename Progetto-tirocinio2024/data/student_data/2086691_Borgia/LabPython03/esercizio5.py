print("Inserire una serie di stringhe: " )
s=input()
while s.islower()==False:
    print(s[0]+s[-1])
    s=input()
print(s[0]+s[-1])

