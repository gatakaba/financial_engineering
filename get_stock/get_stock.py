# coding:utf-8
import os
import time
import urllib

import datetime as dt


def get_csv(day, code):
    url = "http://k-db.com/stocks/{0}/minutely?date={1}&download=csv".format(
        code, day)
    # make folder
    if not os.path.exists("minutely"):
        os.mkdir("minutely")
    if not os.path.exists("minutely/" + code):
        os.mkdir("minutely/" + code)
    # download csv
    urllib.urlretrieve(url, "minutely/" + code + "/" + day + ".csv")
    print "download:" + url
    # wait
    time.sleep(1)


def get_data(day, code=None):
    if code is None:
        # download all code
        with open("code_list") as f:
            code_list = f.read()
        code_list = code_list.split("\n")
        for code in code_list:
            get_csv(day, code)
    else:
        get_csv(day, code)


if __name__ == "__main__":
    # get data for all stocks of up to 100 days before
    prev_day = 10
    for i in range(prev_day):
        day = str((dt.datetime.now() - dt.timedelta(days=i)).date())
        get_data(day)
