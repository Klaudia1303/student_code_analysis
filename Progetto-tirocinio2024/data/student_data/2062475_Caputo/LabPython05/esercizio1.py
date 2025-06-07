print ("inserire due stringhe s1 ed s2 della stessa lunghezza")
s1 = input ("inserire la stringa s1: ")
s2 = input ("inserire la stringa s2: ")
for i in range (0,len(s1)):
    print (s1[i] + (s2[i]), end='')
