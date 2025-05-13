def selectFromDict(options, name="option"):
    index = 0
    indexValidList = []
    print('Select a ' + name + ':')
    for optionName in options:
        index = index + 1
        indexValidList.extend([options[optionName]])
        print(str(index) + ') ' + optionName)
    inputValid = False
    while not inputValid:
        inputRaw = input(name + ': ')
        inputNo = int(inputRaw) - 1
        if inputNo > -1 and inputNo < len(indexValidList):
            selected = indexValidList[inputNo]
            break
        else:
            print('Please select a valid ' + name + ' number')
    return selected

# ---------------

def selectFromList(options, name="option"):
    index = 0
    print('Select a ' + name + ':')
    for optionName in options:
        index = index + 1
        print(str(index) + ') ' + optionName)
    inputValid = False
    while not inputValid:
        inputRaw = input(name + ': ')
        inputNo = int(inputRaw) - 1
        if inputNo > -1 and inputNo < len(options):
            selected = options[inputNo]
            break
        else:
            print('Please select a valid ' + name + ' number')
    return selected