anno = int(input('inserisci anno: '))

var1 = anno%4
var2 = anno%100
var3 = anno%400

if (var1 == 0 and var2 != 0) or var3 == 0:
    print('anno bisestile')
else:
    print('anno non bisestile')
