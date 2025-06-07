x=int(input('inserisci una temperatura: '))
y=input('specifica l\'unità di misura per Celsius usa \"C\" per Fahrenheit \"F\"')
Y=y=='F'
c=float(x-32)/1.8
if Y and(c<=0):
    print('solida')
if Y and(c>=100):
    print('gassosa')
if Y and(1<c<99):
    print('liquida')
X=y=='C'
if X and (x<=0):
    print('solida')
if X and (x>=100):
    print('gassosa')
if X and(1<x<99):
    print('liquida')



   
