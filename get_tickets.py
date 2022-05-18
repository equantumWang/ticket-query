from pickle import FALSE
import requests
import json
from urllib.parse import urlencode

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'Cookie': '_uab_collina=165242486400829515997504; JSESSIONID=9FACAEEDBA4BFA8D49A14497BD0F98D6; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; _jc_save_fromStation=%u4E0A%u6D77%2CSHH; _jc_save_wfdc_flag=dc; BIGipServerpassport=1005060362.50215.0000; RAIL_EXPIRATION=1653080567753; RAIL_DEVICEID=RI4IBB9gtLYCHolegXMdu0AU1m2nCxyUxFEZMGzvxXHsctIctb5as5LFhMUqPtFiKP09v-SNf55XJdPkMojSO_kixbaUR3TXAk2T6ffpzZGxHbtixBsNayRCbIbmayLrX_yzkpzCcN_grKIGtmO720jm2C9HsY2t; route=c5c62a339e7744272a54643b3be5bf64; _jc_save_toDate=2022-05-17; _jc_save_fromDate=2022-05-21; BIGipServerotn=2731999498.64545.0000; _jc_save_toStation=%u8862%u5DDE%2CQEH; current_captcha_type=C'
}

def get_tickets(fromWhere, toWhere, startTime):
    #@fromWhere : 出发地
    #@toWhere : 目的地
    #@startTime : 出发时间

    data = {
        'leftTicketDTO.train_date': startTime,
        'leftTicketDTO.from_station': fromWhere,
        'leftTicketDTO.to_station': toWhere,
        'purpose_codes': 'ADULT'
    }



    request_url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date='+startTime+'&leftTicketDTO.from_station='+fromWhere+'&leftTicketDTO.to_station='+toWhere+'&purpose_codes=ADULT'
    requests.packages.urllib3.disable_warnings()
    text = requests.get(request_url, headers=headers).text
    # file = open('result.txt','w',encoding='utf-8')
    # file.write(str(text))
    # file.close()
    response = json.loads(text,strict = False)
    result = response['data']['result']

    return result

# if __name__ == '__main__':
#     get_tickets('SHH', 'HZH','2022-05-21')
