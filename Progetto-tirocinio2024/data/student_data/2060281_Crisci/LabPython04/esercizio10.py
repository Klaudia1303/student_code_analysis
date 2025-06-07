s1=str(input("Inserire una stringa: "))
s2=str(input("Inserire una stringa: "))
s3=str(input("Inserire una stringa: "))
x=len(s1)
y=len(s2)
z=len(s3)
while not (x+y==z):
    s1=s2
    s2=s3
    s3=str(input("Inserire una stringa: "))
    x=len(s1)
    y=len(s2)
    z=len(s3)
print(s1, s2)
