#!/usr/bin/env python3
import ntplib
import sched
import timeit
from threading import Timer
import datetime

class ThreadedTimer:
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval #Interval in seconds
        self.function   = function #Function to execute
        self.args       = args #Arguments for the function
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

class Clock:
    def get_time(self):
        if self.address != '':
            try:
                start = int(datetime.datetime.now().timestamp()*1000)
                response = self.client.request(self.address)
                end = int(datetime.datetime.now().timestamp()*1000)

                trip_time = (end - start)/2
                # print(trip_time)
                self.server_time = int(response.tx_time*1000 + trip_time)
                self.system_time = int(datetime.datetime.now().timestamp()*1000)
                self.last_synced = self.system_time
            except:
                print('Could not sync with time server.')
        else:
            self.server_time = int(datetime.datetime.now().timestamp()*1000)
            self.system_time = int(datetime.datetime.now().timestamp()*1000)

    def __init__(self, server='', interval=30):
        self.client = ntplib.NTPClient()
        self.address = server
        self.server_time = int(datetime.datetime.now().timestamp()*1000)
        self.system_time = int(datetime.datetime.now().timestamp()*1000)
        self.last_synced = 0
        self.get_time()
        self.sync_thread = ThreadedTimer(interval, self.get_time)

    def stop(self):
        self.sync_thread.stop()

    def time_ms(self):
        return int(self.server_time + (int(datetime.datetime.now().timestamp()*1000) - self.system_time))
