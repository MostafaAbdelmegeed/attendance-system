import datetime


class Timer:

    def __init__(self, time_in_ms):
        self.initial_time = datetime.datetime.now()
        self.seconds = time_in_ms


    def isTimeUp(self):
        if datetime.datetime.now() >= (self.initial_time + self.seconds):
            return True
        else:
            return False
