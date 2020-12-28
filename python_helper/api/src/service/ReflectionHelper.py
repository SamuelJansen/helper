from python_helper.api.src.domain  import Constant as c
from python_helper.api.src.service import LogHelper, ObjectHelper, StringHelper

MAXIMUN_ARGUMENTS = 20

def getAttributeOrMethod(instance, name) :
    attributeOrMethodInstance = None
    try :
        attributeOrMethodInstance = None if ObjectHelper.isNone(instance) or ObjectHelper.isNone(name) else getattr(instance, name)
    except Exception as exception :
        LogHelper.warning(getAttributeOrMethod, f'Not possible to get "{name}" from "{instance.__class__.__name__ if ObjectHelper.isNotNone(instance) else instance}" instance')
    return attributeOrMethodInstance

def getAttributeAndMethodNameList(instanceClass) :
    objectNullArgsInstance = instanciateItWithNoArgsConstructor(instanceClass)
    return [
        attributeOrMethodName
        for attributeOrMethodName in dir(objectNullArgsInstance)
        if isNotPrivate(attributeOrMethodName)
    ]

def getAttributeNameList(instanceClass) :
    objectNullArgsInstance = instanciateItWithNoArgsConstructor(instanceClass)
    return [
        attributeName
        for attributeName in dir(objectNullArgsInstance)
        if isNotPrivate(attributeName) and isNotMethod(objectNullArgsInstance, attributeName)
    ]

def getMethodNameList(instanceClass) :
    objectNullArgsInstance = instanciateItWithNoArgsConstructor(instanceClass)
    return [
        methodName
        for methodName in dir(objectNullArgsInstance)
        if isNotPrivate(methodName) and isMethod(objectNullArgsInstance, methodName)
    ]

def isMethodInstance(methodInstance) :
    return methodInstance.__class__.__name__ in [
        'method',
        'builtin_function_or_method'
    ] if ObjectHelper.isNotNone(methodInstance) and ObjectHelper.isNotNone(methodInstance.__class__) else False

def isNotMethodInstance(methodInstance) :
    return not isMethodInstance(methodInstance)

def isMethod(objectInstance, name) :
    if ObjectHelper.isNone(objectInstance) or StringHelper.isBlank(name) :
        return False
    return isMethodInstance(getAttributeOrMethod(objectInstance, name))

def isNotMethod(objectInstance, name) :
    if ObjectHelper.isNone(objectInstance) or StringHelper.isBlank(name) :
        return False
    return isNotMethodInstance(getAttributeOrMethod(objectInstance, name))

def instanciateItWithNoArgsConstructor(instanceClass) :
    args = []
    objectInstance = None
    for _ in range(MAXIMUN_ARGUMENTS) :
        try :
            objectInstance = instanceClass(*args)
            break
        except :
            args.append(None)
    if not isinstance(objectInstance, instanceClass) :
        raise Exception(f'Not possible to instanciate {instanceClass} class in instanciateItWithNoArgsConstructor() method with None as args constructor')
    return objectInstance

def isNotPrivate(attributeOrMethodName) :
    return StringHelper.isNotBlank(attributeOrMethodName) and (
        not attributeOrMethodName.startswith(f'{2 * c.UNDERSCORE}') and
        not attributeOrMethodName.startswith(c.UNDERSCORE) and
        not ObjectHelper.METADATA_NAME == attributeOrMethodName
    )

def getAttributePointerList(instance) :
    return [
        getattr(instance, instanceAttributeName)
        for instanceAttributeName in dir(instance)
        if (not instanceAttributeName.startswith('__') and not instanceAttributeName.startswith('_'))
    ]

def getAttributeDataList(instance) :
    return [
        (getattr(instance, instanceAttributeName), instanceAttributeName)
        for instanceAttributeName in dir(instance)
        if (not instanceAttributeName.startswith('__') and not instanceAttributeName.startswith('_'))
    ]

def setAttributeOrMethod(instance, attributeOrMethodName, attributeOrMethodInstance) :
    setattr(instance, attributeOrMethodName, attributeOrMethodInstance)

def overrideSignatures(toOverride, original) :
    try :
        toOverride.__name__ = original.__name__
        toOverride.__module__ = original.__module__
        toOverride.__qualname__ = original.__qualname__
    except Exception as exception :
        LogHelper.error(overrideSignatures,f'''failed to override signatures of {toOverride} by signatures of {original} method''',exception)

def printDetails(toDetail):
    print(f'{2 * c.TAB}printDetails({toDetail}):')
    try :
        print(f'{2 * c.TAB}type({toDetail}).__name__ = {type(toDetail).__name__}')
    except :
        pass
    try :
        print(f'{2 * c.TAB}type({toDetail}).__class__ = {type(toDetail).__class__}')
    except :
        pass
    try :
        print(f'{2 * c.TAB}type({toDetail}).__class__.__module__ = {type(toDetail).__class__.__module__}')
    except :
        pass
    try :
        print(f'{2 * c.TAB}type({toDetail}).__class__.__name__ = {type(toDetail).__class__.__name__}')
    except :
        pass
    try :
        print(f'{2 * c.TAB}{toDetail}.__class__.__name__ = {toDetail.__class__.__name__}')
    except :
        pass
    try :
        print(f'{2 * c.TAB}{toDetail}.__class__.__module__ = {toDetail.__class__.__module__}')
    except :
        pass
    try :
        print(f'{2 * c.TAB}{toDetail}.__class__.__qualname__ = {toDetail.__class__.__qualname__}')
    except :
        pass

def printClass(instanceClass) :
    print(f'{2 * c.TAB}printClass({instanceClass}):')
    try :
        print(f'{2 * c.TAB}{instanceClass}.__name__ = {instanceClass.__name__}')
    except :
        pass
    try :
        print(f'{2 * c.TAB}{instanceClass}.__module__ = {instanceClass.__module__}')
    except :
        pass
    try :
        print(f'{2 * c.TAB}{instanceClass}.__qualname__ = {instanceClass.__qualname__}')
    except :
        pass
