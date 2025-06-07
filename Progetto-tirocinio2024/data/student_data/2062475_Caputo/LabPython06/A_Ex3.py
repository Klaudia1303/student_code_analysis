for i in range (1,8):
    for j in range (1,8):
        prodotto = i * j
        baseotto = ""
        while (prodotto != 0):
            baseotto = str(prodotto%8) + baseotto
            prodotto = prodotto // 8
        if len(baseotto)== 1:
            baseotto = "0" + baseotto
        print(baseotto, end = "  ")
    print("\n")
            
