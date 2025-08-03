import time

def Scan_Time(last_time):
    read_time = time.time()
    cycle_time = round((read_time - last_time)*1000, 2)
    last_time = read_time

    return cycle_time, last_time