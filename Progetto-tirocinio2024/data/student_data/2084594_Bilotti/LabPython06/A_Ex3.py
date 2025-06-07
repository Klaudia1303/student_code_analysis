var1 = input('Stampare la tabbella Pitagorica in base ottale? \n[Y/N]: ')
var1 = str(var1)

if var1 == 'Y':
    print('01  02  03  04  05  06  07  10  11  12')
    print('02  04  06  10  12  14  16  20  22  24')
    print('03  06  11  14  17  22  25  30  33  36')
    print('04  10  14  20  24  30  34  40  44  50')
    print('05  12  17  24  31  36  43  50  55  62')
    print('06  14  22  30  36  44  52  60  66  74')
    print('07  16  25  34  43  52  61  70  77  106')
    print('10  20  30  40  50  60  70  100 110 120')
    print('11  22  33  44  55  66  77  110 121 132')
    print('12  24  36  50  62  74  106 120 132 144')
elif var1 == 'N':
    print('...')
