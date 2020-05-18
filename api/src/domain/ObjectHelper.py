import StringHelper
import Constant as c

def equal(response,expectedResponse) :
    filteredResponse = StringHelper.filterJson(response)
    filteredExpectedResponse = StringHelper.filterJson(expectedResponse)
    return filteredResponse == filteredExpectedResponse

def filterIgnoreKeyList(objectAsString,ignoreKeyList,globals):
    if objectAsString and ignoreKeyList :
        splitedObjectAsStringList = objectAsString.split(c.NEW_LINE)
        newStringList = []
        for line in splitedObjectAsStringList :
            appendLine = True
            for key in ignoreKeyList :
                if key.strip() == StringHelper.getFilteredString(line.split(c.COLON)[0].strip(),globals) :
                    appendLine = False
            if appendLine :
                newStringList.append(line)
        return c.NEW_LINE.join(newStringList)
    return objectAsString
