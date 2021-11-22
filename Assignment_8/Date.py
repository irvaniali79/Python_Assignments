
import time

class Date:

    def __init__(self,timestamp):
        self._timestamp=timestamp

    def __add__(self,date):
       return Date(abs(date.getTimeStamp()+self._timestamp))

    def __sub__(self,date):
       return Date(abs(date.getTimeStamp()-self._timestamp))

    def toDate(self):
        return

    def getTimeStamp(self):
        return self._timestamp