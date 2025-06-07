def A_Ex4(filename,anno):
    file=open(filename, encoding="UTF-8")
    annofile=file.readline()
    annofile=annofile.strip().split(',')
    ogg=''
    mass=0
    if str(anno) in annofile:
        pos=annofile.index(str(anno))
        riga=file.readline()
        while len(riga)>0:
            riga=riga.strip().split(',')
            if int(riga[pos])>mass:
                mass=int(riga[pos])
                ogg=str(riga[0])
            elif int(riga[pos])==mass:
                for i in range (min(len(ogg),len(riga[0]))):
                    if ord (riga[0][i])>ord(ogg[i]):
                        mass=int(riga[pos])
                        ogg=str(riga[0])
            riga=file.readline()
    file.close()
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
