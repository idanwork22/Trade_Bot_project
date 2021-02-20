from datetime import datetime, timedelta
import pandas as pd
import requests
import json
import math


def main():
    check = pd.read_csv("Twitter-1m.csv", parse_dates=['time'])
    mask = check["time"] > pd.datetime(2013,1,1)
    check = check[mask]
    check.set_index(['time'],inplace=True)
    list_of_candles = []

    a = check.iterrows()
    b = next(a)
    time = b[0]
    check_datetime_time = pd.to_datetime(time)
    check_datetime_time = datetime(check_datetime_time.year, check_datetime_time.month, check_datetime_time.day,
                                   check_datetime_time.hour, check_datetime_time.minute)
    #check_minute = check_datetime_time.minute
    check_day = check_datetime_time.day
    for candle in a:
        obj = candle[1]
        time = candle[0]
        open = obj[0]
        high = obj[1]
        low = obj[2]
        close = obj[3]
        volume = obj[4]
        datetime_time = pd.to_datetime(time)
        datetime_time = datetime(datetime_time.year, datetime_time.month, datetime_time.day,
                                 datetime_time.hour, datetime_time.minute)
        if  datetime_time.day <= 12 :
            datetime_time = datetime_time.replace(month=datetime_time.day, day=datetime_time.month)
        #print(datetime_time)
        print(datetime_time)
        datetime_time = str(datetime_time)
        # print(datetime_time)
        document = {
            'time': datetime_time,
            'open': open,
            'high': high,
            'low': low,
            'close': close,
            'volume': volume
        }
        list_of_candles.append(document)
    list_of_candles_len = len(list_of_candles)
    for i in range(0, list_of_candles_len, 1000):
        start = i
        end = i + 1000
        if end >= list_of_candles_len:
            end = list_of_candles_len
        a = requests.post('http://127.0.0.1:5000/historical_data?stockname=twtr',
                          data=json.dumps(list_of_candles[start:end]),
                          headers={'stockname': 'TWTR'})

    '''for candle in list_of_candles:
        a = requests.post('http://127.0.0.1:5000/historical_data?stockname=twtr', data=json.dumps([candle]), headers={'stockname': 'TWTR'})
        print(a.text)'''


if __name__ == '__main__':
    main()
