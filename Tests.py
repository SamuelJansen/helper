from python_helper.api.test.api.src.service import StringHelperTest
from python_helper.api.test.api.src.service import SettingHelperTest
from python_helper.api.test.api.src.service import LogHelperTest
from python_helper.api.test.api.src.service import ObjectHelperTest
from python_helper.api.test.api.src.service import ReflectionHelperTest

StringHelperTest.mustFilterSetting()
StringHelperTest.prettyJson_withSucces()
StringHelperTest.prettyPython_withSucces()
StringHelperTest.filterJson_withSucces()
StringHelperTest.isLongString_withSuccess()

SettingHelperTest.mustReadSettingFile()
SettingHelperTest.mustNotReadSettingFile()
SettingHelperTest.mustPrintSettingTree()

LogHelperTest.mustLogWithColors()
LogHelperTest.mustLogWithoutColors()
LogHelperTest.mustLogWithoutColorsAsWell()
LogHelperTest.mustLogEnvironmentSettings()
LogHelperTest.mustLogPretyPythonWithoutColors()
LogHelperTest.mustLogPretyPythonWithColors()
LogHelperTest.mustLogPretyJsonWithColors()

ObjectHelperTest.basicMethods()
ObjectHelperTest.mustAssertEquals()
ObjectHelperTest.mustIgnoreKeyCorrectly()

ReflectionHelperTest.isNotMethodInstance_withSuccess()
ReflectionHelperTest.overrideSignatures_withSuccess()
