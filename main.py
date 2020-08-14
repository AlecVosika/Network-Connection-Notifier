import sys
import time
import threading
import subprocess 
from playsound import playsound

# https://stackoverflow.com/questions/35750041/check-if-ping-was-successful-using-subprocess-in-python

ip1 = ["name", '192.168.1.2', 'connected']
ip2 = ["name", '192.168.1.3', 'connected']
devices = (ip1, ip2)

threads = []

class pingcheckThread (threading.Thread):
    def __init__(self, ip):
        threading.Thread.__init__(self)
        self.IP = ip
    def run(self):
        pingcheck(self.IP)


def pingcheck(ip):
    while True:
        res = subprocess.Popen(['ping', '-n', '1',ip[1]],stdout = subprocess.PIPE).communicate()[0]
        # Not Connected
        if ('unreachable' in str(res)):
            if ip[2] == 'connected':
                print(ip[0], "= disconnected\n")
                playsound('alert.wav')
                ip[2] = 'disconnected'
        # Connected       
        else: 
            if ip[2] == 'disconnected':
                print(ip[0], "= Connected\n")
                playsound('alert.wav')
                ip[2] = 'connected'

        time.sleep(5)

# runs through devices and sets up objects for each device for threading
if True:
    for ip in devices:
        thread = pingcheckThread(ip)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()





################################################################################################
#                                      Linux Version
################################################################################################

# import sys
# import time
# import threading
# import subprocess 
# #from playsound import playsound

# ip1 = ["name", '192.168.1.2', 'connected']
# ip2 = ["name", '192.168.1.3', 'connected']
# devices = (ip1, ip2)

# threads = []

# class pingcheckThread (threading.Thread):
#     def __init__(self, ip):
#         threading.Thread.__init__(self)
#         self.IP = ip
#     def run(self):
#         pingcheck(self.IP)


# def pingcheck(ip):
#     res = subprocess.Popen(['ping', '-c1','-W2',ip[1]],stdout = subprocess.PIPE)
#     res.wait()
#     res.poll()
#     # Not Connected
#     if res.poll() == 1:
#         if ip[2] == 'connected':
#             sys.stderr.write(ip[0] + "= disconnected\n")
#             #playsound('alert.wav')
#             ip[2] = 'disconnected'
#     # Connected       
#     else: 
#         if ip[2] == 'disconnected':
#             sys.stderr.write(ip[0] + "= Connected\n")
#             #playsound('alert.wav')
#             ip[2] = 'connected'

#     time.sleep(5)
#     pingcheck(ip)

# # runs through devices and sets up objects for each device for threading
# print('Starting')
# if True:
#     for ip in devices:
#         thread = pingcheckThread(ip)
#         thread.start()
#         threads.append(thread)

#     for thread in threads:
#         thread.join()


