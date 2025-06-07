def Ex8(file):
    file = open(file,encoding='UTF-8')
    l = []
    for elem in file:
        l.append(elem.strip())
    lista = []
    for elem in l :
        ris = ''
        mesi = 'ABCDEHLMPRST'
        if re.match(r'[A-Z]{3} *[A-Z]{3} *\d{2}[A-Z]\d{2} *[A-Z]\d{3}[A-Z]', elem) != None:
            if re.match(r'\w{3} *\w{3} *\d{2}[A-EHLMPRST]\d{2} *\w\d{3}\w', elem ) != None :
                temp = re.findall(r'\d{2}\w\d{2}',elem)
                data = temp[0]
                gg = int(data[3]+data[4])
                mese = data[2]
                anno = int(data[0]+data[1])
                if mese in 'ACELMRT' :
                    if gg<= 31 :
                        if gg <= 9 :
                            ris = ris + '0'+ str(gg)+'/'
                            pos = mesi.find(mese) +1
                            if pos <= 9:
                                ris = ris+'0'+str(pos)+'/'
                            else:
                                ris = ris + str(pos)+'/'
                            if anno <=20 :
                                ris = ris + '20' + str(anno)
                                lista.append(ris)
                            else:
                                ris = ris + '19' + str(anno)
                                lista.append(ris)  
                        else :
                            ris = ris + str(gg)+'/'
                            pos = mesi.find(mese) +1
                            if pos <= 9:
                                ris = ris+'0'+str(pos)+'/'
                            else:
                                ris = ris + str(pos)+'/'
                            if anno <=20 :
                                ris = ris + '20' + str(anno)
                                lista.append(ris)
                            else:
                                ris = ris + '19' + str(anno)
                                lista.append(ris)              
                    elif 40<gg<=71:
                        gg = gg - 40 
                        if gg <= 9 :
                            ris = ris + '0'+ str(gg)+'/'
                            pos = mesi.find(mese) +1
                            if pos <= 9:
                                ris = ris+'0'+str(pos)+'/'
                            else:
                                ris = ris + str(pos)+'/'
                            if anno <=20 :
                                ris = ris + '20' + str(anno)
                                lista.append(ris)
                            else:
                                ris = ris + '19' + str(anno)
                                lista.append(ris)  
                        else :
                            ris = ris + str(gg)+'/'
                            pos = mesi.find(mese) +1
                            if pos <= 9:
                                ris = ris+'0'+str(pos)+'/'
                            else:
                                ris = ris + str(pos)+'/'
                            if anno <=20 :
                                ris = ris + '20' + str(anno)
                                lista.append(ris)
                            else:
                                ris = ris + '19' + str(anno)
                                lista.append(ris)              
                    else:
                        lista.append('Giorno errato')
                elif mese in 'DHPS' :
                    if gg<=30 :
                        if gg <= 9 :
                            ris = ris + '0'+ str(gg)+'/'
                            pos = mesi.find(mese) +1
                            if pos <= 9:
                                ris = ris+'0'+str(pos)+'/'
                            else:
                                ris = ris + str(pos)+'/'
                            if anno <=20 :
                                ris = ris + '20' + str(anno)
                                lista.append(ris)
                            else:
                                ris = ris + '19' + str(anno)
                                lista.append(ris)  
                        else :
                            ris = ris + str(gg)+'/'
                            pos = mesi.find(mese) +1
                            if pos <= 9:
                                ris = ris+'0'+str(pos)+'/'
                            else:
                                ris = ris + str(pos)+'/'
                            if anno <=20 :
                                ris = ris + '20' + str(anno)
                                lista.append(ris)
                            else:
                                ris = ris + '19' + str(anno)
                                lista.append(ris)              
                    elif 40<gg<=70:
                        gg = gg -40
                        if gg <= 9 :
                            ris = ris + '0'+ str(gg)+'/'
                            pos = mesi.find(mese) +1
                            if pos <= 9:
                                ris = ris+'0'+str(pos)+'/'
                            else:
                                ris = ris + str(pos)+'/'
                            if anno <=20 :
                                ris = ris + '20' + str(anno)
                                lista.append(ris)
                            else:
                                ris = ris + '19' + str(anno)
                                lista.append(ris)  
                        else :
                            ris = ris + str(gg)+'/'
                            pos = mesi.find(mese) +1
                            if pos <= 9:
                                ris = ris+'0'+str(pos)+'/'
                            else:
                                ris = ris + str(pos)+'/'
                            if anno <=20 :
                                ris = ris + '20' + str(anno)
                                lista.append(ris)
                            else:
                                ris = ris + '19' + str(anno)
                                lista.append(ris)                                    
                    else :
                        lista.append('Giorno errato')
                elif mese == 'B':
                    if gg<= 28 :
                        if gg <= 9 :
                            ris = ris + '0'+ str(gg)+'/'
                            pos = mesi.find(mese) +1
                            if pos <= 9:
                                ris = ris+'0'+str(pos)+'/'
                            else:
                                ris = ris + str(pos)+'/'
                            if anno <=20 :
                                ris = ris + '20' + str(anno)
                                lista.append(ris)
                            else:
                                ris = ris + '19' + str(anno)
                                lista.append(ris)  
                        else :
                            ris = ris + str(gg)+'/'
                            pos = mesi.find(mese) +1
                            if pos <= 9:
                                ris = ris+'0'+str(pos)+'/'
                            else:
                                ris = ris + str(pos)+'/'
                            if anno <=20 :
                                ris = ris + '20' + str(anno)
                                lista.append(ris)
                            else:
                                ris = ris + '19' + str(anno)
                                lista.append(ris)              
                    elif 40<gg<=68:
                        gg = gg - 40
                        if gg <= 9 :
                            ris = ris + '0'+ str(gg)+'/'
                            pos = mesi.find(mese) +1
                            if pos <= 9:
                                ris = ris+'0'+str(pos)+'/'
                            else:
                                ris = ris + str(pos)+'/'
                            if anno <=20 :
                                ris = ris + '20' + str(anno)
                                lista.append(ris)
                            else:
                                ris = ris + '19' + str(anno)
                                lista.append(ris)  
                        else :
                            ris = ris + str(gg)+'/'
                            pos = mesi.find(mese) +1
                            if pos <= 9:
                                ris = ris+'0'+str(pos)+'/'
                            else:
                                ris = ris + str(pos)+'/'
                            if anno <=20 :
                                ris = ris + '20' + str(anno)
                                lista.append(ris)
                            else:
                                ris = ris + '19' + str(anno)
                                lista.append(ris)                        
                    else:
                        lista.append('Giorno errato')
            else:
                lista.append('Mese errato')
        else:
            lista.append('Codice errato')        
    return(lista)

    
###############################################################################

if __name__ == '__main__':
    from tester import tester_fun
    import re

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex8, ["codici1.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato'])
    counter_test_positivi += tester_fun(Ex8, ["codici2.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato'])
    counter_test_positivi += tester_fun(Ex8, ["codici3.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato', '01/11/1921'])
    counter_test_positivi += tester_fun(Ex8, ["codici4.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato', '01/11/1921', '01/11/1931'])
    counter_test_positivi += tester_fun(Ex8, ["codici5.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato', '01/11/1921', '01/11/1931', 'Codice errato', 'Giorno errato'])

    print('La funzione',Ex8.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
