def A_Ex3(fileName):
	f=open(fileName,encoding='UTF-8')
	l=f.readlines()
	ris=set()
	for i in range(1,len(l)):
		a=0
		s=l[i]
		ls=s.strip().split(',')
		if int(ls[1])>=29:
			a+=1
		for j in range(1,len(l)):
			if j==i:
				continue
			s2=l[j]
			ls2=s2.strip().split(',')
			if int(ls2[1])>=29 and ls2[2]==ls[2]:
				a+=2
		if a>=2:
			ris.add(ls[2])
	f.close()
	return ris	

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun
    
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex3, ["esami1.csv"], {'Fisica'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami2.csv"], set())
    counter_test_positivi += tester_fun(A_Ex3, ["esami3.csv"], {'Ricerca Operativa','Analisi'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami4.csv"], {'Basi di Dati'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami5.csv"], set())

    print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)