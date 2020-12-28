from python_helper.api.src.domain import Constant as c
from python_helper.api.src.service import ObjectHelper
from python_helper.api.src.helper import StringHelperHelper

def isBlank(thing) :
    return isinstance(thing, str) and c.NOTHING == thing

def isNotBlank(thing) :
    return isinstance(thing, str) and not c.NOTHING == thing

def filterJson(json, extraCharacterList=None) :
    charactereList = [c.NEW_LINE,c.BAR_N]
    if isinstance(extraCharacterList, list) :
        charactereList += extraCharacterList
    filteredJson = json
    for charactere in charactereList :
        filteredJson = removeCharactere(charactere,filteredJson)
    return filteredJson.replace(c.SYSTEM_TAB,c.TAB)

def removeCharactere(charactere,string) :
    filteredString = c.NOTHING.join(string.strip().split(charactere))
    return filteredString.replace(charactere,c.NOTHING)

def getFilteredString(string,globals) :
    return filterString(string)

def prettyPython(
        outterValue,
        quote=c.SINGLE_QUOTE,
        tabCount=0,
        nullValue=c.NONE,
        trueValue=c.TRUE,
        falseValue=c.FALSE,
        withColors=False
    ) :
    '''It always sort sets'''
    strReturn = c.NOTHING
    if ObjectHelper.isCollection(outterValue) :
        if isinstance(outterValue, list) :
            collectionType = c.TYPE_LIST
        elif isinstance(outterValue, set) :
            collectionType = c.TYPE_SET
        elif isinstance(outterValue, tuple):
            collectionType = c.TYPE_TUPLE
        elif isinstance(outterValue, dict) :
            collectionType = c.TYPE_DICT
        else :
            raise Exception(f'Unexpected collection in python_helper.StringHelper.prettyPython(): {outterValue}')
        return StringHelperHelper.prettyCollection(
            StringHelperHelper.getValueCollection(outterValue),
            collectionType,
            quote,
            prettyPython,
            tabCount,
            nullValue,
            trueValue,
            falseValue,
            withColors=withColors
        )
    else :
        return StringHelperHelper.prettyInstance(
            outterValue,
            quote,
            prettyPython,
            tabCount,
            nullValue,
            trueValue,
            falseValue,
            withColors=withColors
        )

def prettyJson(
        outterValue,
        quote=c.DOUBLE_QUOTE,
        tabCount=0,
        nullValue=c.NULL_VALUE,
        trueValue=c.TRUE_VALUE,
        falseValue=c.FALSE_VALUE,
        withColors=False
    ) :
    '''It always sort sets'''
    if ObjectHelper.isCollection(outterValue) :
        if isinstance(outterValue, list) or isinstance(outterValue, set) or isinstance(outterValue, tuple) :
            collectionType = c.TYPE_LIST
        elif isinstance(outterValue, dict) :
            collectionType = c.TYPE_DICT
        else :
            raise Exception(f'Unexpected collection in python_helper.StringHelper.prettyJson(): {outterValue}')
        return StringHelperHelper.prettyCollection(
            StringHelperHelper.getValueCollection(outterValue),
            collectionType,
            quote,
            prettyJson,
            tabCount,
            nullValue,
            trueValue,
            falseValue,
            withColors=withColors
        )
    else :
        return StringHelperHelper.prettyInstance(
            outterValue,
            quote,
            prettyJson,
            tabCount,
            nullValue,
            trueValue,
            falseValue,
            withColors=withColors
        )

def filterString(string) :
    if string is None or not isinstance(string, str) :
        return string
    strippedString = string.strip()
    if c.NOTHING == strippedString :
        return strippedString
    if strippedString[-1] == c.NEW_LINE :
        strippedString = strippedString[:-1]
    surroundedBySingleQuote = strippedString.startswith(c.SINGLE_QUOTE) and strippedString.endswith(c.SINGLE_QUOTE) and not (c.SINGLE_QUOTE*2 == strippedString or c.TRIPLE_SINGLE_QUOTE == strippedString)
    surroundedByDoubleQuote = strippedString.startswith(c.DOUBLE_QUOTE) and strippedString.endswith(c.DOUBLE_QUOTE) and not (c.DOUBLE_QUOTE*2 == strippedString or c.TRIPLE_DOUBLE_QUOTE == strippedString)
    if c.HASH_TAG in strippedString and not (surroundedBySingleQuote or surroundedByDoubleQuote) :
        strippedString = filterString(c.HASH_TAG.join(strippedString.split(c.HASH_TAG)[:-1]))
    if strippedString and (
            (
                strippedString.startswith(c.TRIPLE_SINGLE_QUOTE) and
                strippedString.endswith(c.TRIPLE_SINGLE_QUOTE) and
                not c.TRIPLE_SINGLE_QUOTE == strippedString
            ) or
            (
                strippedString.startswith(c.TRIPLE_DOUBLE_QUOTE) and
                strippedString.endswith(c.TRIPLE_DOUBLE_QUOTE) and
                not c.TRIPLE_DOUBLE_QUOTE == strippedString
            )
        ) :
        return filterString(strippedString[3:-3])
    else :
        return strippedString if not (surroundedBySingleQuote or surroundedByDoubleQuote) else filterString(strippedString[1:-1])

def isLongString(thing) :
    if not thing is None and isinstance(thing, str) :
        return (
            (
                thing.startswith(c.TRIPLE_SINGLE_QUOTE) or
                thing.endswith(c.TRIPLE_SINGLE_QUOTE)
            ) and StringHelperHelper.isNotOneLineLongString(c.TRIPLE_SINGLE_QUOTE, thing) or (
                thing.startswith(c.TRIPLE_DOUBLE_QUOTE) or
                thing.endswith(c.TRIPLE_DOUBLE_QUOTE)
            ) and StringHelperHelper.isNotOneLineLongString(c.TRIPLE_DOUBLE_QUOTE, thing)
        )
    else :
        return False

def getStringWithoutColors(thing) :
    if isNotBlank(thing) :
        for color in c.IMPLEMENTED_PROMP_COLORS :
            if color in thing :
                thing = thing.replace(color,c.NOTHING)
    return thing if isinstance(thing, str) else str(string)
