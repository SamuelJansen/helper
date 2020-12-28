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
    # print(StringHelper.prettyPython(readdedSettingTree))

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

@EnvironmentVariable(environmentVariables={
    **{},
    **LOG_HELPER_SETTINGS
})
def mustNotReadSettingFile() :
    # Arrange
    settingFilePath = str(EnvironmentHelper.OS_SEPARATOR).join(['python_helper', 'api', 'test', 'api', 'resource','application-circular-reference.yml'])

    # Act
    readdedSettingTree = {}
    ext = None
    try :
        readdedSettingTree = SettingHelper.getSettingTree(settingFilePath, keepDepthInLongString=True)
    except Exception as exception :
        ext = exception
        print(exception)

    # Assert
    assert {} == readdedSettingTree

    assert f"""Circular reference detected in following setting injections: {Constant.OPEN_DICTIONARY}
        'circular.reference.on.key': '${Constant.OPEN_DICTIONARY}circular.reference.on.other-key{Constant.CLOSE_DICTIONARY}',
        'circular.reference.on.other-key': '${Constant.OPEN_DICTIONARY}circular.reference.on.key{Constant.CLOSE_DICTIONARY}',
        'circular.key': '${Constant.OPEN_DICTIONARY}circular.other-key{Constant.CLOSE_DICTIONARY}',
        'circular.other-key': '${Constant.OPEN_DICTIONARY}circular.key{Constant.CLOSE_DICTIONARY}'
    {Constant.CLOSE_DICTIONARY}
    """.replace('\n','').replace('\t',Constant.TAB).replace(' ', '') == str(ext).replace(' ', '').replace('\t',Constant.TAB).replace('\n','')


    # assert f"""Circular reference detected in following setting injection list: [
    #     'circular.reference.on.key: ${Constant.OPEN_DICTIONARY}circular.reference.on.other-key{Constant.CLOSE_DICTIONARY}',
    #     'circular.reference.on.other-key: ${Constant.OPEN_DICTIONARY}circular.reference.on.key{Constant.CLOSE_DICTIONARY}',
    #     'circular.key: ${Constant.OPEN_DICTIONARY}circular.other-key{Constant.CLOSE_DICTIONARY}',
    #     'circular.other-key: ${Constant.OPEN_DICTIONARY}circular.key{Constant.CLOSE_DICTIONARY}'
    # ]""".replace(' ', '') == str(ext).replace(' ', '')

@EnvironmentVariable(environmentVariables={
    SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT
})
def mustPrintSettingTree() :
    # Arrange
    settingFilePath = str(EnvironmentHelper.OS_SEPARATOR).join(['python_helper', 'api', 'test', 'api', 'resource','application.yml'])
    readdedSettingTree = SettingHelper.getSettingTree(settingFilePath, keepDepthInLongString=True)

    # Act
    SettingHelper.printSettings(readdedSettingTree,'some name')

    # Assert
    assert ObjectHelper.isNotNone(readdedSettingTree)
