import os
import time
import config
import errno
import colorama

def expire_files():
    '''
    FILE CLEANUP ROUTINE
    
    This function will run on a schedule set by FILE_CLEANUP SCHEDULE
    in config.py. 
    
    Running this function will delete all files that have expired as
    determined by EXPIRE_TIME in config.py
    '''

    colorama.init()
    green = colorama.Fore.GREEN
    yellow = colorama.Fore.YELLOW
    red = colorama.Fore.RED
    reset = colorama.Fore.RESET

    print(green + " -- FILE CLEANUP STARTED -- " + reset)
    for root, dirs, files in os.walk(config.UPLOAD_DIR):
        for name in files:
            file_time = os.path.getmtime(os.path.join(root, name)) 
            expire_time = file_time + config.EXPIRE_TIME * 60 * 60 
            current_time = time.time()
            if current_time > expire_time:
                os.remove(os.path.join(root, name))
                print(red + "removed: " + os.path.join(root, name) + reset)
        for name in dirs:
            try:
                os.rmdir(os.path.join(root, name))
                print(red + "Removed: " + os.path.join(root, name) + reset)       
            except OSError as e:
                if e.errno == errno.ENOTEMPTY:
                    print(yellow + os.path.join(root, name) + " is not empty" + reset)
    print(green + " -- FILE CLEANUP COMPLETED -- " + reset)

 
