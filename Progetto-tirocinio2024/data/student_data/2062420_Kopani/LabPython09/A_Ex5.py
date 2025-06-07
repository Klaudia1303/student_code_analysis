def A_Ex5(filename,oggetto):
	f=open(filename,encoding='UTF-8')
	l=f.readlines()
	pos=0
	mas=0
	for i in range(len(l)):
		s=l[i].strip().split(',')
		if s[0]==oggetto:
			for j in range(2,len(s)):
				if int(s[j])>=int(s[j-1]) and int(s[j])-int(s[j-1])>=mas:
					mas=int(s[j])-int(s[j-1])
					pos=j
		else:
			continue
		d=l[0].strip().split(',')
		f.close()
		if pos==0:
			return int(d[1])
		else:
			return int(d[pos])


###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex5, ['Vendite1.csv','Giubbotto'] , 2012)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite1.csv','Zaino'] , 2010)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite2.csv','Maglione'] , 2012)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite2.csv','Zaino'] , 2013)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite3.csv','Giubbotto'] , 2013)

    print('La funzione',A_Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
