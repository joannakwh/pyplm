import key
import requests
from lxml import html

"""Makes url requet and return a byte tree

"""
def makeRequest(year, make, model):
    url = 'http://www.plussizingguide.com/cgi-bin/ultimate_guide_online.cgi'
    params = {'host': 'HTTP_HOST', 'userName': 'cariboo',
              'password': key.password, 'licenseKey': key.licenseKey}
    if (year is not None and len(year) != 0):
        params.update({'selectYear': year})
    if (year is not None and len(year) != 0):
        params.update({'selectMake': make})
    if (year is not None and len(year) != 0):
        params.update({'selectModel': model})
    result = requests.post(url, data=params)
    tree = html.fromstring(result.content)      # use page.content rather than page.text because html.fromstring implicitly expects bytes as input
    return tree

"""Makes request and returns years

"""
def getYears():
    tree = makeRequest(None, None, None)
    years = tree.xpath('//select[@name="selectYear"]/option/text()')     # traverse raw html output to select specific tags to get year string
    years.pop(0)    # remove 'Select Year' option
    return years

"""Makes request and returns makes
Parameters: year    
"""
def getMakes(year):
    tree = makeRequest(str(year), None, None)
    makes = tree.xpath('//select[@name="selectMake"]/option/text()')
    makes.pop(0)
    return makes

"""Makes request and returns models
Parameters: year, make    
"""
def getModels(year, make):
    tree = makeRequest(str(year), str(make), None)
    models = tree.xpath('//select[@name="selectModel"]/option/text()')
    models.pop(0)
    return models

"""Makes request and returns car info as dictionary pairs
Parameters: year, make model    
"""
def getInfo(year, make, model):
    info = {}
    tree = makeRequest(str(year), str(make), str(model))
    fields = tree.xpath('//input/@name')
    for field in fields:
        values = tree.xpath('//input[@name="' + field + '"]/@value')
        for value in values: 
            info[field] = value
    return info