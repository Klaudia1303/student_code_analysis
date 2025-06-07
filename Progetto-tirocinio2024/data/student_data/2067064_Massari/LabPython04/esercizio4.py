n=int(input('inserire un numero intero (* per terminare): '))
addizione=0
while n!=0:
      if n%3==0:
            addizione=addizione+n
            n=int(input('inserire un numero intero (* per terminare): '))
      else:
            n=int(input('inserire un numero intero (* per terminare): '))
      if n==0:
            print(addizione)
            
      
