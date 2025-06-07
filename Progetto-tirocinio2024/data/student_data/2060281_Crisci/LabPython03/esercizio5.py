s=str(input("Inserire una sequenza di stringhe: "))
while(s.isalpha()==False or s.islower()==False):
    print(s[0:1]+s[len(s)-1:])
    s=str(input())
print(s[0:1]+s[len(s)-1:])
