usrNumber=int(input('please type a prime number: '))
while usrNumber<=1:
    print('the number must be greater than 1.')
    usrNumber=int(input('please type a prime number: '))
for num in range(2, usrNumber + 1):
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
        
   
    
        
        
        


    
    
    
    
    
