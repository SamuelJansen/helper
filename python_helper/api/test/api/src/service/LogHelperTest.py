from python_helper import log, SettingHelper, StringHelper, EnvironmentVariable, EnvironmentHelper

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

@EnvironmentVariable(environmentVariables={
    log.LOG : True,
    log.SUCCESS : True,
    log.SETTING : True,
    log.DEBUG : True,
    log.WARNING : True,
    log.WRAPPER : True,
    log.FAILURE : True,
    log.ERROR : True,
    SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT
})
def mustLogWithColors() :
    # Arrange
    noExceptionThrown = 'exception not thrown'
    someLogMessage = 'some log message'
    someExceptionMessage = 'some exception message'
    someInnerExceptionMessage = 'some inner exception message'
    exception = None
    def controlableException(logType) :
        try :
            raise Exception(someExceptionMessage)
        except Exception as e :
            if log.log == logType :
                logType(logType, someLogMessage, exception=e)
            else :
                logType(logType, someLogMessage, e)

    # Act
    log.success(log.success, someLogMessage)
    log.setting(log.setting, someLogMessage)
    log.debug(log.debug, someLogMessage)
    log.warning(log.warning, someLogMessage)
    controlableException(log.wraper)
    controlableException(log.failure)
    controlableException(log.error)
    log.wraper(log.wraper, noExceptionThrown, None)
    log.failure(log.failure, noExceptionThrown, None)
    log.error(log.error, noExceptionThrown, None)
    log.log(log.log, someLogMessage, None)
    controlableException(log.log)

    # Assert
    assert True == SettingHelper.activeEnvironmentIsLocal()
    assert 'local' == EnvironmentHelper.getEnvironmentValue(SettingHelper.ACTIVE_ENVIRONMENT)

@EnvironmentVariable(environmentVariables={
    log.LOG : True,
    log.SUCCESS : True,
    log.SETTING : True,
    log.DEBUG : True,
    log.WARNING : True,
    log.WRAPPER : True,
    log.FAILURE : True,
    log.ERROR : True,
    SettingHelper.ACTIVE_ENVIRONMENT : 'my environment'
})
def mustLogWithoutColors() :
    # Arrange
    noExceptionThrown = 'exception not thrown'
    someLogMessage = 'some log message'
    someExceptionMessage = 'some exception message'
    someInnerExceptionMessage = 'some inner exception message'
    exception = None
    def controlableException(logType) :
        try :
            raise Exception(someExceptionMessage)
        except Exception as e :
            if log.log == logType :
                logType(logType, someLogMessage, exception=e)
            else :
                logType(logType, someLogMessage, e)

    # Act
    log.success(log.success, someLogMessage)
    log.setting(log.setting, someLogMessage)
    log.debug(log.debug, someLogMessage)
    log.warning(log.warning, someLogMessage)
    controlableException(log.wraper)
    controlableException(log.failure)
    controlableException(log.error)
    log.wraper(log.wraper, noExceptionThrown, None)
    log.failure(log.failure, noExceptionThrown, None)
    log.error(log.error, noExceptionThrown, None)
    log.log(log.log, someLogMessage, None)
    controlableException(log.log)

    # Assert
    assert 'my environment' == EnvironmentHelper.getEnvironmentValue(SettingHelper.ACTIVE_ENVIRONMENT)

@EnvironmentVariable(environmentVariables={
    log.LOG : True,
    log.SUCCESS : True,
    log.SETTING : True,
    log.DEBUG : True,
    log.WARNING : True,
    log.WRAPPER : True,
    log.FAILURE : True,
    log.ERROR : True,
    SettingHelper.ACTIVE_ENVIRONMENT : None
})
def mustLogWithoutColorsAsWell() :
    # Arrange
    someLogMessage = 'some log message'
    someExceptionMessage = 'some exception message'
    someInnerExceptionMessage = 'some inner exception message'
    exception = None
    def controlableException(logType) :
        try :
            raise Exception(someExceptionMessage)
        except Exception as exception :
            logType(logType, someLogMessage, exception)

    # Act
    log.success(log.success, someLogMessage)
    log.setting(log.setting, someLogMessage)
    log.debug(log.debug, someLogMessage)
    log.warning(log.warning, someLogMessage)
    controlableException(log.wraper)
    controlableException(log.failure)
    controlableException(log.error)

    # Assert
    assert True == SettingHelper.activeEnvironmentIsDefault()
    assert EnvironmentHelper.getEnvironmentValue(SettingHelper.ACTIVE_ENVIRONMENT) is None
    assert 'default' == SettingHelper.getActiveEnvironment()

@EnvironmentVariable(environmentVariables={
    log.LOG : False,
    log.SUCCESS : False,
    log.SETTING : True,
    log.DEBUG : False,
    log.WARNING : False,
    log.WRAPPER : False,
    log.FAILURE : True,
    log.ERROR : True,
    SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT,
    'SOME_PARTICULAR_SETTING' : '"some value"'
})
def mustLogEnvironmentSettings() :
    # Arrange

    # Act
    SettingHelper.logEnvironmentSettings()

    # Assert
    assert True == SettingHelper.activeEnvironmentIsLocal()
    assert 'local' == SettingHelper.getActiveEnvironment()
    assert "some value" == EnvironmentHelper.getEnvironmentValue('SOME_PARTICULAR_SETTING')

@EnvironmentVariable(environmentVariables={
    log.LOG : True,
    log.SUCCESS : False,
    log.SETTING : False,
    log.DEBUG : False,
    log.WARNING : False,
    log.WRAPPER : False,
    log.FAILURE : True,
    log.ERROR : False,
    SettingHelper.ACTIVE_ENVIRONMENT : None
})
def mustLogPretyPythonWithoutColors() :
    # Arrange
    dictionaryInstance = {**{}, **DICTIONARY_INSTANCE}
    exception = None

    # Act
    try :
        log.prettyPython(mustLogPretyPythonWithoutColors, 'prettyPythonWithoutColors', dictionaryInstance)
    except Exception as e :
        log.failure(mustLogPretyPythonWithoutColors, 'Failed to log prety python in this method call', e)
        exception = e

    # Assert
    assert exception is None

@EnvironmentVariable(environmentVariables={
    log.LOG : True,
    log.SUCCESS : False,
    log.SETTING : False,
    log.DEBUG : False,
    log.WARNING : False,
    log.WRAPPER : False,
    log.FAILURE : True,
    log.ERROR : False,
    SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT
})
def mustLogPretyPythonWithColors() :
    # Arrange
    dictionaryInstance = {**{}, **DICTIONARY_INSTANCE}
    exception = None

    # Act
    try :
        log.prettyPython(mustLogPretyPythonWithColors, 'prettyPython', dictionaryInstance)
    except Exception as e :
        log.failure(mustLogPretyPythonWithColors, 'Failed to log prety python in this method call', e)
        exception = e

    # Assert
    assert exception is None

@EnvironmentVariable(environmentVariables={
    log.LOG : True,
    log.SUCCESS : False,
    log.SETTING : False,
    log.DEBUG : False,
    log.WARNING : False,
    log.WRAPPER : False,
    log.FAILURE : True,
    log.ERROR : False,
    SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT
})
def mustLogPretyJsonWithColors() :
    # Arrange
    dictionaryInstance = {**{}, **DICTIONARY_INSTANCE}
    exception = None

    # Act
    try :
        log.prettyJson(mustLogPretyJsonWithColors, 'prettyJson', dictionaryInstance)
    except Exception as e :
        log.failure(mustLogPretyJsonWithColors, 'Failed to log prety json in this method call', e)
        exception = e

    # Assert
    assert exception is None
