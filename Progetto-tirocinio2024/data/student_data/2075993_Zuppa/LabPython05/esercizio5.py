s=input('inserire una stringa   ')
while len(s)<2:
    s=input('inserire una stringa di almeno 2 carateri   ')
n=int(input('inserire un intero   '))
c=False
for i in range(len(s)-n):
      if s[i]==s[i+2]:
          c=True
          print(c)
if not c:
    print(c)
