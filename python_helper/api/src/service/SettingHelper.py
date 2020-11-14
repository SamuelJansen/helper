from python_helper.api.src.service import StringHelper
from python_helper.api.src.domain import Constant

def getFilteredSetting(setting,globals) :
    if Constant.STRING == setting.__class__.__name__ :
        return StringHelper.getFilteredString(setting,globals)
    return setting

def getSetting(nodeKey,settingTree) :
    try :
        return accessTree(nodeKey,settingTree)
    except Exception as exception :
        log.debug(getSetting,f'Not possible to get {nodeKey} node key. Cause: {str(exception)}')
        return None

def accessTree(nodeKey,tree) :
    if nodeKey == Constant.NOTHING :
        try :
            return StringHelper.filterString(tree)
        except :
            return tree
    else :
        nodeKeyList = nodeKey.split(Constant.DOT)
        lenNodeKeyList = len(nodeKeyList)
        if lenNodeKeyList > 0 and lenNodeKeyList == 1 :
             nextNodeKey = Constant.NOTHING
        else :
            nextNodeKey = Constant.DOT.join(nodeKeyList[1:])
        return accessTree(nextNodeKey,tree[nodeKeyList[0]])
