from python_helper.api.src.domain import Constant as c
from python_helper.api.src.service import StringHelper, LogHelper, ReflectionHelper, EnvironmentHelper

def EnvironmentVariable(*outerArgs, environmentVariables=None, **outerKwargs) :
    def innerMethodWrapper(resourceInstanceMethod,*innerMethodArgs,**innerMethodKwargs) :
        def innerResourceInstanceMethod(*innerArgs,**innerKwargs) :
            originalEnvironmentVariables = {}
            if environmentVariables :
                for key,value in environmentVariables.items() :
                    originalEnvironmentVariables[key] = EnvironmentHelper.replaceEnvironmentVariable(key, value)
            LogHelper.loadSettings() 
            try :
                methodReturn = resourceInstanceMethod(*innerArgs,**innerKwargs)
            except Exception as exception :
                raise exception
            if environmentVariables :
                for key in environmentVariables.keys() :
                    if key in originalEnvironmentVariables :
                        EnvironmentHelper.setEnvironmentValue(key, originalEnvironmentVariables[key])
            return methodReturn
        ReflectionHelper.overrideSignatures(innerResourceInstanceMethod, resourceInstanceMethod)
        return innerResourceInstanceMethod
    return innerMethodWrapper
