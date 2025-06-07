hh=int(input('Inserire il numero di ore: '))
mm=int(input('Inserire il numero di minuti: '))
ss=int(input('Inserire il numero di secondi: '))
orem=int(hh*60)
tot_secondi=(orem*60)+(mm*60)+ss
print('L\'equivalente in numero di secondi corrisponde a '+str(tot_secondi)+' secondi')
