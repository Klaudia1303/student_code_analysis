a=str(input('inserire una stinga '))
b=0
for i in range(len(a)):
    if a.rfind(a[i])-a.find(a[i])>b:
        b=a.rfind(a[i])-a.find(a[i])
print(b)
