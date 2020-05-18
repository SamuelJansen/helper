import StringHelper

def getFilteredSetting(setting,globals) :
    if globals.STRING == setting.__class__.__name__ :
        return StringHelper.getFilteredString(setting,globals)
    return setting
