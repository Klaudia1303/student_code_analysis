n1=int(input('inserisci un numero: '))
n2=int(input('inserisci un secondo numero: '))
var=0
molt=0

while var<abs(n1):
    molt=molt+n2
    var=var+1
if var>n1:
     var=var+1
     molt=-molt
print(molt)


