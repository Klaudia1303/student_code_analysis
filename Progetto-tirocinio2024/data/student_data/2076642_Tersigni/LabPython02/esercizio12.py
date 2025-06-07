x=input("F o C?")
t=int(input("temperatura"))
if (x=="C" and t>=100) or (x=="F" and t>=132/1.8) :
      print("gassosa")
elif (x=="C" and t<0) or (x=="F" and t<=32/1.8) :
    print("solida")
elif (x=="C" and 0<t<100) or (x=="F" and 32/1.8<t<132/1.8) :
    print("liquida")
