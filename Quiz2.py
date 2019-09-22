def converter(inputValue):
    try:
        inputValue = int(inputValue)
        #return inputValue
    except:
        inputValue = -1
        #print('Error.')
        #sys.exit()
    #UnicodeTranslateError
    return inputValue
    '''else :
        return inputValue'''
         
    #return inputValue


def eleConverter(HKFloor):
    if HKFloor=='G':
        MCFloor = 1
    else:  
        HKFloor = converter(HKFloor) 
        while HKFloor == -1:
            print('Input again.')
            HKFloor = input('Input HK Floor Number:')   
            HKFloor = converter(HKFloor)
        MCFloor = HKFloor + 1
    return MCFloor


HKLevel = input('Input HK Floor Number:')
HKLevel = str.upper(HKLevel)

MCLevel = eleConverter(HKLevel)

print('HK Floor Number: ', HKLevel)
print('Mainland China Floor Number:', MCLevel)