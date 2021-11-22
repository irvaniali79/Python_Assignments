
import time
import datetime

class Date:

    def __init__(self,timestamp):
        self._timestamp=timestamp

    def __add__(self,date):
       return Date(abs(date.getTimeStamp()+self._timestamp))

    def __sub__(self,date):
       return Date(abs(date.getTimeStamp()-self._timestamp))

    def toDate(self):
        timestamp = datetime.datetime.fromtimestamp(self._timestamp)
        return timestamp.strftime('%m/%d/%Y %H:%M:%S %Z')

    def getTimeStamp(self):
        return self._timestamp

