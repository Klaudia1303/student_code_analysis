print('Inserire un orario ')
ore=int(input('ore: '))
minuti=int(input('minuti: '))
secondi=int(input('secondi: '))
minutitot=(ore*60)+minuti+(secondi/60)
seconditot=minutitot*60
print(seconditot)
