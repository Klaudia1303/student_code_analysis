def A_Ex4(filename,anno):
     f=open(filename,encoding='UTF-8')
     l=f.readlines()
     mas=0
     for i in range(len(l)):
     	s=l[i].strip().split(',')
     	if i==0:
     		k=s.index(str(anno))
     	else:
     		if int(s[k])>mas:
     			mas=int(s[k])
     			ris=s[0]
     		elif int(s[k])==mas and s[0]>ris:
     			ris=s[0]
     return ris
     
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
