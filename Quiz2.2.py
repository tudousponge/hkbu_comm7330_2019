def Convert(_floorNumHK):
    temp = True
    try: 
        _floorNumHK = int(_floorNumHK)
        _floorNumMCN = _floorNumHK + 1
        print('\nHK Floor Number : {0} \n'.format(_floorNumHK))
        print('Mainland China Floor Number : {0} \n'.format(_floorNumMCN))
        temp = False
    except:
        if _floorNumHK == 'G' or _floorNumHK == 'g':
            print('\nHK Floor Number : G \n')    # As a modification to the form of the input
            print('Mainland China Floor Number : 1 \n')
            temp = False
        else:
            print('\nYou did not input the floor correctly!\nPlese try again')
    return temp 


condition = True
while condition == True:
    floor = input('Input HK Floor Number : ')
    condition = Convert(_floorNumHK = floor)