from datetime import datetime

timestamp = [1571647115, 1571647881, 1571648733, 1571651845, 1571652671]

for unix_time in timestamp:
        human_readable = datetime.utcfromtimestamp(unix_time).strftime('%Y-%m-%d %H:%M:%S')
        print (f"The human readable form of {unix_time} is {human_readable}")

def convert_utime():
    with open("unixtimestamp.txt", "r+") as line:
        utime = line.read()
        for unix_time in utime.split('\n'):
                humanreadable = datetime.utcfromtimestamp(int(unix_time)).strftime('%Y-%m-%d %H:%M:%S')
                print(f'The human readable form of {unix_time} is {humanreadable}')
convert_utime()