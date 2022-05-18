from traceback import print_tb
from grep_info import get_station
from get_tickets import get_tickets
from Decrypt import decrypt
from texttable import Texttable
import os
import datetime
import time

def run(_fw, _tw):
    print("\n")
    station_name = get_station()
    fw = _fw
    fromwhere = station_name[fw]
    st = str(datetime.date.today() + datetime.timedelta(4))
    print('date: ',st, '\n')
    for tw in _tw:
        towhere = station_name[tw]
        startTime = st
        tickets = get_tickets(fromwhere, towhere, startTime)
        
        if(tickets):
            print(tw,":\n")
            for item in tickets:
                result = list(decrypt(item))
                new_dict = {v:k for k,v in station_name.items()}
                
                # print(result)
                # print(result[0])
                
                result[2] = new_dict[result[2]]
                result[3] = new_dict[result[3]]
                rightWidth = 8
                print('{0:{1}^9}'.format(result[1], chr(12288)),end = '')
                print('{0:{1}^9}'.format(result[2], chr(12288)),end = '')
                print('{0:{1}^9}'.format(result[3], chr(12288)),end = '')
                print('{0:{1}^9}'.format(result[4], chr(12288)),end = '')
                print('{0:{1}^9}'.format(result[5], chr(12288)),end = '')
                print(result[0].center(rightWidth,'-'),end = '')
                print('\n')
        else:
            print(tw, "无车次\n")
        time.sleep(1)


def query():
    _fwCity = "上海"
    f = open(r'citys.txt',encoding="utf-8")
    a = f.readline()
    _twCity = list(a.split(' '))
    # _twCity = ["南宁", "广州", "深圳", "长沙"]
    run(_fwCity,_twCity)

if __name__ == '__main__':
    query()
    os.system('pause')