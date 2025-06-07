s=input('inserire una stringa: ')
n=int(input('inserire un intero positivo: '))
if s.isalpha() and n%2==0:
      for i in range (len(s)):
            for j in range(n):
                  print(s[i],end='')