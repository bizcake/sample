
import time
import os
import subprocess
import re

pinglist = ( '52.231.54.76', '' )
print(type(pinglist))
p = re.compile('[=]\s(\d+)[m][s]')

for i in pinglist:

    cmd = 'ping -n 3 '+i     # ping을 3번 수행
    try:
        for x in subprocess.check_output(cmd).splitlines():
            p1 = p.findall(str(x))

        print(i, 'Ping Ok','최소 응답시간: '+p1[0],'최대 응답시간: '+p1[1],'평균 응답시간: '+p1[2])

    except subprocess.CalledProcessError:
        print(i, 'Ping Check')

# n = 5
# for i in range(1, 10):
#     print(i)
#     if i == 5:
#         continue
#     else:
#         cmd = 'ping {}'.format("52.231.54.76")
#         os.system(cmd)
#         continue
#     time.sleep(.5)