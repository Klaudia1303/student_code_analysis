anno=input('inserisci un anno: ')
anno=int(anno)
if (anno%4==0 and anno%100!=0):
    print('questo anno è bisestile')
else:
    print('questo anno non è bisestile')
