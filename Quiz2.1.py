def liftConverter(HKLevel):
    HKLevel = str.upper(HKLevel) #to convert HKLevel to uppercase, which avoids to judge 'g' or 'G'
    loopControl = False #loopControl is a variable to control whether to input again

    if HKLevel == 'G':
        MCLevel = 1
        print('HK floor number:', HKLevel)
        print('Mainland China floor number:', MCLevel)
        loopControl = True

    else:
        try:
            HKLevel = int(HKLevel)
        except:
            print('Your input is not availble.')            
        else:
            MCLevel = HKLevel + 1
            print('HK Floor number:', HKLevel)
            print('Mainland China floor number:', MCLevel) 
            loopControl = True

    return loopControl


HKFloor = input('Input HK floor number:')
while liftConverter(HKFloor) == False: #if the return value is False, then input again.
    HKFloor = input('Input HK floor number again:')

