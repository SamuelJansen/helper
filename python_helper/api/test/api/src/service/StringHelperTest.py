from python_helper import StringHelper, SettingHelper, Constant, log, Test

# LOG_HELPER_SETTINGS = {
#     log.LOG : True,
#     log.SUCCESS : True,
#     log.SETTING : True,
#     log.DEBUG : True,
#     log.WARNING : True,
#     log.FAILURE : True,
#     log.WRAPPER : True,
#     log.ERROR : True,
#     log.TEST : False,
#     SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT
# }

LOG_HELPER_SETTINGS = {
    log.LOG : False,
    log.SUCCESS : False,
    log.SETTING : False,
    log.DEBUG : False,
    log.WARNING : False,
    log.FAILURE : False,
    log.WRAPPER : False,
    log.ERROR : False,
    log.TEST : False
}

DICTIONARY_INSTANCE = {
    11: 'yolo',
    10: 2.2,
    True: False,
    'key': 'value',
    'anotherKey': {
        'key': 'value'
    },
    'aThirdKey': [
        'a',
        'b',
        {
            'c': 'd'
        },
        [
            None,
            True,
            'True',
            3.3,
            (
                2,
                '2'
            )
        ],
        {
            'key': (
                'e',
                'f',
                {
                    'g': {
                        'h': [
                            'i',
                            'j'
                        ]
                    }
                }
            )
        },
        {
            'someKey': 'someValue',
            'someOtherKey': {
                'q',
                'r',
                1,
                2,
                3,
                's'
            }
        }
    ]
}

@Test(environmentVariables={**LOG_HELPER_SETTINGS})
def mustFilterSetting() :
    # Arrange
    expectedSingleQuoteSettingCase = 'b'
    singleQuoteSettingCase = f' " {expectedSingleQuoteSettingCase}   "   '

    expectedTripleQuoteSettingCase = 'b'
    tripleQuoteSettingCase = f''' """ {expectedTripleQuoteSettingCase}   """   '''


    expectedBothCasesSingleQuoteSettingCase = 'b'
    bothCasesSingleQuoteSettingCase = f' " {expectedBothCasesSingleQuoteSettingCase}   "   '
    bothCases = f''' """ {bothCasesSingleQuoteSettingCase}   """   '''

    someCommentsInBetween = 'b'
    someCommentsInBetweenSingle = f"  '  {someCommentsInBetween}  #  '  #   "
    someCommentsInBetweenTriple = f"""   '''   {someCommentsInBetweenSingle} #  '''     #   """

    onlyComment = Constant.HASH_TAG*4
    onlyCommentSurroundleByTriples = f'''"""{onlyComment}Something after comment token"""'''
    onlyCommentSetting = f'"{onlyCommentSurroundleByTriples}"'

    # Act
    filteredStringSingleQuoteSettingCase = StringHelper.filterString(singleQuoteSettingCase)
    filteredStringTripleQuoteSettingCase = StringHelper.filterString(tripleQuoteSettingCase)
    filteredStringBothCasesSingleQuoteSettingCase = StringHelper.filterString(bothCases)
    filteredStringSomeCommentsInBetween = StringHelper.filterString(someCommentsInBetweenTriple)
    filteredStringOnlyComment = StringHelper.filterString(onlyCommentSetting)

    # Assert
    assert expectedSingleQuoteSettingCase == filteredStringSingleQuoteSettingCase
    assert expectedTripleQuoteSettingCase == filteredStringTripleQuoteSettingCase
    assert expectedBothCasesSingleQuoteSettingCase == filteredStringBothCasesSingleQuoteSettingCase
    assert someCommentsInBetween == filteredStringSomeCommentsInBetween
    assert Constant.NOTHING == filteredStringOnlyComment

@Test(environmentVariables={**{}, **LOG_HELPER_SETTINGS})
def prettyJson_withSucces() :
    # Arrange
    simpleDictionaryInstance = {**{}, **DICTIONARY_INSTANCE}
    expected = '''{
        "11": "yolo",
        "10": 2.2,
        "true": false,
        "key": "value",
        "anotherKey": {
            "key": "value"
        },
        "aThirdKey": [
            "a",
            "b",
            {
                "c": "d"
            },
            [
                null,
                true,
                "True",
                3.3,
                [
                    2,
                    "2"
                ]
            ],
            {
                "key": [
                    "e",
                    "f",
                    {
                        "g": {
                            "h": [
                                "i",
                                "j"
                            ]
                        }
                    }
                ]
            },
            {
                "someKey": "someValue",
                "someOtherKey": [
                    1,
                    2,
                    3,
                    "q",
                    "r",
                    "s"
                ]
            }
        ]
    }'''.replace(Constant.SYSTEM_TAB,Constant.TAB_UNITS * Constant.SPACE)

    # Act
    toAssert = StringHelper.prettyJson(simpleDictionaryInstance, tabCount=1, withColors=True)

    # Assert
    toAssert = StringHelper.removeColors(toAssert)
    assert expected == toAssert

@Test(environmentVariables={**{}, **LOG_HELPER_SETTINGS})
def prettyPython_withSucces() :
    # Arrange
    simpleDictionaryInstance = {**{}, **DICTIONARY_INSTANCE}
    expected = '''{
        11: 'yolo',
        10: 2.2,
        True: False,
        'key': 'value',
        'anotherKey': {
            'key': 'value'
        },
        'aThirdKey': [
            'a',
            'b',
            {
                'c': 'd'
            },
            [
                None,
                True,
                'True',
                3.3,
                (
                    2,
                    '2'
                )
            ],
            {
                'key': (
                    'e',
                    'f',
                    {
                        'g': {
                            'h': [
                                'i',
                                'j'
                            ]
                        }
                    }
                )
            },
            {
                'someKey': 'someValue',
                'someOtherKey': {
                    1,
                    2,
                    3,
                    'q',
                    'r',
                    's'
                }
            }
        ]
    }'''.replace('\t','   ')

    # Act
    toAssert = StringHelper.prettyPython(simpleDictionaryInstance, tabCount=1, withColors=True)
    # log.debug(prettyPython_withSucces, 'does it works ' + toAssert + ' correctly?')

    # Assert
    toAssert = StringHelper.removeColors(toAssert)
    assert expected == toAssert

@Test(environmentVariables={**{}, **LOG_HELPER_SETTINGS})
def filterJson_withSucces() :
    # Arrange
    simpleDictionaryInstance = {'key':'value','anotherKey':{'key':'value'},'aThirdKey':['a','b',{'c':'d'},[None, True, 'True', 3.3, (2,'2')],{'key':('e','f',{'g':{'h':['i','j']}})},{'someKey':'someValue','someOtherKey':{'q','r',1,2,3,'s'}}]}
    expectedWithSpace = '''{        'key': 'value',        'anotherKey': {            'key': 'value'        },        'aThirdKey': [            'a',            'b',            {                'c': 'd'            },            [                None,                True,                'True',                3.3,                (                    2,                    '2'                )            ],            {                'key': (                    'e',                    'f',                    {                        'g': {                            'h': [                                'i',                                'j'                            ]                        }                    }                )            },            {                'someKey': 'someValue',                'someOtherKey': {                    1,                    2,                    3,                    'q',                    'r',                    's'                }            }        ]    }'''
    expectedWithoutSpace = '''{'key':'value','anotherKey':{'key':'value'},'aThirdKey':['a','b',{'c':'d'},[None,True,'True',3.3,(2,'2')],{'key':('e','f',{'g':{'h':['i','j']}})},{'someKey':'someValue','someOtherKey':{1,2,3,'q','r','s'}}]}'''
    filteredJson = StringHelper.prettyPython(simpleDictionaryInstance, tabCount=1, withColors=True)

    # Act
    toAssertWithSpace = StringHelper.filterJson(filteredJson)
    toAssertWithoutSpace = StringHelper.filterJson(filteredJson, extraCharacterList=[' '])

    # Assert
    toAssertWithSpace = StringHelper.removeColors(toAssertWithSpace)
    toAssertWithoutSpace = StringHelper.removeColors(toAssertWithoutSpace)
    assert expectedWithSpace == toAssertWithSpace
    assert expectedWithoutSpace == toAssertWithoutSpace

@Test(environmentVariables={**{}, **LOG_HELPER_SETTINGS})
def isLongString_withSuccess() :
    # Arrange
    tripleSinleQuotes = f'{Constant.TRIPLE_SINGLE_QUOTE}'
    tripleDoubleQuotes = f'{Constant.TRIPLE_DOUBLE_QUOTE}'
    doubleTripleSinleQuotes = f'{2*Constant.TRIPLE_SINGLE_QUOTE}'
    doubleTripleDoubleQuotes = f'{2*Constant.TRIPLE_DOUBLE_QUOTE}'
    doubleTripleSinleAndDoubleQuotes = f"{Constant.TRIPLE_SINGLE_QUOTE}{2*Constant.TRIPLE_DOUBLE_QUOTE}{Constant.TRIPLE_SINGLE_QUOTE}"
    actualLongStringWithTripleSinleQuotes = f'''{Constant.TRIPLE_SINGLE_QUOTE}
        longSring
    {Constant.TRIPLE_SINGLE_QUOTE}'''
    actualLongStringWithTripleDoubleQuotes = f'''{Constant.TRIPLE_DOUBLE_QUOTE}
        longSring
    {Constant.TRIPLE_DOUBLE_QUOTE}'''

    # Act
    toAssertTripleSinleQuotes = StringHelper.isLongString(tripleSinleQuotes)
    toAssertTripleDoubleQuotes = StringHelper.isLongString(tripleDoubleQuotes)
    toAssertDoubleTripleSinleQuotes = StringHelper.isLongString(doubleTripleSinleQuotes)
    toAssertDoubleTripleDoubleQuotes = StringHelper.isLongString(doubleTripleDoubleQuotes)
    toAssertDoubleTripleSinleAndDoubleQuotes = StringHelper.isLongString(doubleTripleSinleAndDoubleQuotes)
    toAssertActualLongStringWithTripleSinleQuotes = StringHelper.isLongString(actualLongStringWithTripleSinleQuotes)
    toAssertActualLongStringWithTripleDoubleQuotes = StringHelper.isLongString(actualLongStringWithTripleDoubleQuotes)

    # Assert
    assert toAssertTripleSinleQuotes
    assert toAssertTripleDoubleQuotes
    assert not toAssertDoubleTripleSinleQuotes
    assert not toAssertDoubleTripleDoubleQuotes
    assert not toAssertDoubleTripleSinleAndDoubleQuotes
    assert not toAssertActualLongStringWithTripleSinleQuotes
    assert not toAssertActualLongStringWithTripleDoubleQuotes
