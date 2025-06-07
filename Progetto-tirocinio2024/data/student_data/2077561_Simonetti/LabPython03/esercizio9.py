usrNumber=int(input('please type a number to check if it is prime or not: '))
if usrNumber>1:
    for i in range(2,usrNumber):
        if usrNumber%i==0:
           print(usrNumber,'is not prime.')
           break
    else:
            print(usrNumber,'is prime number.')
    
