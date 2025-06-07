s1 = input ("inserire la stringa s1: ")
s2 = input ("inserire la stringa s2: ")
n = int ( input ("inserire il numero n: ") )
stringa = ""
for i in range (0, len(s1)):
    if ( i >= n and i+n <= len(s2)-1 ):
        for j in range (i-n,i+n+1):
            if ( s1[i] == s2[j]):
                stringa = stringa + s1[i]
    elif ( i >= n and i+n > len(s2)-1 ):
        for j in range (i-n, len(s2)):
            if ( s1[i] == s2[j]):
                stringa = stringa + s1[i]
    else:
        for j in range (0, i+n+1):
            if ( s1[i] == s2[j]):
                stringa = stringa + s1[j]
print (stringa)
