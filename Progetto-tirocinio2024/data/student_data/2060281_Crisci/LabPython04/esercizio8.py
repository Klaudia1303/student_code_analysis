s1=str(input("Inserire una stringa: "))
s2=str(input("Inserire una stringa: "))
x=s1[len(s1)-1:]
y=s2[0:1]
while not(x==y):
    s1=s2
    s2=str(input("Inserire una stringa: "))
    x=s1[len(s1)-1:]
    y=s2[0:1]
print(s1, s2)
