hh = input('Insert hours: ')
hh = int(hh)
mm = input('Insert minutes: ')
mm = int(mm)
ss = input('Insert seconds: ')
ss = int(ss)
hs = hh*3600
ms = mm*60
time = hs+ms+ss
print(time)
