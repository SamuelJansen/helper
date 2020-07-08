from python_helper.api.src.domain import Constant as c

def softLog(cls,message,level) :
    if not cls or cls == c.NOTHING :
        classPortion = c.NOTHING
    else :
        classPortion = f'{cls.__name__}{c.COLON_SPACE}'
    print(f'{level}{classPortion}{message}')

def hardLog(cls,message,exception,level) :
    if not cls or cls == c.NOTHING :
        classPortion = c.NOTHING
    else :
        classPortion = f'{cls.__name__}{c.COLON_SPACE}'
    if not exception or exception == c.NOTHING :
        errorPortion = c.NOTHING
    else :
        errorPortion = f'{c.DOT_SPACE}{c.LOG_CAUSE}{str(exception)}'
    print(f'{level}{classPortion}{message}{errorPortion}')

def logSuccess(cls,message) :
    softLog(cls,message,c.SUCCESS)

def logSetting(cls,message) :
    softLog(cls,message,c.SETTING)

def logDebug(cls,message) :
    softLog(cls,message,c.DEBUG)

def logWarning(cls,message) :
    softLog(cls,message,c.WARNING)

def logFailure(cls,message,exception) :
    hardLog(cls,message,exception,c.FAILURE)

def logWraper(cls,message,exception) :
    hardLog(cls,message,exception,c.WRAPPER)

def logError(cls,message,exception) :
    hardLog(cls,message,exception,c.ERROR)
