import Constant as c

def filterJson(json) :
    charactereList = [c.NEW_LINE,c.SPACE,c.BAR_N]
    filteredJson = json
    for charactere in charactereList :
        filteredJson = removeCharactere(charactere,filteredJson)
    return filteredJson

def removeCharactere(charactere,string) :
    filteredString = c.NOTHING.join(string.strip().split(charactere))
    return filteredString.replace(charactere,c.NOTHING)

def getFilteredString(string,globals) :
    charactereToFilter = c.NOTHING
    if c.TRIPLE_SINGLE_QUOTE in string or c.TRIPLE_DOUBLE_QUOTE in string :
        if string.strip()[0:3] == c.TRIPLE_SINGLE_QUOTE :
            charactereToFilter = c.TRIPLE_SINGLE_QUOTE
        else :
            charactereToFilter = c.TRIPLE_DOUBLE_QUOTE
    elif string.strip().startswith(c.SINGLE_QUOTE) or string.strip().startswith(c.DOUBLE_QUOTE) :
        if string.strip()[0] == c.SINGLE_QUOTE :
            charactereToFilter = c.SINGLE_QUOTE
        else :
            charactereToFilter = c.DOUBLE_QUOTE
    return string.replace(charactereToFilter,c.NOTHING)
