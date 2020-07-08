from helper.api.src.service import StringHelper
from helper.api.src.domain import Constant

def getFilteredSetting(setting,globals) :
    if Constant.STRING == setting.__class__.__name__ :
        return StringHelper.getFilteredString(setting,globals)
    return setting
