n=input('inserire un intero (* premere per terminare): ')
contatore=0
while n!='*':
      if n!='*':
            s=n
            s=int(s)
            if s%2==0:
                  contatore+=1
                  n=input('inserire un intero (* premere per terminare): ')
            else:
                  n=input('inserire un intero (* premere per terminare): ')
print(contatore)

      
            
