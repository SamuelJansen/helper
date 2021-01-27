from python_helper import TestHelper
TestHelper.run(__file__, inspectGlobals=False)
TestHelper.run(
    __file__,
    times = 2,
    testStatus = False,
    logStatus = True,
    logResult = True,
    inspectGlobals = True
)
TestHelper.run(
    __file__,
    times = 10,
    runOnly = [
        'LogHelperTest.mustLogPretyPythonWithColors',
        'LogHelperTest.mustLogPretyJsonWithColors'
        ],
    testStatus = False,
    logStatus = False,
    logResult = False,
    inspectGlobals = False
)
# TestHelper.run(
#     __file__,
#     times = 1,
#     runOnly = [
#         'ModuleImportsTest.allImportedSuccesfuly'
#     ],
#     testStatus = False,
#     logStatus = False,
#     logResult = False,
#     inspectGlobals = False
# )
# TestHelper.run(
#     __file__,
#     times = 1,
#     runOnly = [
#         'MethodAnnotationTest.Function_withSuccess'
#         ],
#     testStatus = False,
#     logStatus = False,
#     logResult = False,
#     inspectGlobals = False
# )
# TestHelper.run(
#     __file__,
#     times = 1,
#     runOnly = [
#         'LogHelperTest.mustLogWithColors'
#         ],
#     testStatus = False,
#     logStatus = False,
#     logResult = False,
#     inspectGlobals = True
# )
