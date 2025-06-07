c=input('inserire una sequenza di stringhe: ')
while (c.isalpha()==False or c.islower()==False):
    print(c[0:1]+c[len(c)-1:])
    c=str(input())
print(c[0:1]+c[len(c)-1:])
