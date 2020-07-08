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

def success(cls,message) :
    softLog(cls,message,c.SUCCESS)

def setting(cls,message) :
    softLog(cls,message,c.SETTING)

def debug(cls,message) :
    softLog(cls,message,c.DEBUG)

def warning(cls,message) :
    softLog(cls,message,c.WARNING)

def failure(cls,message,exception) :
    hardLog(cls,message,exception,c.FAILURE)

def wraper(cls,message,exception) :
    hardLog(cls,message,exception,c.WRAPPER)

def error(cls,message,exception) :
    hardLog(cls,message,exception,c.ERROR)
