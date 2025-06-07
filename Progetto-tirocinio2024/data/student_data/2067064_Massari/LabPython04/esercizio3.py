n=input('inserire un numero intero (* per terminare): ')
addizione=0
while n!='*':
      if n!='*':
            s=n
            s=int(s)
            if s<0:
                  addizione=addizione+s
                  n=input('inserire un numero intero (* per terminare): ')
            else:
                  n=input('inserire un numero intero (* per terminare): ')
      if n=='*':
            print(addizione)
                  
                  
