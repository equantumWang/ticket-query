import re

def decrypt(string):
    reg = re.compile('.*?\|(.*?)\|.*?\|(.*?)\|.*?\|.*?\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|.*')

    result = re.findall(reg, string)[0]
    # print(result)
    return result
