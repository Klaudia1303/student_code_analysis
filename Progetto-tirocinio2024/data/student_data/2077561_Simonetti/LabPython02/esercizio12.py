temp=float(input('please type the temperature: '))
scale=str(input('please type \'C\' for Celsius and \'F\' for Farenheit: '))
correctScale=scale.upper()
editTemp=str(temp)
fullTemp=editTemp+'°'+correctScale
celsius='C'
farenheit='F'

if correctScale==celsius or correctScale==farenheit:
    if farenheit in fullTemp:
        celsiusTemp=(temp-32)/1.8
        if celsiusTemp>0 and celsiusTemp<100:
            print('liquida a',fullTemp)
        elif celsiusTemp<=0:
            print('solida a',fullTemp)
        else:
            print('gassosa a',fullTemp)
    else:
        if temp>0 and temp<100:
            print('liquda a',fullTemp)
        elif temp<=0:
            print('solida a',fullTemp)
        else:
            print('gassosa a',fullTemp)
else:
    print('invalid scale. Please attain to °C or °F.')
