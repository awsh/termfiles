import os
import time


def expire_files():
    # need to recursively travel upload dir and compare file time to current time

    file_time = os.path.getmtime(file) 
    file_time_plus_24_hours = file_time * config.EXPIRE_TIME * 60 * 60
    current_time = time.time()
