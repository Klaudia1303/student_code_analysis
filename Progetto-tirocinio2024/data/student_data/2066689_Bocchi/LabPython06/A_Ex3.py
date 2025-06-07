ris1=0
ris2=0
for i in range(0,8):
    print('-----------')
    for y in range(0,8):
        ris= i*y
        if ris >= 8:
            ris1 = ris//8
            ris2 = ris%8
        print(i, 'x', y, '=', str(ris1)+str(ris2))
''' un numero in base ottale quando arriva ad 8 diventa 10
perche il 10 è composto da
--> 8 diviso la base ottale quindi 8 quindi il risultato di 8//8 è 1
+ il resto che troviamo facendo 8%8 quindi resto 0

QUINDI 8 in base ottale è composto da 1 e 0 --> 10
'''
