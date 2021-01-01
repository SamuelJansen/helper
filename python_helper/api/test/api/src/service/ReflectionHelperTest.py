from python_helper import ObjectHelper, StringHelper, SettingHelper, Constant, log, EnvironmentVariable, ReflectionHelper

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
    **LOG_HELPER_SETTINGS
})
def isNotMethodInstance_withSuccess() :
    # Arrange
    class MyObject:
        def __init__(self, myAttribute) :
            self.myAttribute = myAttribute
        def myMethod(self):
            return self.myAttribute
    myObject = ReflectionHelper.instanciateItWithNoArgsConstructor(MyObject)
    MY_ATTRIBUTE_NAME = 'myAttribute'
    MY_METHOD_NAME = 'myMethod'
    MY_NOT_EXISTING_ATTRIBUTE_OR_METHOD_NAME = 'myNotExistingMethodOrAtrributeName'

    # Act
    attributeOrMethodNameList = ReflectionHelper.getAttributeAndMethodNameList(myObject.__class__)
    attributeNameList = ReflectionHelper.getAttributeNameList(myObject.__class__)
    methodNameList = ReflectionHelper.getMethodNameList(myObject.__class__)
    myAttribute = getattr(myObject, MY_ATTRIBUTE_NAME)
    myMethod = getattr(myObject, 'myMethod')

    # Assert
    assert [MY_ATTRIBUTE_NAME, MY_METHOD_NAME] == attributeOrMethodNameList
    assert [MY_ATTRIBUTE_NAME] == attributeNameList
    assert [MY_METHOD_NAME] == methodNameList
    assert ReflectionHelper.isNotMethodInstance(myAttribute)
    assert not ReflectionHelper.isNotMethodInstance(myMethod)
    assert ReflectionHelper.isNotMethodInstance(ReflectionHelper.getAttributeOrMethod(myObject, MY_NOT_EXISTING_ATTRIBUTE_OR_METHOD_NAME))

    assert ReflectionHelper.isNotMethod(myObject, MY_ATTRIBUTE_NAME)
    assert not ReflectionHelper.isNotMethod(myObject, MY_METHOD_NAME)
    assert ReflectionHelper.isNotMethod(myObject, MY_NOT_EXISTING_ATTRIBUTE_OR_METHOD_NAME)

    assert ReflectionHelper.isMethodInstance(myMethod)
    assert not ReflectionHelper.isMethodInstance(myAttribute)
    assert not ReflectionHelper.isMethodInstance(ReflectionHelper.getAttributeOrMethod(myObject, MY_NOT_EXISTING_ATTRIBUTE_OR_METHOD_NAME))

    assert not ReflectionHelper.isMethod(myObject, MY_ATTRIBUTE_NAME)
    assert ReflectionHelper.isMethod(myObject, MY_METHOD_NAME)
    assert not ReflectionHelper.isMethod(myObject, MY_NOT_EXISTING_ATTRIBUTE_OR_METHOD_NAME)

@EnvironmentVariable(environmentVariables={
    SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT,
    **LOG_HELPER_SETTINGS
})
def overrideSignatures_withSuccess() :
    # Arrange
    class MyObject:
        def myMethod(self, something):
            return something

    def myWrapper(myFunction,*wrapperAgrs,**wrapperKwargs):
        def myInBetweenWrapperFunction(*agrs,**kwargs) :
            return myFunction(*agrs,**kwargs)
        ReflectionHelper.overrideSignatures(myInBetweenWrapperFunction, myFunction)
        return myInBetweenWrapperFunction

    def myWrapperWithoutOverride(myFunction,*wrapperAgrs,**wrapperKwargs):
        def myInBetweenWrapperFunction(*agrs,**kwargs) :
            return myFunction(*agrs,**kwargs)
        return myInBetweenWrapperFunction

    OVERRIDED = '__overrided'
    NOT_OVERRIDED = '__not_overrided'

    @myWrapper
    def myOverridedFunction(arg) :
        return f'{arg}{OVERRIDED}'

    @myWrapperWithoutOverride
    def myNotOverridedFunction(arg) :
        return f'{arg}{NOT_OVERRIDED}'

    ABCD = 'abcd'
    exception = None

    # Act
    myObject = ReflectionHelper.instanciateItWithNoArgsConstructor(MyObject)
    setattr(myObject, myOverridedFunction.__name__, myOverridedFunction)
    setattr(myObject, myNotOverridedFunction.__name__, myNotOverridedFunction)
    try :
        myObject.myNotOverridedFunction('any arg')
    except Exception as e :
        exception = e

    # Assert
    assert myObject.myMethod(True)
    assert not myObject.myMethod(False)
    assert ObjectHelper.isNotNone(myOverridedFunction(True))
    assert ObjectHelper.isNotNone(myOverridedFunction(False))
    assert ObjectHelper.isNotNone(myOverridedFunction(ABCD))
    assert ObjectHelper.isNotNone(myNotOverridedFunction(True))
    assert ObjectHelper.isNotNone(myNotOverridedFunction(False))
    assert ObjectHelper.isNotNone(myNotOverridedFunction(ABCD))
    assert ObjectHelper.isNotNone(myObject.myOverridedFunction(True))
    assert ObjectHelper.isNotNone(myObject.myOverridedFunction(False))
    assert ObjectHelper.isNotNone(myObject.myOverridedFunction(ABCD))
    assert myOverridedFunction(True) == myObject.myOverridedFunction(True)
    assert myOverridedFunction(False) == myObject.myOverridedFunction(False)
    assert myOverridedFunction(ABCD) == myObject.myOverridedFunction(ABCD)
    assert f'{True}{OVERRIDED}' == myObject.myOverridedFunction(True)
    assert f'{False}{OVERRIDED}' == myObject.myOverridedFunction(False)
    assert f'{ABCD}{OVERRIDED}' == myObject.myOverridedFunction(ABCD)
    assert ObjectHelper.isNotNone(exception)
    assert "'MyObject' object has no attribute 'myNotOverridedFunction'" == str(exception)
    assert ObjectHelper.isNotNone(myObject.myInBetweenWrapperFunction(True))
    assert ObjectHelper.isNotNone(myObject.myInBetweenWrapperFunction(False))
    assert ObjectHelper.isNotNone(myObject.myInBetweenWrapperFunction(ABCD))
    assert myNotOverridedFunction(True) == myObject.myInBetweenWrapperFunction(True)
    assert myNotOverridedFunction(False) == myObject.myInBetweenWrapperFunction(False)
    assert myNotOverridedFunction(ABCD) == myObject.myInBetweenWrapperFunction(ABCD)
    assert f'{True}{NOT_OVERRIDED}' == myObject.myInBetweenWrapperFunction(True)
    assert f'{False}{NOT_OVERRIDED}' == myObject.myInBetweenWrapperFunction(False)
    assert f'{ABCD}{NOT_OVERRIDED}' == myObject.myInBetweenWrapperFunction(ABCD)

@EnvironmentVariable(environmentVariables={
    SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT,
    **LOG_HELPER_SETTINGS
})
def getArgsOrder_withSuccess() :
    # Arrange
    class MyClass :
        def __init__(
            self,
            attributeValue,
            otherAttributeValue,
            otherAttributeValueAgain,
            someOtherAttributeValue,
            otherAttributeValueOnceAgain
        ):
            self.attributeKey = attributeValue
            self.otherAttributeKey = otherAttributeValue
            self.otherAttributeKeyAgain = otherAttributeValueAgain
            self.someOtherAttributeKey = someOtherAttributeValue
            self.otherAttributeKeyOnceAgain = otherAttributeValueOnceAgain
    class MyClassWithoutAttributes :
        def __init__(self):
            ...
    class MyClassWithMoreAttributesThanArgs :
        def __init__(self,attributeValue):
            self.attributeKey = attributeValue
            self.otherAttributeKey = None
            self.otherAttributeKeyAgain = None
            self.someOtherAttributeKey = None
            self.otherAttributeKeyOnceAgain = None
    class MyClassWithLessAttributesThanArgs :
        def __init__(
            self,
            attributeValue,
            otherAttributeValue,
            otherAttributeValueAgain,
            someOtherAttributeValue,
            otherAttributeValueOnceAgain
        ):
            self.attributeKey = attributeValue
    class MyClassWithoutInitMethod :
        attributeKey = None
        otherAttributeKey = None
        otherAttributeKeyAgain = None
        someOtherAttributeKey = None
        otherAttributeKeyOnceAgain = None

    # Act
    myClassArgsOrder = ReflectionHelper.getArgsOrder(MyClass)
    myClassWithoutAttributesArgsOrder = ReflectionHelper.getArgsOrder(MyClassWithoutAttributes)
    myClassWithMoreAttributesThanArgsArgsOrder = ReflectionHelper.getArgsOrder(MyClassWithMoreAttributesThanArgs)
    myClassWithLessAttributesThanArgsArgsOrder = ReflectionHelper.getArgsOrder(MyClassWithLessAttributesThanArgs)
    myClassWithoutInitMethodArgsOrder = ReflectionHelper.getArgsOrder(MyClassWithoutInitMethod)

    # Assert
    assert [
        'attributeKey',
        'otherAttributeKey',
        'otherAttributeKeyAgain',
        'someOtherAttributeKey',
        'otherAttributeKeyOnceAgain'
    ] == myClassArgsOrder
    assert [] == myClassWithoutAttributesArgsOrder
    assert [
        'attributeKey'
    ] == myClassWithLessAttributesThanArgsArgsOrder
    assert [
        'attributeKey'
    ] == myClassWithMoreAttributesThanArgsArgsOrder
    assert [] == myClassWithoutInitMethodArgsOrder
