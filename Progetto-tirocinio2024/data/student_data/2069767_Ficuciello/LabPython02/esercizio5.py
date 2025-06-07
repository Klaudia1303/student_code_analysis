y=int(input('Inserire un anno:' ))
if y%4==0 and y%100!=0:
      print('anno bisestile')
elif y%400==0:
      print('anno bisestile')
else:
    print('anno non bisestile')
