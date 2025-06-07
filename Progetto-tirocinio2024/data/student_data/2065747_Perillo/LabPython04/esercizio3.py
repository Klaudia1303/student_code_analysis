n=input("Enter a number:")
m=0
while n!="*":
    if int(n)<0:
        m=m+int(n)
    n=input("Enter a number:")
print(m)
