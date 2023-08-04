from python_helper.api.src.domain import Constant as c
from python_helper.api.src.service import SettingHelper


class SettingsManager:

    def __init__(self,
        settingFilePath,
        settingTree = None,
        fallbackSettingFilePath = None,
        fallbackSettingTree = None,
        lazyLoad = False,
        keepDepthInLongString = False,
        depthStep = c.TAB_UNITS,
        encoding = c.ENCODING
    ):
        self.settingFilePath = settingFilePath
        self.settingTree = settingTree
        self.fallbackSettingFilePath = fallbackSettingFilePath
        self.fallbackSettingTree = fallbackSettingTree
        self.lazyLoad = lazyLoad
        self.keepDepthInLongString = keepDepthInLongString
        self.depthStep = depthStep
        self.encoding = encoding
    

    def load(self):
        self.settingsTree = SettingHelper.getSettingTree(
            self.settingFilePath,
            settingTree = self.settingTree,
            fallbackSettingFilePath = self.fallbackSettingFilePath,
            fallbackSettingTree = self.fallbackSettingTree,
            lazyLoad = self.lazyLoad,
            keepDepthInLongString = self.keepDepthInLongString,
            depthStep = self.depthStep,
            encoding = self.encoding
        )
        return self.settingsTree
    

    def get(self, nodeKey):
        return SettingHelper.getSetting(nodeKey, self.settingsTree)
    
    def query(self, keywordQuery):
        return SettingHelper.querySetting(keywordQuery, self.settingTree)
    
    def update(self, newSettingsTreeValues):
        return SettingHelper.updateSettingTree(self.settingsTree, newSettingsTreeValues)
    

    def display(self, tree, name, depth=1, withColors=False):
        return SettingHelper.printSettings(tree, name, depth=depth, withColors=withColors)