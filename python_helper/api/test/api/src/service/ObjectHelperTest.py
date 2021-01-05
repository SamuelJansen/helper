import json
from python_helper import ObjectHelper, StringHelper, SettingHelper, Constant, log, Test

# LOG_HELPER_SETTINGS = {
#     log.LOG : True,
#     log.SUCCESS : True,
#     log.SETTING : True,
#     log.DEBUG : True,
#     log.WARNING : True,
#     log.FAILURE : True,
#     log.WRAPPER : True,
#     log.ERROR : True,
    # log.TEST : False,
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
    'my_none_value' : None,
    'my_none_value-as_string' : 'None',
    'string_key_as_string' : 'value',
    'integer_key_as_string' : 12345678901,
    10987654321 : 12345678901,
    'bool_key_as_string' : True,
    False : True,
    'float_key_as_string' : 12345.678901,
    109876.54321 : 12345.678901,
    'list_key_as_string' : [
        'my',
        'list',
        'elements'
    ],
    'list_of_list_key_as_string' : [
        [
            'my',
            'first',
            'list',
            False,
            12345.678901
        ],
        [
            'my',
            'second',
            'list',
            True,
            10987654321
        ]
    ],
    'set_of_string_key_as_string' : {
        'a',
        'True',
        '2',
        '3.4',
        True,
        2,
        2.4
    }
}
JSON_INSTANCE = json.loads(StringHelper.prettyJson(DICTIONARY_INSTANCE))

@Test(environmentVariables={**{}, **LOG_HELPER_SETTINGS})
def basicMethods() :
    # Arrange
    def generatorInstance() :
        while True :
            yield False
            break
    STR_INSTANCE = str()
    BOOLEAN_INSTANCE = bool()
    INTEGER_INSTANCE = int()
    FLOAT_INSTANCE = float()
    DICTIONARY_INSTANCE = dict()
    LIST_INSTANCE = list()
    TUPLE_INSTANCE = tuple()
    SET_INSTANCE = set()
    GENERATOR_INSTANCE = generatorInstance()

    STR_FILLED_INSTANCE = 'str()'
    BOOLEAN_FILLED_INSTANCE = True
    INTEGER_FILLED_INSTANCE = 2
    FLOAT_FILLED_INSTANCE = 3.3
    DICTIONARY_FILLED_INSTANCE = {'dict()':dict()}
    LIST_FILLED_INSTANCE = [list(),list()]
    TUPLE_FILLED_INSTANCE = (tuple(),tuple())
    SET_FILLED_INSTANCE = {'set()',2}

    # Act

    # Assert
    assert ObjectHelper.isNotNone(STR_INSTANCE)
    assert ObjectHelper.isNotNone(BOOLEAN_INSTANCE)
    assert ObjectHelper.isNotNone(INTEGER_INSTANCE)
    assert ObjectHelper.isNotNone(FLOAT_INSTANCE)
    assert ObjectHelper.isNotNone(DICTIONARY_INSTANCE)
    assert ObjectHelper.isNotNone(LIST_INSTANCE)
    assert ObjectHelper.isNotNone(TUPLE_INSTANCE)
    assert ObjectHelper.isNotNone(SET_INSTANCE)
    assert ObjectHelper.isNotNone(GENERATOR_INSTANCE)

    assert ObjectHelper.isNotNone(STR_FILLED_INSTANCE)
    assert ObjectHelper.isNotNone(BOOLEAN_FILLED_INSTANCE)
    assert ObjectHelper.isNotNone(INTEGER_FILLED_INSTANCE)
    assert ObjectHelper.isNotNone(FLOAT_FILLED_INSTANCE)
    assert ObjectHelper.isNotNone(DICTIONARY_FILLED_INSTANCE)
    assert ObjectHelper.isNotNone(LIST_FILLED_INSTANCE)
    assert ObjectHelper.isNotNone(TUPLE_FILLED_INSTANCE)
    assert ObjectHelper.isNotNone(SET_FILLED_INSTANCE)

    assert not ObjectHelper.isNone(STR_FILLED_INSTANCE)
    assert not ObjectHelper.isNone(BOOLEAN_FILLED_INSTANCE)
    assert not ObjectHelper.isNone(INTEGER_FILLED_INSTANCE)
    assert not ObjectHelper.isNone(FLOAT_FILLED_INSTANCE)
    assert not ObjectHelper.isNone(DICTIONARY_FILLED_INSTANCE)
    assert not ObjectHelper.isNone(LIST_FILLED_INSTANCE)
    assert not ObjectHelper.isNone(TUPLE_FILLED_INSTANCE)
    assert not ObjectHelper.isNone(SET_FILLED_INSTANCE)
    assert not ObjectHelper.isNone(GENERATOR_INSTANCE)

    assert not ObjectHelper.isList(STR_FILLED_INSTANCE)
    assert not ObjectHelper.isList(BOOLEAN_FILLED_INSTANCE)
    assert not ObjectHelper.isList(INTEGER_FILLED_INSTANCE)
    assert not ObjectHelper.isList(FLOAT_FILLED_INSTANCE)
    assert not ObjectHelper.isList(DICTIONARY_FILLED_INSTANCE)
    assert ObjectHelper.isList(LIST_FILLED_INSTANCE)
    assert not ObjectHelper.isList(TUPLE_FILLED_INSTANCE)
    assert not ObjectHelper.isList(SET_FILLED_INSTANCE)
    assert not ObjectHelper.isList(GENERATOR_INSTANCE)

    assert ObjectHelper.isNotList(STR_FILLED_INSTANCE)
    assert ObjectHelper.isNotList(BOOLEAN_FILLED_INSTANCE)
    assert ObjectHelper.isNotList(INTEGER_FILLED_INSTANCE)
    assert ObjectHelper.isNotList(FLOAT_FILLED_INSTANCE)
    assert ObjectHelper.isNotList(DICTIONARY_FILLED_INSTANCE)
    assert not ObjectHelper.isNotList(LIST_FILLED_INSTANCE)
    assert ObjectHelper.isNotList(TUPLE_FILLED_INSTANCE)
    assert ObjectHelper.isNotList(SET_FILLED_INSTANCE)
    assert ObjectHelper.isNotList(GENERATOR_INSTANCE)

    assert not ObjectHelper.isSet(STR_FILLED_INSTANCE)
    assert not ObjectHelper.isSet(BOOLEAN_FILLED_INSTANCE)
    assert not ObjectHelper.isSet(INTEGER_FILLED_INSTANCE)
    assert not ObjectHelper.isSet(FLOAT_FILLED_INSTANCE)
    assert not ObjectHelper.isSet(DICTIONARY_FILLED_INSTANCE)
    assert not ObjectHelper.isSet(LIST_FILLED_INSTANCE)
    assert not ObjectHelper.isSet(TUPLE_FILLED_INSTANCE)
    assert ObjectHelper.isSet(SET_FILLED_INSTANCE)
    assert not ObjectHelper.isSet(GENERATOR_INSTANCE)

    assert ObjectHelper.isNotSet(STR_FILLED_INSTANCE)
    assert ObjectHelper.isNotSet(BOOLEAN_FILLED_INSTANCE)
    assert ObjectHelper.isNotSet(INTEGER_FILLED_INSTANCE)
    assert ObjectHelper.isNotSet(FLOAT_FILLED_INSTANCE)
    assert ObjectHelper.isNotSet(DICTIONARY_FILLED_INSTANCE)
    assert ObjectHelper.isNotSet(LIST_FILLED_INSTANCE)
    assert ObjectHelper.isNotSet(TUPLE_FILLED_INSTANCE)
    assert not ObjectHelper.isNotSet(SET_FILLED_INSTANCE)
    assert ObjectHelper.isNotSet(GENERATOR_INSTANCE)

    assert not ObjectHelper.isTuple(STR_FILLED_INSTANCE)
    assert not ObjectHelper.isTuple(BOOLEAN_FILLED_INSTANCE)
    assert not ObjectHelper.isTuple(INTEGER_FILLED_INSTANCE)
    assert not ObjectHelper.isTuple(FLOAT_FILLED_INSTANCE)
    assert not ObjectHelper.isTuple(DICTIONARY_FILLED_INSTANCE)
    assert not ObjectHelper.isTuple(LIST_FILLED_INSTANCE)
    assert ObjectHelper.isTuple(TUPLE_FILLED_INSTANCE)
    assert not ObjectHelper.isTuple(SET_FILLED_INSTANCE)
    assert not ObjectHelper.isTuple(GENERATOR_INSTANCE)

    assert ObjectHelper.isNotTuple(STR_FILLED_INSTANCE)
    assert ObjectHelper.isNotTuple(BOOLEAN_FILLED_INSTANCE)
    assert ObjectHelper.isNotTuple(INTEGER_FILLED_INSTANCE)
    assert ObjectHelper.isNotTuple(FLOAT_FILLED_INSTANCE)
    assert ObjectHelper.isNotTuple(DICTIONARY_FILLED_INSTANCE)
    assert ObjectHelper.isNotTuple(LIST_FILLED_INSTANCE)
    assert not ObjectHelper.isNotTuple(TUPLE_FILLED_INSTANCE)
    assert ObjectHelper.isNotTuple(SET_FILLED_INSTANCE)
    assert ObjectHelper.isNotTuple(GENERATOR_INSTANCE)

    assert not ObjectHelper.isDictionary(STR_FILLED_INSTANCE)
    assert not ObjectHelper.isDictionary(BOOLEAN_FILLED_INSTANCE)
    assert not ObjectHelper.isDictionary(INTEGER_FILLED_INSTANCE)
    assert not ObjectHelper.isDictionary(FLOAT_FILLED_INSTANCE)
    assert ObjectHelper.isDictionary(DICTIONARY_FILLED_INSTANCE)
    assert not ObjectHelper.isDictionary(LIST_FILLED_INSTANCE)
    assert not ObjectHelper.isDictionary(TUPLE_FILLED_INSTANCE)
    assert not ObjectHelper.isDictionary(SET_FILLED_INSTANCE)
    assert not ObjectHelper.isDictionary(GENERATOR_INSTANCE)

    assert ObjectHelper.isNotDictionary(STR_FILLED_INSTANCE)
    assert ObjectHelper.isNotDictionary(BOOLEAN_FILLED_INSTANCE)
    assert ObjectHelper.isNotDictionary(INTEGER_FILLED_INSTANCE)
    assert ObjectHelper.isNotDictionary(FLOAT_FILLED_INSTANCE)
    assert not ObjectHelper.isNotDictionary(DICTIONARY_FILLED_INSTANCE)
    assert ObjectHelper.isNotDictionary(LIST_FILLED_INSTANCE)
    assert ObjectHelper.isNotDictionary(TUPLE_FILLED_INSTANCE)
    assert ObjectHelper.isNotDictionary(SET_FILLED_INSTANCE)
    assert ObjectHelper.isNotDictionary(GENERATOR_INSTANCE)

    assert not ObjectHelper.isCollection(STR_FILLED_INSTANCE)
    assert not ObjectHelper.isCollection(BOOLEAN_FILLED_INSTANCE)
    assert not ObjectHelper.isCollection(INTEGER_FILLED_INSTANCE)
    assert not ObjectHelper.isCollection(FLOAT_FILLED_INSTANCE)
    assert ObjectHelper.isCollection(DICTIONARY_FILLED_INSTANCE)
    assert ObjectHelper.isCollection(LIST_FILLED_INSTANCE)
    assert ObjectHelper.isCollection(TUPLE_FILLED_INSTANCE)
    assert ObjectHelper.isCollection(SET_FILLED_INSTANCE)
    assert not ObjectHelper.isCollection(GENERATOR_INSTANCE)

    assert ObjectHelper.isNotCollection(STR_FILLED_INSTANCE)
    assert ObjectHelper.isNotCollection(BOOLEAN_FILLED_INSTANCE)
    assert ObjectHelper.isNotCollection(INTEGER_FILLED_INSTANCE)
    assert ObjectHelper.isNotCollection(FLOAT_FILLED_INSTANCE)
    assert not ObjectHelper.isNotCollection(DICTIONARY_FILLED_INSTANCE)
    assert not ObjectHelper.isNotCollection(LIST_FILLED_INSTANCE)
    assert not ObjectHelper.isNotCollection(TUPLE_FILLED_INSTANCE)
    assert not ObjectHelper.isNotCollection(SET_FILLED_INSTANCE)
    assert ObjectHelper.isNotCollection(GENERATOR_INSTANCE)

    assert not ObjectHelper.isDictionaryClass(STR_FILLED_INSTANCE)
    assert not ObjectHelper.isDictionaryClass(BOOLEAN_FILLED_INSTANCE)
    assert not ObjectHelper.isDictionaryClass(INTEGER_FILLED_INSTANCE)
    assert not ObjectHelper.isDictionaryClass(FLOAT_FILLED_INSTANCE)
    assert not ObjectHelper.isDictionaryClass(DICTIONARY_FILLED_INSTANCE)
    assert not ObjectHelper.isDictionaryClass(LIST_FILLED_INSTANCE)
    assert not ObjectHelper.isDictionaryClass(TUPLE_FILLED_INSTANCE)
    assert not ObjectHelper.isDictionaryClass(SET_FILLED_INSTANCE)
    assert not ObjectHelper.isDictionaryClass(GENERATOR_INSTANCE)

    assert ObjectHelper.isNotDictionaryClass(STR_FILLED_INSTANCE)
    assert ObjectHelper.isNotDictionaryClass(BOOLEAN_FILLED_INSTANCE)
    assert ObjectHelper.isNotDictionaryClass(INTEGER_FILLED_INSTANCE)
    assert ObjectHelper.isNotDictionaryClass(FLOAT_FILLED_INSTANCE)
    assert ObjectHelper.isNotDictionaryClass(DICTIONARY_FILLED_INSTANCE)
    assert ObjectHelper.isNotDictionaryClass(LIST_FILLED_INSTANCE)
    assert ObjectHelper.isNotDictionaryClass(TUPLE_FILLED_INSTANCE)
    assert ObjectHelper.isNotDictionaryClass(SET_FILLED_INSTANCE)
    assert ObjectHelper.isNotDictionaryClass(GENERATOR_INSTANCE)

    assert not ObjectHelper.isDictionaryClass(type(STR_FILLED_INSTANCE))
    assert not ObjectHelper.isDictionaryClass(type(BOOLEAN_FILLED_INSTANCE))
    assert not ObjectHelper.isDictionaryClass(type(INTEGER_FILLED_INSTANCE))
    assert not ObjectHelper.isDictionaryClass(type(FLOAT_FILLED_INSTANCE))
    assert ObjectHelper.isDictionaryClass(type(DICTIONARY_FILLED_INSTANCE))
    assert not ObjectHelper.isDictionaryClass(type(LIST_FILLED_INSTANCE))
    assert not ObjectHelper.isDictionaryClass(type(TUPLE_FILLED_INSTANCE))
    assert not ObjectHelper.isDictionaryClass(type(SET_FILLED_INSTANCE))
    assert not ObjectHelper.isDictionaryClass(type(GENERATOR_INSTANCE))

    assert ObjectHelper.isNotDictionaryClass(type(STR_FILLED_INSTANCE))
    assert ObjectHelper.isNotDictionaryClass(type(BOOLEAN_FILLED_INSTANCE))
    assert ObjectHelper.isNotDictionaryClass(type(INTEGER_FILLED_INSTANCE))
    assert ObjectHelper.isNotDictionaryClass(type(FLOAT_FILLED_INSTANCE))
    assert not ObjectHelper.isNotDictionaryClass(type(DICTIONARY_FILLED_INSTANCE))
    assert ObjectHelper.isNotDictionaryClass(type(LIST_FILLED_INSTANCE))
    assert ObjectHelper.isNotDictionaryClass(type(TUPLE_FILLED_INSTANCE))
    assert ObjectHelper.isNotDictionaryClass(type(SET_FILLED_INSTANCE))
    assert ObjectHelper.isNotDictionaryClass(type(GENERATOR_INSTANCE))

    assert ObjectHelper.isNativeClass(type(STR_FILLED_INSTANCE))
    assert ObjectHelper.isNativeClass(type(BOOLEAN_FILLED_INSTANCE))
    assert ObjectHelper.isNativeClass(type(INTEGER_FILLED_INSTANCE))
    assert ObjectHelper.isNativeClass(type(FLOAT_FILLED_INSTANCE))
    assert not ObjectHelper.isNativeClass(type(DICTIONARY_FILLED_INSTANCE))
    assert not ObjectHelper.isNativeClass(type(LIST_FILLED_INSTANCE))
    assert not ObjectHelper.isNativeClass(type(TUPLE_FILLED_INSTANCE))
    assert not ObjectHelper.isNativeClass(type(SET_FILLED_INSTANCE))
    assert ObjectHelper.isNativeClass(type(GENERATOR_INSTANCE))

    assert not ObjectHelper.isNotNativeClass(type(STR_FILLED_INSTANCE))
    assert not ObjectHelper.isNotNativeClass(type(BOOLEAN_FILLED_INSTANCE))
    assert not ObjectHelper.isNotNativeClass(type(INTEGER_FILLED_INSTANCE))
    assert not ObjectHelper.isNotNativeClass(type(FLOAT_FILLED_INSTANCE))
    assert ObjectHelper.isNotNativeClass(type(DICTIONARY_FILLED_INSTANCE))
    assert ObjectHelper.isNotNativeClass(type(LIST_FILLED_INSTANCE))
    assert ObjectHelper.isNotNativeClass(type(TUPLE_FILLED_INSTANCE))
    assert ObjectHelper.isNotNativeClass(type(SET_FILLED_INSTANCE))
    assert not ObjectHelper.isNotNativeClass(type(GENERATOR_INSTANCE))

    assert ObjectHelper.isNativeClassIsntance(STR_FILLED_INSTANCE)
    assert ObjectHelper.isNativeClassIsntance(BOOLEAN_FILLED_INSTANCE)
    assert ObjectHelper.isNativeClassIsntance(INTEGER_FILLED_INSTANCE)
    assert ObjectHelper.isNativeClassIsntance(FLOAT_FILLED_INSTANCE)
    assert not ObjectHelper.isNativeClassIsntance(DICTIONARY_FILLED_INSTANCE)
    assert not ObjectHelper.isNativeClassIsntance(LIST_FILLED_INSTANCE)
    assert not ObjectHelper.isNativeClassIsntance(TUPLE_FILLED_INSTANCE)
    assert not ObjectHelper.isNativeClassIsntance(SET_FILLED_INSTANCE)
    assert ObjectHelper.isNativeClassIsntance(GENERATOR_INSTANCE)

    assert not ObjectHelper.isNotNativeClassIsntance(STR_FILLED_INSTANCE)
    assert not ObjectHelper.isNotNativeClassIsntance(BOOLEAN_FILLED_INSTANCE)
    assert not ObjectHelper.isNotNativeClassIsntance(INTEGER_FILLED_INSTANCE)
    assert not ObjectHelper.isNotNativeClassIsntance(FLOAT_FILLED_INSTANCE)
    assert ObjectHelper.isNotNativeClassIsntance(DICTIONARY_FILLED_INSTANCE)
    assert ObjectHelper.isNotNativeClassIsntance(LIST_FILLED_INSTANCE)
    assert ObjectHelper.isNotNativeClassIsntance(TUPLE_FILLED_INSTANCE)
    assert ObjectHelper.isNotNativeClassIsntance(SET_FILLED_INSTANCE)
    assert not ObjectHelper.isNotNativeClassIsntance(GENERATOR_INSTANCE)

    assert ObjectHelper.isNone(None)
    assert not ObjectHelper.isNotNone(None)
    assert not ObjectHelper.isList(None)
    assert ObjectHelper.isNotList(None)
    assert not ObjectHelper.isSet(None)
    assert ObjectHelper.isNotSet(None)
    assert not ObjectHelper.isTuple(None)
    assert ObjectHelper.isNotTuple(None)
    assert not ObjectHelper.isDictionary(None)
    assert ObjectHelper.isNotDictionary(None)
    assert not ObjectHelper.isCollection(None)
    assert ObjectHelper.isNotCollection(None)
    assert not ObjectHelper.isDictionaryClass(None)
    assert ObjectHelper.isNotDictionaryClass(None)
    assert not ObjectHelper.isNativeClass(None)
    assert ObjectHelper.isNotNativeClass(None)
    assert not ObjectHelper.isNativeClassIsntance(None)
    assert ObjectHelper.isNotNativeClassIsntance(None)

    assert not ObjectHelper.isNone(type(None))
    assert ObjectHelper.isNotNone(type(None))
    assert not ObjectHelper.isList(type(None))
    assert ObjectHelper.isNotList(type(None))
    assert not ObjectHelper.isDictionary(type(None))
    assert ObjectHelper.isNotDictionary(type(None))
    assert not ObjectHelper.isCollection(type(None))
    assert ObjectHelper.isNotCollection(type(None))
    assert not ObjectHelper.isDictionaryClass(type(None))
    assert ObjectHelper.isNotDictionaryClass(type(None))
    assert not ObjectHelper.isNativeClass(type(None))
    assert ObjectHelper.isNotNativeClass(type(None))
    assert not ObjectHelper.isNativeClassIsntance(type(None))
    assert ObjectHelper.isNotNativeClassIsntance(type(None))

@Test(environmentVariables={**{}, **LOG_HELPER_SETTINGS})
def mustAssertEquals() :
    # Arrange
    dictionaryInstance = {**{},**JSON_INSTANCE}
    someDictionary = {
        'a' : 'b',
        'c' : 'd',
        'e' : {
            'f' : 'g',
            't' : [
                {
                    's1',
                    's1',
                    's3',
                    1,
                    3.3,
                    False,
                    None
                },
                {
                    's1',
                    False,
                    's3',
                    3.3,
                    1,
                    None
                }
            ],
            1 : 7,
            False : 2.3
        },
        2.2 : {
            False,
            2,
            None,
            'string'
        },
        'tuple' : (
            2,
            3,
            '3',
            9
        )
    }
    someOtherDictionary = {
        'c' : 'd',
        'a' : 'b',
        'e' : {
            False : 2.3,
            1 : 7,
            'f' : 'g',
            't' : [
                {
                    3.3,
                    's1',
                    's3',
                    1,
                    None,
                    False
                },
                {
                    's1',
                    's1',
                    's3',
                    None,
                    1,
                    3.3,
                    False
                }
            ]
        },
        2.2 : {
            False,
            2,
            None,
            'string'
        },
        'tuple' : (
            2,
            9,
            3,
            '3'
        )
    }
    differentDictionary = {
        'c' : 'd',
        'a' : 'b',
        'e' : {
            False : 2.3,
            1 : 7,
            'f' : 'g',
            't' : [
                {
                    's1',
                    's3',
                    1,
                    3.3,
                    False,
                    None
                },
                {
                    's1',
                    's1',
                    's3',
                    1,
                    3.3,
                    False,
                    None
                }
            ]
        },
        2.2 : {
            False,
            2,
            None,
            str()
        },
        'tuple' : (
            9,
            2,
            3,
            '3'
        )
    }

    # Act
    toAssert = ObjectHelper.equal(dictionaryInstance, JSON_INSTANCE, ignoreCharactereList=[Constant.NEW_LINE])
    unsortedDictionaryToAssert = ObjectHelper.equal(someDictionary, someOtherDictionary)
    notEqualsToAssert = ObjectHelper.equal(someDictionary, differentDictionary)

    # Assert
    assert toAssert
    assert unsortedDictionaryToAssert
    assert not notEqualsToAssert

@Test(environmentVariables={**{}, **LOG_HELPER_SETTINGS})
def mustIgnoreKeyCorrectly() :
    # Arrange
    expected = {**{},**DICTIONARY_INSTANCE}
    anotherDictionaryInstance = {**{},**DICTIONARY_INSTANCE}
    IGNORABLE_KEY = 'ignorableKey'
    anotherDictionaryInstance[IGNORABLE_KEY] = 'ignorableValue'

    # Act
    toAssert = ObjectHelper.filterIgnoreKeyList(anotherDictionaryInstance,[IGNORABLE_KEY])

    # Assert
    assert ObjectHelper.equal(expected, toAssert)
