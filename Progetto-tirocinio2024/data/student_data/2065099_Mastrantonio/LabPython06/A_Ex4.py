viagg1 = viagg2 =0
for giorno in range (1,1001):
    viagg1 = viagg1 +20
    viagg2 = viagg2 + giorno
    print(viagg1,viagg2)
    if viagg2 >= viagg1 :
        break
print (giorno)
