numero=int(input('Inserire un numero diverso da 1: '))

div=2
count=0

while div<=numero/2 and count==0:

     if numero%div==0:

        count+=1

        div+=1

     if count==0:

         print('Numero primo')

     else:

         print('Il numero non è primo')
    
    
    
    


    
       
