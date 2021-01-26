from python_helper import SettingHelper, log, ObjectHelper, Function, Method, FunctionThrough, RandomHelper, Test

# LOG_HELPER_SETTINGS = {
#     log.LOG : True,
#     log.SUCCESS : True,
#     log.SETTING : True,
#     log.DEBUG : True,
#     log.WARNING : True,
#     log.WRAPPER : True,
#     log.FAILURE : True,
#     log.ERROR : True,
    # log.TEST : False
# }

LOG_HELPER_SETTINGS = {
    log.LOG : False,
    log.SUCCESS : False,
    log.SETTING : False,
    log.DEBUG : False,
    log.WARNING : False,
    log.WRAPPER : False,
    log.FAILURE : False,
    log.ERROR : False,
    log.TEST : False
}

@Test(environmentVariables={
    SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT,
    **LOG_HELPER_SETTINGS
})
def Function_withSuccess() :
    # Arrange
    TEST = RandomHelper.string(minimum=10)
    @Function
    def myFunction(something) :
        return TEST, something
    @Function
    def myOtherFunction(something) :
        raise Exception(TEST)
    SOMETHING = RandomHelper.string(minimum=10)
    exception = None

    # Act
    myRestult = myFunction(SOMETHING)
    myOtherResult = None
    try :
        myOtherResult = myOtherFunction(SOMETHING)
    except Exception as ext :
        exception = ext

    # Assert
    assert (TEST, SOMETHING) == myRestult
    assert ObjectHelper.isNone(myOtherResult)
    assert ObjectHelper.isNotNone(exception)
    assert f"myOtherFunction function error. Cause: {TEST}" == str(exception)

@Test(environmentVariables={
    SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT,
    **LOG_HELPER_SETTINGS
})
def Method_withSuccess() :
    # Arrange
    TEST = RandomHelper.string(minimum=10)
    class MyClass :
        @Method
        def myMethod(self,something) :
            return TEST, something
        @Method
        def myOtherMethod(self,something) :
            raise Exception(TEST)

    @Method
    def myNotMethod(self,something) :
        raise Exception(TEST)
    SOMETHING = RandomHelper.string(minimum=10)
    methodException = None
    notMethodEception = None
    myClass = MyClass()

    # Act
    myRestult = myClass.myMethod(SOMETHING)
    myOtherResult = None
    try :
        myOtherResult = myClass.myOtherMethod(SOMETHING)
    except Exception as ext :
        methodException = ext
    myNotMethodResult = None
    try :
        myNotMethodResult = myNotMethod(None,SOMETHING)
    except Exception as ext :
        notMethodEception = ext

    # Assert
    assert (TEST, SOMETHING) == myRestult
    assert ObjectHelper.isNone(myOtherResult)
    assert ObjectHelper.isNotNone(methodException)
    assert f"MyClass.myOtherMethod method error. Cause: {TEST}" == str(methodException)
    assert ObjectHelper.isNone(myNotMethodResult)
    assert ObjectHelper.isNotNone(notMethodEception)
    assert f"NoneType.myNotMethod method error. Cause: {TEST}" == str(notMethodEception)

@Test(environmentVariables={
    SettingHelper.ACTIVE_ENVIRONMENT : None,
    **LOG_HELPER_SETTINGS
})
def FunctionThrough_withSuccess() :
    # Arrange
    TEST = RandomHelper.string(minimum=10)
    @FunctionThrough
    def myFunction(something) :
        return TEST, something
    @FunctionThrough
    def myOtherFunction(something) :
        raise Exception(TEST)
    SOMETHING = RandomHelper.string(minimum=10)
    exception = None

    # Act
    myRestult = myFunction(SOMETHING)
    myOtherResult = None
    try :
        myOtherResult = myOtherFunction(SOMETHING)
    except Exception as ext :
        print(ext)
        exception = ext

    # Assert
    assert (TEST, SOMETHING) == myRestult
    assert ObjectHelper.isNone(myOtherResult)
    assert ObjectHelper.isNotNone(exception)
    assert TEST == str(exception)
