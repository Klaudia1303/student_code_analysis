x=int(input('Inserisci un numero intero: '))
y=int(input('Inserisci un numero intero: '))

#se non metto x e y posso mettere una condizione per cui si entra
#dentro while, ad esempio x=5 e y=6

while x<0 or x>10 or y<0 or y>10:
    #nella condizione di while inserisco i parametri che permettono di
    #controllare se x e y sono compresi uguali nell'intervallo
    #quindi quando x<0 or x>10 or y<0 or y>10 esce da while
    
    x=int(input('Inserisci un numero intero: '))
    y=int(input('Inserisci un numero intero: '))

i=0
while 0<=i<=10:
    if i!=x and i!=y:
        print (i)
    i+=1
    
