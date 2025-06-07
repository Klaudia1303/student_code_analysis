def Ex8(file):
    fin=open(file,encoding="UTF-8")
    codici=fin.readlines()
    fin.close()
    pattern=r"([A-Z]{3}) ?([A-Z]{3}) ?([0-9][0-9][A-Z][0-9][0-9]) ?([A-Z][0-9][0-9][0-9][A-Z])"
    mesi={"A":"01","B":"02","C":"03","D":"04","E":"05","H":"06","L":"07","M":"08","P":"09","R":"10","S":"11","T":"12",}
    lista=[]
    for riga in codici:
        cf=re.search(pattern,riga)
        if cf:
            gruppo3=cf.group(3)
            anno=int(gruppo3[0:2])
            if anno<=20:
                anno=int("20"+str(anno))
            else:
                anno=int("19"+str(anno))

            if gruppo3[2] in "ACELMRT":
                giorno=int(gruppo3[3:5])
                if 1<=giorno<=31:
                    data=str(giorno)+"/"+mesi[gruppo3[2]]+"/"+str(anno)
                    lista.append(data)
                elif 41<=giorno<=71:
                    giorno=giorno-40
                    giorno=str(giorno)
                    if len(giorno) ==1:
                        giorno="0"+giorno
                    data=giorno+"/"+mesi[gruppo3[2]]+"/"+str(anno)
                    lista.append(data)
                else:
                    lista.append("Giorno errato")
            elif gruppo3[2] in "DHPS":
                giorno=int(gruppo3[3:5])
                if 1<=giorno<=30:
                    data=str(giorno)+"/"+mesi[gruppo3[2]]+"/"+str(anno)
                    lista.append(data)
                elif 41<=giorno<=70:
                    giorno=giorno-40
                    giorno=str(giorno)
                    if len(giorno) ==1:
                        giorno="0"+giorno
                    data=giorno+"/"+mesi[gruppo3[2]]+"/"+str(anno)
                    lista.append(data)
                else:
                    lista.append("Giorno errato")
                
            elif gruppo3[2]=="B":
                giorno=int(gruppo3[3:5])
                if 1<=giorno<=28:
                    data=str(giorno)+"/"+mesi[gruppo3[2]]+"/"+str(anno)
                    lista.append(data)
                elif 41<=giorno<=68:
                    giorno=giorno-40
                    giorno=str(giorno)
                    if len(giorno)==1:
                        giorno="0"+giorno
                    data=giorno+"/"+mesi[gruppo3[2]]+"/"+str(anno)
                    lista.append(data)
                else:
                    lista.append("Giorno errato")
            else:
                lista.append("Mese errato")
        else:
            lista.append("Codice errato")
    return lista    
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    
###############################################################################

if __name__ == '__main__':
    from tester import tester_fun
    import re

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex8, ["codici1.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato'])
    counter_test_positivi += tester_fun(Ex8, ["codici2.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato'  ])
    counter_test_positivi += tester_fun(Ex8, ["codici3.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato', '01/11/1921'])
    counter_test_positivi += tester_fun(Ex8, ["codici4.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato', '01/11/1921', '01/11/1931'])
    counter_test_positivi += tester_fun(Ex8, ["codici5.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato', '01/11/1921', '01/11/1931', 'Codice errato', 'Giorno errato'])

    print('La funzione',Ex8.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
