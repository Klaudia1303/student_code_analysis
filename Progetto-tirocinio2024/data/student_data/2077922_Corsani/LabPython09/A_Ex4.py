#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.4

def A_Ex4(filename,anno):
    f = open(filename,encoding="UTF-8")
    r = f.readline()
    fv = r.strip().split(",")
    pos = 0
    for j in range(len(fv)):
        if fv[j].isdecimal() and int(fv[j])==anno:
            pos = j
    max = 0
    ogg = ''
    for i in f:
        iv = i.strip().split(",")
        if int(iv[pos])>max or (int(iv[pos])==max and iv[0]>ogg):
            max = int(iv[pos])
            ogg = iv[0]
    f.close()
    return ogg

###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex4, ['Vendite1.csv',2012] , 'Giubbotto')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite2.csv',2012] , 'Maglione')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite2.csv',2013] , 'Zaino')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite3.csv',2011] , 'Giubbotto')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite3.csv',2010] , 'Cellulare')
    
    print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
