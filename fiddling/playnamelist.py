import time
import requests
import hashlib
from datetime import datetime

with open('/software_namelist.txt', 'r') as f:
    lines = f.readline().split(' ')

while True:
    for line in lines:
        name=line[0]
        id=line[1]
        res = requests.put("https://anti-epidemic.ecnu.edu.cn/clock/record",
                           json={
                               "number":
                               id,
                               "location":
                               "不在境内",
                               "health":
                               "体温超过37.3",
                               "recordTime":
                               int(time.time() * 1000),
                               "token":
                               hashlib.md5(
                                   f"{name}{id}ecnu1024".encode()).hexdigest()
                           }).json()
        print(res)
        print('sent')
        print(datetime.now(), 'maybeok')
    time.sleep(5 * 3600)
