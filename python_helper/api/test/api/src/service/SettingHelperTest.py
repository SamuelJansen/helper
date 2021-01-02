from python_helper import SettingHelper, StringHelper, Constant, log, EnvironmentVariable, EnvironmentHelper, ObjectHelper

# LOG_HELPER_SETTINGS = {
#     log.LOG : True,
#     log.SUCCESS : True,
#     log.SETTING : True,
#     log.DEBUG : True,
#     log.WARNING : True,
#     log.WRAPPER : True,
#     log.FAILURE : True,
#     log.ERROR : True
# }

LOG_HELPER_SETTINGS = {
    log.LOG : False,
    log.SUCCESS : False,
    log.SETTING : False,
    log.DEBUG : False,
    log.WARNING : False,
    log.WRAPPER : False,
    log.FAILURE : False,
    log.ERROR : False
}

@EnvironmentVariable(environmentVariables={
    SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT,
    'MY_COMPLEX_ENV' : ' -- my complex value -- ',
    'LATE_VALUE' : '-- late environment value --',
    'ONLY_ENVIRONMENT_VARIABLE' : 'only environment variable value',
    **LOG_HELPER_SETTINGS
})
def mustReadSettingFile() :
    # Arrange
    settingFilePath = str(EnvironmentHelper.OS_SEPARATOR).join(['python_helper', 'api', 'test', 'api', 'resource','application.yml'])

    # Act
    readdedSettingTree = SettingHelper.getSettingTree(settingFilePath, keepDepthInLongString=True)
    # log.prettyPython(mustReadSettingFile, '', readdedSettingTree)

    # Assert
    assert 'self reference value' == SettingHelper.getSetting('my.self-reference-key', readdedSettingTree)
    assert 'other self reference value as well' == SettingHelper.getSetting('my.other.self-reference-key.as-well', readdedSettingTree)
    assert 'other repeated self reference value as well' == SettingHelper.getSetting('my.other.repeated.self-reference-key.as-well', readdedSettingTree)
    assert 'my default value' == SettingHelper.getSetting('my.configuration-without-environment-variable-key', readdedSettingTree)
    assert "my default value" == SettingHelper.getSetting('my.configuration-without-environment-variable-key-with-value-surrounded-by-single-quotes', readdedSettingTree)
    assert 'my default value' == SettingHelper.getSetting('my.configuration-without-environment-variable-key-and-space-after-colon', readdedSettingTree)
    assert 'self reference value' == SettingHelper.getSetting('my.configuration', readdedSettingTree)
    assert 'self reference value' == SettingHelper.getSetting('my.own.configuration', readdedSettingTree)
    assert 'other root value' == SettingHelper.getSetting('other.root.key', readdedSettingTree)
    assert 'other root value' == SettingHelper.getSetting('my.own.very.deep.configuration', readdedSettingTree)
    assert 'other self reference value as well' == SettingHelper.getSetting('my.other-with-other-name.self-reference-key.as-well', readdedSettingTree)
    assert 'self reference value' == SettingHelper.getSetting('my.other-with-other-name.configuration', readdedSettingTree)
    assert 'other self reference value as well' == SettingHelper.getSetting('my.other-with-other-name.configuration-as-well', readdedSettingTree)
    assert 'other repeated self reference value as well' == SettingHelper.getSetting('my.other-with-other-name.configuration-repeated-as-well', readdedSettingTree)
    assert SettingHelper.getSetting('my.override-case.overridden', readdedSettingTree) is None
    assert 'overrider configuration' == SettingHelper.getSetting('my.override-case.overrider', readdedSettingTree)

    assert 'delayed assignment value' == SettingHelper.getSetting('some-reference.before-its-assignment', readdedSettingTree)
    assert 'delayed assignment value' == SettingHelper.getSetting('some-reference.much.before-its-assignment', readdedSettingTree)
    assert "'''  value  ''' with spaces" == SettingHelper.getSetting('some-key.with-an-enter-in-between-the-previous-one', readdedSettingTree)
    assert f'''Hi
                every
            one''' == SettingHelper.getSetting('long.string', readdedSettingTree)
    assert f'''Hi
                            every
                            one
                            this
                            is
                            the
                            deepest
                            long
                                        string
                            here''' == SettingHelper.getSetting('deepest.long.string.ever.long.string', readdedSettingTree)
    assert f'''me
                    being
        not
                    fshds''' == SettingHelper.getSetting('not.idented.long.string', readdedSettingTree)
    assert 'abcdefg' == SettingHelper.getSetting('it.contains.one-setting-injection', readdedSettingTree)
    assert 'abcdefghijklm' == SettingHelper.getSetting('it.contains.two-consecutive-setting-injection', readdedSettingTree)
    assert 'abcdefghijklm' == SettingHelper.getSetting('it.contains.one-inside-of-the-other-setting-injection', readdedSettingTree)
    assert 'ABCD-- my complex value --EFG' == SettingHelper.getSetting('it.contains.one-setting-injection-with-environment-variable', readdedSettingTree)
    assert 'ABCDEFGEFG-- my complex value --HIJKLMNOP' == SettingHelper.getSetting('it.contains.one-inside-of-the-other-setting-injection-with-environment-variable', readdedSettingTree)
    assert 'abcdefghijklm' == SettingHelper.getSetting('it.contains.two-consecutive-setting-injection-with-missing-environment-variable', readdedSettingTree)
    assert 'abcd-- late value ----abcd---- late value ----abcd--efg' == SettingHelper.getSetting('it.contains.some-composed-key.pointing-to.a-late-value', readdedSettingTree)
    assert 'abcd-- late environment value ----abcd--it.contains.late-value--abcd--efg' == SettingHelper.getSetting('it.contains.some-composed-key.pointing-to.a-late-value-with-an-environment-variable-in-between', readdedSettingTree)
    assert '-- late value --' == SettingHelper.getSetting('it.contains.late-value', readdedSettingTree)
    assert 'only environment variable value' == SettingHelper.getSetting('it.contains.environment-variable.only', readdedSettingTree)
    assert 'ABCD -- only environment variable value -- EFGH' == SettingHelper.getSetting('it.contains.environment-variable.surrounded-by-default-values', readdedSettingTree)
    assert 'ABCD -- "some value followed by: "only environment variable value\' and some following default value\' -- EFGH' == SettingHelper.getSetting('it.contains.environment-variable.in-between-default-values', readdedSettingTree)
    assert 'ABCD -- very late definiton value -- EFGH' == SettingHelper.getSetting('it.contains.refference.to-a-late-definition', readdedSettingTree)
    assert 222233444 == SettingHelper.getSetting('handle.integer', readdedSettingTree)
    assert 2.3 == SettingHelper.getSetting('handle.float', readdedSettingTree)
    assert True == SettingHelper.getSetting('handle.boolean', readdedSettingTree)
    assert 222233444 == SettingHelper.getSetting('handle.late.integer', readdedSettingTree)
    assert 2.3 == SettingHelper.getSetting('handle.late.float', readdedSettingTree)
    assert True == SettingHelper.getSetting('handle.late.boolean', readdedSettingTree)
    assert [] == SettingHelper.getSetting('handle.empty.list', readdedSettingTree)
    assert {} == SettingHelper.getSetting('handle.empty.dictionary-or-set', readdedSettingTree)
    assert (()) == SettingHelper.getSetting('handle.empty.tuple', readdedSettingTree)
    assert 'ABCD -- 222233444 -- EFGH' == SettingHelper.getSetting('some-not-string-selfreference.integer', readdedSettingTree)
    assert 'ABCD -- 2.3 -- EFGH' == SettingHelper.getSetting('some-not-string-selfreference.float', readdedSettingTree)
    assert 'ABCD -- True -- EFGH' == SettingHelper.getSetting('some-not-string-selfreference.boolean', readdedSettingTree)

@EnvironmentVariable(environmentVariables={
    **{},
    **LOG_HELPER_SETTINGS
})
def mustNotReadSettingFile() :
    # Arrange
    settingFilePath = str(EnvironmentHelper.OS_SEPARATOR).join(['python_helper', 'api', 'test', 'api', 'resource','application-circular-reference.yml'])

    # Act
    readdedSettingTree = {}
    exception = None
    try :
        readdedSettingTree = SettingHelper.getSettingTree(settingFilePath, keepDepthInLongString=True)
    except Exception as ext :
        exception = ext

    # Assert
    assert {} == readdedSettingTree

    circularReferenceSettingInjectionDictionary = {
        'circular.reference.on.key': {
            'SETTING_KEY': 'key',
            'SETTING_VALUE': '${circular.reference.on.other-key}',
            'SETTING_NODE_KEY': 'circular.reference.on'
        },
        'circular.reference.on.other-key': {
            'SETTING_KEY': 'other-key',
            'SETTING_VALUE': '${circular.reference.on.key}',
            'SETTING_NODE_KEY': 'circular.reference.on'
        },
        'circular.key': {
            'SETTING_KEY': 'key',
            'SETTING_VALUE': '${circular.other-key}',
            'SETTING_NODE_KEY': 'circular'
        },
        'circular.other-key': {
            'SETTING_KEY': 'other-key',
            'SETTING_VALUE': '${circular.key}',
            'SETTING_NODE_KEY': 'circular'
        }
    }

    exceptionMessage = f'Circular reference detected in following setting injections: {StringHelper.prettyPython(circularReferenceSettingInjectionDictionary)}'

    assert exceptionMessage == str(exception)



@EnvironmentVariable(environmentVariables={
    SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT,
    **LOG_HELPER_SETTINGS
})
def mustPrintSettingTree() :
    # Arrange
    settingFilePath = str(EnvironmentHelper.OS_SEPARATOR).join(['python_helper', 'api', 'test', 'api', 'resource','application.yml'])
    readdedSettingTree = SettingHelper.getSettingTree(settingFilePath, keepDepthInLongString=True)

    # Act
    SettingHelper.printSettings(readdedSettingTree,'some name')

    # Assert
    assert ObjectHelper.isNotNone(readdedSettingTree)

def querySetting_withSuccess() :
    # Arrange
    tree = {
        'key' : {
            'key' : {
                'some-query-key' : {
                    'key' : {
                        'key' : {
                            'some-query-key' : 'value',
                            'key' : 'value'
                        }
                    },
                    'other-key' : {
                        'key' : {
                            'other-key' : 'value',
                            'key' : 'value'
                        }
                    }
                },
                'key' : {
                    'key' : {
                        'key' : {
                            'other-key' : 'value',
                            'key' : 'value'
                        }
                    },
                    'other-key' : {
                        'key' : {
                            'other-key' : 'value',
                            'key' : 'value'
                        }
                    }
                },
                'other-key' : {
                    'key' : {
                        'key' : {
                            'other-key' : 'value',
                            'key' : 'value'
                        }
                    },
                    'other-key' : {
                        'key' : {
                            'other-key' : 'value',
                            'key' : {
                                'some-query-key' : 'value',
                                'key' : 'value'
                            }
                        }
                    }
                }
            }
        },
        'other-key' : 'value'
    }

    # Act
    queryTree = SettingHelper.querySetting('some-query-key',tree)

    # Assert
    assert {
        'key.key.some-query-key': {
            'key': {
                'key': {
                    'some-query-key': 'value',
                    'key': 'value'
                }
            },
            'other-key': {
                'key': {
                    'other-key': 'value',
                    'key': 'value'
                }
            }
        },
        'key.key.some-query-key.key.key.some-query-key': 'value',
        'key.key.other-key.other-key.key.key.some-query-key': 'value'
    } == queryTree

@EnvironmentVariable(environmentVariables={
    SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT,
    **LOG_HELPER_SETTINGS
})
def mustHandleSettingValueInFallbackSettingTree() :
    # Arrange
    settingFallbackFilePath = str(EnvironmentHelper.OS_SEPARATOR).join(['python_helper', 'api', 'test', 'api', 'resource','fallback-application.yml'])
    settingFilePath = str(EnvironmentHelper.OS_SEPARATOR).join(['python_helper', 'api', 'test', 'api', 'resource','referencing-fallback-application.yml'])

    # Act
    readdedSettingFallbackFilePath = SettingHelper.getSettingTree(settingFallbackFilePath)
    readdedSettingTree = SettingHelper.getSettingTree(settingFilePath, keepDepthInLongString=True, fallbackSettingTree=readdedSettingFallbackFilePath)
    # log.prettyPython(mustHandleSettingValueInFallbackSettingTree, '', readdedSettingTree)

    # Assert
    assert [] == SettingHelper.getSetting('reffer-to.fallback-settings.empty.list', readdedSettingTree)
    assert 'ABCD -- [] -- EFGH' == SettingHelper.getSetting('reffer-to.fallback-settings.empty.list-in-between', readdedSettingTree)
    assert (()) == SettingHelper.getSetting('reffer-to.fallback-settings.empty.tuple', readdedSettingTree)
    assert 'ABCD -- () -- EFGH' == SettingHelper.getSetting('reffer-to.fallback-settings.empty.tuple-in-between', readdedSettingTree)
    assert {} == SettingHelper.getSetting('reffer-to.fallback-settings.empty.set-or-dictionary', readdedSettingTree)
    assert 'ABCD -- {} -- EFGH' == SettingHelper.getSetting('reffer-to.fallback-settings.empty.set-or-dictionary-in-between', readdedSettingTree)

    assert [
        'a',
        'b',
        'c'
    ] == SettingHelper.getSetting('reffer-to.fallback-settings.not-empty.list', readdedSettingTree)
    assert "ABCD -- ['a', 'b', 'c'] -- EFGH" == SettingHelper.getSetting('reffer-to.fallback-settings.not-empty.list-in-between', readdedSettingTree)
    assert (
        True,
        False,
        'None'
    ) == SettingHelper.getSetting('reffer-to.fallback-settings.not-empty.tuple', readdedSettingTree)
    assert "ABCD -- (True, False, 'None') -- EFGH" == SettingHelper.getSetting('reffer-to.fallback-settings.not-empty.tuple-in-between', readdedSettingTree)
    assert {} == SettingHelper.getSetting('reffer-to.fallback-settings.not-empty.set', readdedSettingTree)
    assert 'ABCD -- {} -- EFGH' == SettingHelper.getSetting('reffer-to.fallback-settings.not-empty.set-in-between', readdedSettingTree)
    assert {
        '1': 20,
        '2': 10,
        '3': 30
    } == SettingHelper.getSetting('reffer-to.fallback-settings.not-empty.dictionary', readdedSettingTree)
    assert "ABCD -- {'1': 20, '2': 10, '3': 30} -- EFGH" == SettingHelper.getSetting('reffer-to.fallback-settings.not-empty.dictionary-in-between', readdedSettingTree)
    assert "fallback value" == SettingHelper.getSetting('reffer-to.fallback-settings.string', readdedSettingTree)
    assert "ABCD -- fallback value -- EFGH" == SettingHelper.getSetting('reffer-to.fallback-settings.string-in-between', readdedSettingTree)

    assert 222233444 == SettingHelper.getSetting('reffer-to.fallback-settings.integer', readdedSettingTree)
    assert "ABCD -- 222233444 -- EFGH" == SettingHelper.getSetting('reffer-to.fallback-settings.integer-in-between', readdedSettingTree)

    assert 2.3 == SettingHelper.getSetting('reffer-to.fallback-settings.float', readdedSettingTree)
    assert "ABCD -- 2.3 -- EFGH" == SettingHelper.getSetting('reffer-to.fallback-settings.float-in-between', readdedSettingTree)

    assert True == SettingHelper.getSetting('reffer-to.fallback-settings.boolean', readdedSettingTree)
    assert "ABCD -- True -- EFGH" == SettingHelper.getSetting('reffer-to.fallback-settings.boolean-in-between', readdedSettingTree)

    assert 'None' == SettingHelper.getSetting('reffer-to.fallback-settings.none', readdedSettingTree)
    assert "ABCD -- None -- EFGH" == SettingHelper.getSetting('reffer-to.fallback-settings.none-in-between', readdedSettingTree)

@EnvironmentVariable(environmentVariables={
    SettingHelper.ACTIVE_ENVIRONMENT : None,
    **LOG_HELPER_SETTINGS
})
def updateActiveEnvironment_withSuccess() :
    # Arrange
    originalActiveEnvironment = EnvironmentHelper.getEnvironmentValue(SettingHelper.ACTIVE_ENVIRONMENT)
    originalActiveEnvironmentIsDefault = SettingHelper.activeEnvironmentIsDefault()
    originalGottenActiveEnvironment = SettingHelper.getActiveEnvironment()
    myNewActiveEnvironment = 'my new artive environment'
    originalACTIVE_ENVIRONMENT_VALUE = SettingHelper.ACTIVE_ENVIRONMENT_VALUE

    # Act
    myGottenNewActiveEnvironment = SettingHelper.updateActiveEnvironment(myNewActiveEnvironment)

    # Assert
    assert SettingHelper.DEFAULT_ENVIRONMENT == originalActiveEnvironment
    assert True == originalActiveEnvironmentIsDefault
    assert SettingHelper.DEFAULT_ENVIRONMENT == originalGottenActiveEnvironment
    assert myNewActiveEnvironment == EnvironmentHelper.getEnvironmentValue(SettingHelper.ACTIVE_ENVIRONMENT)
    assert False == SettingHelper.activeEnvironmentIsDefault()
    assert myNewActiveEnvironment == SettingHelper.getActiveEnvironment()
    assert ObjectHelper.isNotEmpty(myGottenNewActiveEnvironment)
    assert myGottenNewActiveEnvironment == myNewActiveEnvironment
    assert SettingHelper.DEFAULT_ENVIRONMENT == originalACTIVE_ENVIRONMENT_VALUE
    assert SettingHelper.ACTIVE_ENVIRONMENT_VALUE == myNewActiveEnvironment
