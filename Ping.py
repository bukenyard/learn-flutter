# ping script in python

import subprocess
import platform 

def pingServer(host):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    number_of_pin_requests = '5'
    command = ['ping', param, number_of_pin_requests, host]
    return subprocess.call(command)

host = 'localhost'
print(pingServer(host))