"""
    parsingCsv python file
    Date: 19/02/2021
    Reading the BackTest-Market csv and convert him
    into regular csv : Date, Open, High, Low, Close, Volume
"""
import pandas as pd


def create_column(row):
    split_data = row.split(";")
    date = split_data[0] + " " + split_data[1]
    open = split_data[2]
    high = split_data[3]
    low = split_data[4]
    close = split_data[5]
    volume = split_data[6]
    return date, open, high, low, close, volume


def main():
    twtr = pd.read_csv("twtr-1m.csv")
    # Date, Open, High, Low, Close, Volume
    twtr['time'], twtr['open'], twtr['high'], twtr['low'], twtr['close'], twtr['volume'] = \
        zip(*twtr['data'].apply(create_column))
    twtr.drop(columns='data', inplace=True)  # drop the data column
    twtr['time'] = pd.to_datetime(twtr['time'])
    print(twtr)
    twtr.set_index('time', inplace=True)
    twtr.to_json("Twitter-1m.json", index=True)
    print("finish")


if __name__ == '__main__':
    main()
