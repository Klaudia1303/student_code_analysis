etaCane = float(input('Inserire l\' eta\' del cane:'))

if etaCane <= 2 and etaCane!=0:
    print(etaCane * 10.5)
elif etaCane > 2:
    print(2.0 * 10.5 + (etaCane - 2.0) * 4.0)
