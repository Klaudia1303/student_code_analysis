giorno=0
primo=0
secondo=0
for km in range (1,1001):
    while primo>=secondo:
            giorno+=1
            #print('Giorno:',giorno)
            primo+=20
            #print('Il primo è al km:',primo)
            secondo=secondo+km
            #print('Il secondo è al km:',secondo,'\n')
            break
print(giorno-1)
