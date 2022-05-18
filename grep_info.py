import requests
import re


#获取12306站点信息
def get_station():
    #@url : 12306网站站点信息
    #:return : station
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9230'
    requests.packages.urllib3.disable_warnings()
    response = requests.get(url, verify=False)
    pattern = u'([\u4e00-\u9fa5]+)\|([A-Z]+)'
    result = re.findall(pattern, response.text)

    station = dict(result)

    # file = open('station.txt','w',encoding='utf-8')
    # file.write(str(station))
    # file.close()
    return station

# if __name__ == '__main__':
#     get_station()
