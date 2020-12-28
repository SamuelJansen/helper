import os, sys, json
from python_helper.api.src.service import StringHelper, LogHelper
from python_helper.api.src.domain import Constant as c

OS = os
SYS = sys
OS_SEPARATOR = OS.path.sep

clear = lambda: OS.system('cls')

def getEnvironmentValue(environmentKey, default=None) :
    environmentValue = OS.environ.get(environmentKey) if not environmentKey is None else default
    return environmentValue if not environmentValue is None else default

def setEnvironmentValue(environmentKey, environmentValue, default=None):
    if not environmentKey is None :
        if not environmentValue is None :
            OS.environ[environmentKey] = str(StringHelper.filterString(environmentValue))
        elif not default is None :
            OS.environ[environmentKey] = str(StringHelper.filterString(default))
        else :
            deleteEnvironmentValue(environmentKey)
    else :
        LogHelper.debug(setEnvironmentValue, f'arguments: environmentKey: {environmentKey}, environmentValue: {environmentValue}, default: {default}')
        raise Exception(f'Environment key cannot be {environmentKey}')

def replaceEnvironmentVariable(environmentKey, environmentValue, default=None) :
    originalEnvironmentValue = getEnvironmentValue(environmentKey, default=default)
    setEnvironmentValue(environmentKey, environmentValue, default=default)
    return originalEnvironmentValue

def deleteEnvironmentValue(environmentKey) :
    if not environmentKey is None :
        OS.environ.pop(environmentKey)

def getActiveEnvironmentVariableSet() :
    try :
        return json.loads(str(OS.environ)[8:-1].replace(c.DOUBLE_QUOTE, c.BACK_SLASH_DOUBLE_QUOTE).replace(c.SINGLE_QUOTE, c.DOUBLE_QUOTE))
    except Exception as exception :
        LogHelper.error(getActiveEnvironmentVariableSet, 'Not possible to load os.environ as a json. Returning os.environ as string by default', exception)
        return str(OS.environ)[8:-1]

def listDirectoryContent() :
    return OS.listdir(apisPath)

def appendPath(path) :
    SYS.path.append(path)

def getCurrentSoutStatus() :
    return SYS.stdout, SYS.stderr

def overrideSoutStatus(stdout, stderr) :
    SYS.stdout = stdout
    SYS.stderr = stderr
