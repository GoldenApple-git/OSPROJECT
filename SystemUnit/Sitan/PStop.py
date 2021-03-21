from os import system
from time import sleep

class PStop:
    def __init__(self,time=-1):
        self.time = time

    def stop(self):
        sleep(int(self.time))
