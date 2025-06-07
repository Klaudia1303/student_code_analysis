a=input('inserire una stringa ')
b=input('inserire una stringa ')
for i in range(len(a)):
              c=b.find(a[i])
              if c<0:
                  print(a[i],end='')
