changingParam = ['Taste','Odor','Fat','Turbidity']
changingValues = [['Bad','Good'],['Bad','Good'],['Low','High'],['Low','High']]

def generateProfile(data):
    milk_profile = []
    for x in data:
        if x in changingParam:
            X_index = changingParam.index(x)
            newStrings = x + '  :  ' + changingValues[X_index][int(data[x])]
        else:
            newStrings = x + '  :  ' + data[x]
        milk_profile.append(newStrings)
    print(milk_profile)
    return milk_profile