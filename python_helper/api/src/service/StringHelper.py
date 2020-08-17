from python_helper.api.src.domain import Constant as c

NULL_VALUE = 'null'

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


def newLine(strReturn, charactere):
    if charactere == strReturn[-1] :
        return f'{c.NEW_LINE}'
    else :
        return f'{c.COMA}{c.NEW_LINE}'

def stringfyThisDictionary(outterValue, tabCount=0, nullValue=NULL_VALUE) :
    strReturn = c.NOTHING
    if isinstance(outterValue, list) :
        if len(outterValue) == 0 :
            strReturn += f'{c.OPEN_LIST}{c.CLOSE_LIST}'
        else :
            strReturn += c.OPEN_LIST
            tabCount += 1
            for value in outterValue :
                strReturn += newLine(strReturn, c.OPEN_LIST)
                strReturn += f'{tabCount * c.TAB}{stringfyThisDictionary(value, tabCount=tabCount)}'
            strReturn += c.NEW_LINE
            tabCount -= 1
            strReturn += f'{tabCount * c.TAB}{c.CLOSE_LIST}'
    elif isinstance(outterValue, dict) :
        if len(outterValue) == 0 :
            strReturn += f'{c.OPEN_DICTIONARY}{c.CLOSE_DICTIONARY}'
        else :
            strReturn += c.OPEN_DICTIONARY
            tabCount += 1
            for key, value in outterValue.items() :
                strReturn += newLine(strReturn, c.OPEN_DICTIONARY)
                strReturn += f'{tabCount * c.TAB}"{key}": {stringfyThisDictionary(value, tabCount=tabCount)}'
            strReturn += c.NEW_LINE
            tabCount -= 1
            strReturn += f'{tabCount * c.TAB}{c.CLOSE_DICTIONARY}'
    elif isinstance(outterValue, int) or isinstance(outterValue, float) :
        strReturn += str(outterValue)
    elif outterValue is None :
        strReturn += nullValue
    else :
        strReturn += f'"{str(outterValue)}"'
    return strReturn
