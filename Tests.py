from python_helper.api.test.api.src.service import StringHelperTest
from python_helper.api.test.api.src.service import SettingHelperTest
from python_helper.api.test.api.src.service import LogHelperTest
from python_helper.api.test.api.src.service import ObjectHelperTest
from python_helper.api.test.api.src.service import ReflectionHelperTest
from python_helper.api.test.api.src.service import RandomHelperTest
from python_helper.api.test.api.src.service import MethodAnnotationTest
from python_helper.api.test.api.src.annotation import TestTest

import time
startTime = time.time()

TestTest.mustRun_withSuccess()
TestTest.mustRun_withFailure()
TestTest.mustRun_withSuccess_ExecutingActionFirst()
TestTest.mustRun_withFailre_ExecutingActionFirst()
TestTest.mustRun_withSuccess_ExecutingActionFirst_withFailure()
TestTest.mustRun_withFailre_ExecutingActionFirst_withFailre()
TestTest.mustRun_withSuccess_ExecutingActionLater()
TestTest.mustRun_withFailre_ExecutingActionLater()
TestTest.mustRun_withSuccess_ExecutingActionLater_withFailure()
TestTest.mustRun_withFailre_ExecutingActionLater_withFailre()
TestTest.handleEnvironmentChangesProperly_withSuccess()
TestTest.handleEnvironmentChangesProperly_withErrorBefore()
TestTest.handleEnvironmentChangesProperly_withErrorAfter()
TestTest.handleEnvironmentChangesProperly_withError()

SettingHelperTest.updateActiveEnvironment_withSuccess()
SettingHelperTest.mustReadSettingFile()
SettingHelperTest.mustNotReadSettingFile()
SettingHelperTest.mustPrintSettingTree()
SettingHelperTest.querySetting_withSuccess()
SettingHelperTest.mustHandleSettingValueInFallbackSettingTree()

StringHelperTest.mustFilterSetting()
StringHelperTest.prettyJson_withSucces()
StringHelperTest.prettyPython_withSucces()
StringHelperTest.filterJson_withSucces()
StringHelperTest.isLongString_withSuccess()

LogHelperTest.mustLogWithColors()
LogHelperTest.mustLogWithoutColors()
LogHelperTest.mustLogWithoutColorsAsWell()
LogHelperTest.mustLogEnvironmentSettings()
LogHelperTest.mustLogPretyPythonWithoutColors()
LogHelperTest.mustLogPretyPythonWithColors()
LogHelperTest.mustLogPretyJsonWithColors()
LogHelperTest.mustPrintMessageLog_withColors()

ObjectHelperTest.basicMethods()
ObjectHelperTest.mustAssertEquals()
ObjectHelperTest.mustIgnoreKeyCorrectly()

ReflectionHelperTest.isNotMethodInstance_withSuccess()
ReflectionHelperTest.overrideSignatures_withSuccess()
ReflectionHelperTest.getArgsOrder_withSuccess()

RandomHelperTest.sample_withSuccess()
RandomHelperTest.randomValues()

MethodAnnotationTest.Function_withSuccess()
MethodAnnotationTest.Method_withSuccess()
MethodAnnotationTest.FunctionThrough_withSuccess()

endTime = time.time()
print(f'endTime - startTime = {endTime - startTime}')
