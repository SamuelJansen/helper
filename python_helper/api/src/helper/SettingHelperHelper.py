from python_helper.api.src.service import StringHelper, LogHelper, ObjectHelper, EnvironmentHelper, SettingHelper
from python_helper.api.src.domain import Constant as c
from python_helper.api.src.helper import StringHelperHelper

OPEN_SETTING_INJECTION = '${'
CLOSE_SETTING_INJECTION = '}'

SETTING_KEY = 'SETTING_KEY'
SETTING_VALUE = 'SETTING_VALUE'
NODE_KEY = 'NODE_KEY'

def getFilteredSetting(settingKey, settingValue, nodeKey, settingTree) :
    # if not settingValue is None and isinstance(settingValue, str) :
    if StringHelper.isNotBlank(settingValue) :
        settingEvaluationList = settingValue.split(c.COLON)
        if len(settingEvaluationList) > 1 :
            defaultSettingValue = c.COLON.join(settingValue.split(c.COLON)[1:]).strip()
        else :
            defaultSettingValue = c.NONE
        if isSettingInjection(defaultSettingValue) :
            return getSettingInjectionValue(
                settingKey,
                defaultSettingValue,
                nodeKey,
                settingTree
            )
        return None if c.NONE == defaultSettingValue else StringHelper.filterString(defaultSettingValue)
    return settingValue

def lineAproved(settingLine) :
    approved = True
    if c.NEW_LINE == settingLine  :
        approved = False
    if c.HASH_TAG in settingLine :
        filteredSettingLine = StringHelper.filterString(settingLine)
        if filteredSettingLine is None or c.NOTHING == filteredSettingLine or c.NEW_LINE == filteredSettingLine :
            approved = False
    return approved

def updateSettingTreeAndReturnNodeKey(settingKey, settingValue, nodeKey, settingTree) :
    updateSettingTree(settingKey, settingValue, nodeKey, settingTree)
    if not isSettingValue(settingValue) :
        if c.NOTHING == nodeKey :
            nodeKey += f'{settingKey}'
        else :
            nodeKey += f'{c.DOT}{settingKey}'
    return nodeKey

def accessTree(nodeKey,tree) :
    strippedNodeKey = nodeKey.strip()
    if nodeKey is None or nodeKey == c.NOTHING :
        returnTree = None
        try :
            returnTree = StringHelper.filterString(tree)
        except Exception as exception :
            LogHelper.log(accessTree, f'Failed to get filtered string from {tree} tree', exception=exception)
            returnTree = tree
        return returnTree
    elif isinstance(nodeKey,str) :
        nodeKeyList = nodeKey.split(c.DOT)
        if len(nodeKeyList) == 1 :
             nextNodeKey = c.NOTHING
        else :
            nextNodeKey = c.DOT.join(nodeKeyList[1:])
        return accessTree(nextNodeKey,tree[nodeKeyList[0]])

def safelyAccessTree(nodeKey, settingTree) :
    setting = None
    try :
        setting = accessTree(nodeKey,settingTree)
    except Exception as exception :
        LogHelper.log(safelyAccessTree, f'Not possible to safely access "{nodeKey}" node key while looping through setting tree. Returning "{setting}" by default', exception=exception)
    return setting

def updateSettingTree(settingKey, settingValue, nodeKey, settingTree) :
    accessTree(nodeKey,settingTree)[settingKey] = getSettingValueOrNewNode(settingValue)

def getDepth(settingLine) :
    depthNotFount = True
    depth = 0
    while not settingLine[depth] == c.NEW_LINE and depthNotFount:
        if settingLine[depth] == c.SPACE :
            depth += 1
        else :
            depthNotFount = False
    return depth

def settingTreeInnerLoop(
        settingLine,
        nodeKey,
        settingTree,
        longStringCapturing,
        quoteType,
        longStringList,
        settingInjectionList
    ) :
    settingKey, settingValue = getAttributeKeyValue(settingLine)

    if containsSettingInjection(settingValue) :
        try :
            settingKey, settingValue, nodeKey, longStringCapturing, quoteType, longStringList = handleSettingInjection(
                settingKey,
                settingValue,
                nodeKey,
                settingTree,
                longStringCapturing,
                quoteType,
                longStringList,
                settingInjectionList
            )
        except Exception as exception :
            LogHelper.log(settingTreeInnerLoop, f'Not possible to handle association of "{nodeKey}{c.DOT}{settingKey}" setting key to "{settingValue}" value', exception=exception)
            settingInjectionList.append({
                SETTING_KEY : settingKey,
                SETTING_VALUE : settingValue,
                NODE_KEY : nodeKey
            })
        return settingKey, settingValue, nodeKey, longStringCapturing, quoteType, longStringList
    else :
        return handleLongStringOrSetting(
            settingKey,
            settingValue,
            nodeKey,
            settingTree,
            longStringCapturing,
            quoteType,
            longStringList,
            settingInjectionList
        )

def handleSettingInjection(
        settingKey,
        settingValue,
        nodeKey,
        settingTree,
        longStringCapturing,
        quoteType,
        longStringList,
        settingInjectionList
    ) :
    if isSettingInjection(settingValue) :
        settingValue = getSettingInjectionValue(settingKey, settingValue, nodeKey, settingTree)
    if containsSettingInjection(settingValue) :
        settingInjectionList.append({
            SETTING_KEY : settingKey,
            SETTING_VALUE : settingValue,
            NODE_KEY : nodeKey
        })
        return settingKey, settingValue, nodeKey, longStringCapturing, quoteType, longStringList
    return handleLongStringOrSetting(
        settingKey,
        settingValue,
        nodeKey,
        settingTree,
        longStringCapturing,
        quoteType,
        longStringList,
        settingInjectionList
    )

def handleSettingInjectionList(settingInjectionList, settingTree, fallbackSetingTree=None) :
    if ObjectHelper.isNotEmptyCollection(settingInjectionList) and ObjectHelper.isNotNone(settingTree) :
        try :
            done = False
            strugled = False
            while not done and not strugled :
                strugled = True
                isSettingInjectionCount = 0
                containsSettingInjectionCount = 0
                settingInjectionListCopy = [] + settingInjectionList
                for settingInjection in settingInjectionListCopy :
                    try :
                        if isSettingInjection(settingInjection[SETTING_VALUE]) :
                            settingInjection[SETTING_VALUE] = safelyGetSettingInjectionValue(
                                settingInjection[SETTING_KEY],
                                settingInjection[SETTING_VALUE],
                                settingInjection[NODE_KEY],
                                settingTree,
                                fallbackSetingTree=fallbackSetingTree
                            )
                            settingInjectionList.remove(settingInjection)
                            settingInjectionArgs = list(settingInjection.values()) + [settingTree]
                            updateSettingTree(*settingInjectionArgs)
                            isSettingInjectionCount += 1
                            strugled = False
                        elif containsSettingInjection(settingInjection[SETTING_VALUE]) :
                            settingInjectionListFromSettingValue = getSettingInjectionListFromSettingValue(settingInjection[SETTING_VALUE])
                            newSettingInjection = settingInjection[SETTING_VALUE]
                            for settingValue in settingInjectionListFromSettingValue :
                                newSettingValue = safelyGetSettingInjectionValue(
                                    settingInjection[SETTING_KEY],
                                    settingValue,
                                    settingInjection[NODE_KEY],
                                    settingTree,
                                    fallbackSetingTree=fallbackSetingTree
                                )
                                newSettingInjection = newSettingInjection.replace(settingValue,str(newSettingValue))
                            settingInjection[SETTING_VALUE] = newSettingInjection
                            if not containsSettingInjection(settingInjection[SETTING_VALUE]) :
                                settingInjectionList.remove(settingInjection)
                            settingInjectionArgs = list(settingInjection.values()) + [settingTree]
                            updateSettingTree(*settingInjectionArgs)
                            containsSettingInjectionCount += 1
                            strugled = False
                    except Exception as exception :
                        LogHelper.log(handleSettingInjectionList, f'Ignored exception while handling setting injection list', exception=exception)
                if strugled :
                    LogHelper.setting(handleSettingInjectionList, f'Parsed settings: {StringHelper.prettyPython(settingTree)}')
                    notParsedSettingInjectionDictionary = {}
                    for setting in settingInjectionList :
                        notParsedSettingInjectionDictionary[f'{setting[NODE_KEY]}{c.DOT}{setting[SETTING_KEY]}'] = setting[SETTING_VALUE]
                    if 0 == isSettingInjectionCount :
                        raise Exception(f'Circular reference detected in following setting injections: {StringHelper.prettyPython(notParsedSettingInjectionDictionary)}')
                    else :
                        raise Exception(f'Not possible to parse the following setting injections: {StringHelper.prettyPython(notParsedSettingInjectionDictionary)}')
                elif 0 == len(settingInjectionList) :
                    done = True
        except Exception as exception :
            LogHelper.error(handleSettingInjectionList,'Not possible to load setting injections properly',exception)
            raise exception

def safelyGetSettingInjectionValue(settingKey, settingValue, nodeKey, settingTree, fallbackSetingTree=None) :
    exception = None
    newSettingValue = None
    try :
        newSettingValue = getSettingInjectionValue(settingKey, settingValue, nodeKey, settingTree)
    except Exception as e :
        exception = e
        LogHelper.log(safelyGetSettingInjectionValue, f'Not possible to load "{settingKey}" setting key from setting tree. Now trying to load it from default setting tree', exception=exception)
    if ObjectHelper.isNone(newSettingValue) and ObjectHelper.isNotNone(fallbackSetingTree) :
        return getSettingInjectionValue(settingKey, settingValue, nodeKey, fallbackSetingTree)
    if ObjectHelper.isNotNone(exception) :
        raise exception
    return newSettingValue

def handleLongStringOrSetting(
        settingKey,
        settingValue,
        nodeKey,
        settingTree,
        longStringCapturing,
        quoteType,
        longStringList,
        settingInjectionList
    ) :
    if StringHelper.isLongString(settingValue) :
        longStringCapturing = True
        splitedSettingValueAsString = settingValue.split(c.TRIPLE_SINGLE_QUOTE)
        if c.TRIPLE_SINGLE_QUOTE in settingValue and splitedSettingValueAsString and c.TRIPLE_DOUBLE_QUOTE not in splitedSettingValueAsString[0] :
            quoteType = c.TRIPLE_SINGLE_QUOTE
        else :
            quoteType = c.TRIPLE_DOUBLE_QUOTE
        longStringList = [settingValue + c.NEW_LINE]
    else :
        nodeKey = updateSettingTreeAndReturnNodeKey(settingKey, settingValue, nodeKey, settingTree)
    filteredSettingValue = getFilteredSetting(settingKey, settingValue, nodeKey, settingTree)
    return settingKey, filteredSettingValue, nodeKey, longStringCapturing, quoteType, longStringList

def getAttributeKeyValue(settingLine) :
    settingKey = getAttributeKey(settingLine)
    settingValue = getAttibuteValue(settingLine)
    return settingKey,settingValue

def getAttributeKey(settingLine) :
    possibleKey = StringHelper.filterString(settingLine)
    return possibleKey.split(c.COLON)[0].strip()

def getAttibuteValue(settingLine) :
    possibleValue = StringHelper.filterString(settingLine)
    return getValue(c.COLON.join(possibleValue.split(c.COLON)[1:]))

def isSettingKey(possibleSettingKey) :
    return possibleSettingKey and (
        not isSettingInjection(possibleSettingKey) and
        possibleSettingKey == possibleSettingKey.lower() and
        not c.COLON in possibleSettingKey
    )

def isSettingValue(settingValue) :
    return ObjectHelper.isNotEmpty(settingValue) or ObjectHelper.isCollection(settingValue)

def getSettingValueOrNewNode(settingValue) :
    return settingValue if isSettingValue(settingValue) else dict()

def getValue(value) :
    filteredValue = StringHelper.filterString(value)
    if isSettingValue(filteredValue) :
        if StringHelper.isNotBlank(filteredValue) :
            if c.OPEN_LIST == filteredValue[0] :
                return getList(filteredValue)
            elif c.OPEN_TUPLE == filteredValue[0] :
                return getTuple(filteredValue)
            elif c.OPEN_DICTIONARY == filteredValue[0] :
                return getDictionary(filteredValue)
            elif c.OPEN_SET == filteredValue[0] :
                return getSet(filteredValue)
        parsedValue = None
        try :
            parsedValue = int(filteredValue)
        except :
            try :
                parsedValue = float(filteredValue)
            except :
                try :
                    parsedValue = filteredValue
                    if not filteredValue is None :
                        if filteredValue == c.TRUE :
                            parsedValue = True
                        elif filteredValue == c.FALSE :
                            parsedValue = False
                except:
                    parsedValue = filteredValue
        return parsedValue
    return filteredValue

def getList(value) :
    roughtValueList = value[1:-1].split(c.COMA)
    valueList = list()
    for value in roughtValueList :
        gottenValue = getValue(value)
        if ObjectHelper.isNotEmpty(gottenValue) :
            valueList.append(gottenValue)
    return valueList

def getTuple(value) :
    return tuple(getList(value))

def getSet(value) :
    roughtValueList = value[1:-1].split(c.COMA)
    valueSet = set()
    for value in roughtValueList :
        gottenValue = getValue(value)
        if ObjectHelper.isNotNone(gottenValue) :
            valueSet.add(gottenValue)
    return valueSet

def getDictionary(value) :
    splitedValue = value[1:-1].split(c.COLON)
    keyList = []
    for index in range(len(splitedValue) -1) :
        keyList.append(splitedValue[index].split(c.COMA)[-1].strip())
    valueList = []
    valueListSize = len(splitedValue) -1
    for index in range(valueListSize) :
        if index == valueListSize -1 :
            correctValue = splitedValue[index+1].strip()
        else :
            correctValue = c.COMA.join(splitedValue[index+1].split(c.COMA)[:-1]).strip()
        valueList.append(getValue(correctValue))
    resultantDictionary = dict()
    for index in range(len(keyList)) :
        resultantDictionary[keyList[index]] = valueList[index]
    return resultantDictionary

def getSettingInjectionListFromSettingValue(settingValue) :
    if StringHelper.isNotBlank(settingValue) :
        splitedSettingValue = settingValue.split(OPEN_SETTING_INJECTION)
        settingValueList = []
        completeSettingValue = c.NOTHING
        for segment in splitedSettingValue if settingValue.startswith(OPEN_SETTING_INJECTION) else splitedSettingValue[1:] :
            if not segment is None and not segment.count(c.OPEN_DICTIONARY) is None and not segment.count(c.OPEN_DICTIONARY) == segment.count(c.CLOSE_DICTIONARY) and 0 < segment.count(c.OPEN_DICTIONARY) :
                completeSettingValue += segment
            else :
                splitedSegment = segment.split(CLOSE_SETTING_INJECTION)
                completeSettingValue += splitedSegment[0]
                settingValueList.append(f'{OPEN_SETTING_INJECTION}{completeSettingValue}{CLOSE_SETTING_INJECTION}')
                completeSettingValue = c.NOTHING
        return settingValueList
    return []

def containsValidSettingInjection(settingValue) :
    if StringHelper.isNotBlank(settingValue) and 0 < settingValue.count(OPEN_SETTING_INJECTION) and settingValue.count(c.OPEN_DICTIONARY) == settingValue.count(c.CLOSE_DICTIONARY) :
        splitedSettingValue = settingValue.split(OPEN_SETTING_INJECTION)
        settingValueList = []
        completeSettingValue = c.NOTHING
        for segment in splitedSettingValue if settingValue.startswith(OPEN_SETTING_INJECTION) else splitedSettingValue[1:] :
            if not segment is None and not segment.count(c.OPEN_DICTIONARY) is None and not segment.count(c.OPEN_DICTIONARY) == segment.count(c.CLOSE_DICTIONARY) and 0 < segment.count(c.OPEN_DICTIONARY) :
                completeSettingValue += segment
            else :
                splitedSegment = segment.split(CLOSE_SETTING_INJECTION)
                completeSettingValue += splitedSegment[0]
                settingValueList.append(f'{OPEN_SETTING_INJECTION}{completeSettingValue}{CLOSE_SETTING_INJECTION}')
                completeSettingValue = c.NOTHING
        return len(splitedSettingValue) == len(settingValueList) if settingValue.startswith(OPEN_SETTING_INJECTION) else len(splitedSettingValue) == len(settingValueList) + 1
    return False

def isSettingInjection(settingValue) :
    return ObjectHelper.isNotNone(settingValue) and (
        isinstance(settingValue, str) and
        settingValue.startswith(OPEN_SETTING_INJECTION) and
        settingValue.endswith(CLOSE_SETTING_INJECTION) and
        containsSettingInjection(settingValue)
    )

def containsSettingInjection(settingValue) :
    return False if not containsValidSettingInjection(settingValue) else 0 < len(getSettingInjectionListFromSettingValue(settingValue))

def getSettingInjectionValue(settingKey, settingValue, nodeKey, settingTree) :
    unwrapedSettingInjectionValue = getUnwrappedSettingInjection(settingValue)
    if isSettingKey(unwrapedSettingInjectionValue) :
        selfReferenceSettingValue = safelyAccessTree(unwrapedSettingInjectionValue, settingTree)
        if ObjectHelper.isNone(selfReferenceSettingValue) :
            raise Exception(f'Not possible to associate "{nodeKey}{c.DOT}{settingKey}" key to "{unwrapedSettingInjectionValue}" value. "{unwrapedSettingInjectionValue}" value is probably not defined')
        return selfReferenceSettingValue
    environmentKey = unwrapedSettingInjectionValue.split(c.COLON)[0]
    environmentValue = EnvironmentHelper.getEnvironmentValue(environmentKey)
    if environmentValue :
        return environmentValue
    else :
        return getFilteredSetting(settingKey, unwrapedSettingInjectionValue, nodeKey, settingTree)

def getUnwrappedSettingInjection(settingValue) :
    if isSettingInjection(settingValue) :
        return settingValue[2:-1]
    return settingValue

def keepSearching(keywordQuery,tree,querySet,history=None):
    if ObjectHelper.isDictionary(tree) :
        for key in tree.keys() :
            if StringHelper.isNotBlank(history) :
                newHistory = f'{history}.{key}'
            else :
                newHistory = f'{key}'
            if StringHelper.isNotBlank(keywordQuery) and key == keywordQuery :
                querySet[newHistory] = tree[key]
            keepSearching(keywordQuery,tree[key],querySet,history=newHistory)

def printNodeTree(
        tree,
        depth,
        settingKeyColor=c.NOTHING,
        settingValueColor=c.NOTHING,
        colonColor=c.NOTHING,
        resetColor=c.NOTHING
    ):
    depthSpace = c.NOTHING
    for nodeDeep in range(depth) :
        depthSpace += f'{c.TAB_UNITS * c.SPACE}'
    depth += 1
    for node in list(tree) :
        if ObjectHelper.isDictionary(tree[node]) :
            print(f'{depthSpace}{settingKeyColor}{node}{colonColor}{c.SPACE}{c.COLON}')
            printNodeTree(
                tree[node],
                depth,
                settingKeyColor=settingKeyColor,
                settingValueColor=settingValueColor,
                colonColor=colonColor,
                resetColor=resetColor
            )
        else :
            print(f'{depthSpace}{settingKeyColor}{node}{colonColor}{c.SPACE}{c.COLON_SPACE}{settingValueColor}{tree[node]}{resetColor}')

def getSettingKeyPrompColor(withColors) :
    return c.DARK_MAGENTA if withColors else c.NOTHING

def getSettingValuePrompColor(withColors) :
    return c.DARK_YELLOW if withColors else c.NOTHING

def getSettingColonPrompColor(withColors) :
    return c.BRIGHT_BLACK if withColors else c.NOTHING

def getSettingResetPrompColor(withColors) :
    return c.DEFAULT_COLOR if withColors else c.NOTHING
