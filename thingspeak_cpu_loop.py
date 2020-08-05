from time import localtime, strftime

# download from http://code.google.com/p/psutil/
import psutil
import time

import thingspeak

channel_id = 1049013  # PUT CHANNEL ID HERE
key = 'B530FR63JBR4S3MN'   # PUT YOUR WRITE KEY HERE
read_key = 'BQE5HYPZ0YTXJULT' # PUT YOUR READ KEY HERE

def doit(channel):

    cpu_pc = psutil.cpu_percent()
    mem_avail_mb = psutil.virtual_memory().percent

    try:
        response = channel.update({'field4': cpu_pc,'field2': mem_avail_mb})
        print(cpu_pc)
        print(mem_avail_mb)
        print(strftime("%a, %d %b %Y %H:%M:%S", localtime()))
        print(response)
    except:
        print("connection failed")


# sleep for 16 seconds (api limit of 15 secs)
if __name__ == "__main__":
    channel = thingspeak.Channel(id=channel_id, api_key=key)
    while True:
        doit(channel)
        time.sleep(16)
