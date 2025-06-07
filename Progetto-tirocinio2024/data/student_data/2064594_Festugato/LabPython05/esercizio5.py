s = input('inserisci almeno due caratteri: ')
n = int(input('inserisci un intero positivo: '))
uguali= 0



for i in range(len(s)-n):
    if s[i] == s[i+n]:
                print(s[i],s[i+n])
                uguali = 1
                print('True')
                break
if uguali == 0:
    print('False')
  
           


    
         
             



        
        
    
    
        
    
    
