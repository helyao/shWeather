# -*- coding: utf-8 -*-
import datetime

# Get current timestamp
def GetDateStamp():
    datestamp = datetime.datetime.now().strftime("%Y-%m-%d")
    return datestamp