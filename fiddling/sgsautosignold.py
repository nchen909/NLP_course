import time
import requests
import hashlib
from datetime import datetime

# stuid = 10175501112
# name = "陈诺"
#
# while True:
#     res = requests.put("https://anti-epidemic.ecnu.edu.cn/clock/record",
#                        json={
#                            "number":
#                            id,
#                            "location":
#                            "在学校",
#                            "health":
#                            "健康，未超过37.3",
#                            "recordTime":
#                            int(time.time() * 1000),
#                            "token":
#                            hashlib.md5(
#                                f"{name}{stuid}ecnu1024".encode()).hexdigest()
#                        }).json()
#     print(res)
#     print('sent')
#     print(datetime.now(), 'maybeok')
#     time.sleep(5 * 3600)

# POST http://wx.sanguosha.com/api/clock/do HTTP/1.1
# Host: wx.sanguosha.com
# Connection: keep-alive
# Content-Length: 0
# Accept: application/json, text/javascript, */*; q=0.01
# Origin: http://wx.sanguosha.com
# X-Requested-With: XMLHttpRequest
# User-Agent: Mozilla/5.0 (Linux; Android 9; DUK-AL20 Build/HUAWEIDUK-AL20; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045409 Mobile Safari/537.36 MMWEBID/6669 MicroMessenger/7.0.20.1781(0x2700143F) Process/tools WeChat/arm64 NetType/WIFI Language/zh_CN ABI/arm64
# Referer: http://wx.sanguosha.com/clock2019/
# Accept-Encoding: gzip, deflate
# Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7
# Cookie: XSRF-TOKEN=eyJpdiI6ImtlTlwvb2lDWGJMdG9FdlZZMkI0WU53PT0iLCJ2YWx1ZSI6ImNHMzhZa3lMdGtXa1dLZXZcL1lOcXRtdFN5VG0wb0UxMEdqT2ZZcWs0SHhJbjRvSVF5V0FqQ1dMODE0TzVtbk8zQk9ac0dXYTRaNkw2ZFhaZHB5SGR1QT09IiwibWFjIjoiMjg0ZTVlODQwMDA1NDAwNWRjZTgyNTQ0NDRiYjg1NWYxOTM0YzY3Y2VmMTk2ZTFmYzdhMjVmNjUyYjFjZjI5ZiJ9; php_session=eyJpdiI6InVGV1pVdU9vTVZsMnBnNHlKU09jT0E9PSIsInZhbHVlIjoiQU5wV1VIcGFXMEVTYlZNcVBXTk02YkorRnBscnJpeE9YTytSUnV2Y1lhV3VQRG41VkMzZjdCM1FJcndpblhBamUyVW92UXJlaWxkV1VyUHk2QjVwc3c9PSIsIm1hYyI6IjBhNWY5YTBhNTdlOWE0Yzc4N2ZlOWEzYTMyNWVjYTA1MmRiMGZkMzM5MjBhM2NmZTA5ZWZjMzU4M2RlMTkzMjYifQ%3D%3D

# -*- coding:utf-8 -*-
import requests
import json

host = "http://wx.sanguosha.com/"
endpoint = "api/clock/do"
cookie20201123="XSRF-TOKEN=eyJpdiI6Ijg4MllkVDBVSEVhOWlcLzdJWWZDYTZBPT0iLCJ2YWx1ZSI6InQ4bzk0bWIxbEtlSmY5cUlmVXVcL1BMaVpLYzdNQjE0SnBJTkFMRU9NTitHRlR1cU8xOUhvZVJOT2tvM05NYjVIQUh3bVJ0Zk1xaVwvdTBLbDZudSs5bWc9PSIsIm1hYyI6IjhlM2NkZDI1NDM2ZGU1MzhjZDdmOWMwYzRmNTVkYzk5NmViOGVjZjU2ZjU5ZjIyNGRmYzRkYjllZTkwODEyY2IifQ%3D%3D; php_session=eyJpdiI6IllsNzYxRFBEM0VaWTZacE5heGxIcEE9PSIsInZhbHVlIjoiZHJNd2ZieWNEYVpaNmNPZ1JpcmE2ZVpVMTZiRTBqRGMxSXFmSFwvdHlGazNuOGU3YTdcL0QxVXZmWk4yblRMakVhSEhNdHZ6Zis4R3pFOEljbzZsQ1wvWmc9PSIsIm1hYyI6IjE0ZTQyMTEyOTM1M2QwZGY3NmQzOTc1MzliMWNhOTE3N2ZiODAyOTdiYmQ3OWM3ZDlmNTI3MDMzMTg5YTEzNzQifQ%3D%3D"
cookie202011232="XSRF-TOKEN=eyJpdiI6IldmS0RhZVZiT0wwQlNiSVBLc09CakE9PSIsInZhbHVlIjoiK25ETm8yZWNWM041TExQZWI0bTdsN2c1OWRZZnkxaXpITVBBR0ZMV3ZPQ0VCQnVzaTVTYno1Z0VJZXAzYXhvWXh5aU15NzI4V29LaGZVNzYrM3ZLZEE9PSIsIm1hYyI6IjMxODc0YTM4Zjg3MDMwNjJmYjcyNzk2ODRmZTY0ODUzNmEwNDZiZWJiNjM1MDY5MTcwMzE5MzkzZjY2OGYzODAifQ%3D%3D; php_session=eyJpdiI6Ino2c3AxNVlRaUhyMG01WjN0UzY3NHc9PSIsInZhbHVlIjoiNks0aFlEMTh5NDZuSmJpR1duclwvVFQxcDFMM25GZm1Sa1J1dExwOEg5aHdIdDZlQkErcVAyYWRsK2NQWUNkS0ZNNjdZcjlOMWxvVGRVa1J3RGN1R2JnPT0iLCJtYWMiOiI3NmU5MmQ5NzZmMjRiZTc0YTE0MjFlNzNmYjViOWIyODA1ZGI5YTk1NzFmOTRmMDVkM2NiZDBjZjhlMzdmMmU5In0%3D"
cookie20201124="XSRF-TOKEN=eyJpdiI6ImtlTlwvb2lDWGJMdG9FdlZZMkI0WU53PT0iLCJ2YWx1ZSI6ImNHMzhZa3lMdGtXa1dLZXZcL1lOcXRtdFN5VG0wb0UxMEdqT2ZZcWs0SHhJbjRvSVF5V0FqQ1dMODE0TzVtbk8zQk9ac0dXYTRaNkw2ZFhaZHB5SGR1QT09IiwibWFjIjoiMjg0ZTVlODQwMDA1NDAwNWRjZTgyNTQ0NDRiYjg1NWYxOTM0YzY3Y2VmMTk2ZTFmYzdhMjVmNjUyYjFjZjI5ZiJ9; php_session=eyJpdiI6InVGV1pVdU9vTVZsMnBnNHlKU09jT0E9PSIsInZhbHVlIjoiQU5wV1VIcGFXMEVTYlZNcVBXTk02YkorRnBscnJpeE9YTytSUnV2Y1lhV3VQRG41VkMzZjdCM1FJcndpblhBamUyVW92UXJlaWxkV1VyUHk2QjVwc3c9PSIsIm1hYyI6IjBhNWY5YTBhNTdlOWE0Yzc4N2ZlOWEzYTMyNWVjYTA1MmRiMGZkMzM5MjBhM2NmZTA5ZWZjMzU4M2RlMTkzMjYifQ%3D%3D"
cookie20201124ydk="XSRF-TOKEN=eyJpdiI6Ik9sWXRLTkdhTFVHYVwvRnB4a0NmcHlRPT0iLCJ2YWx1ZSI6InMxWVhURks4WGl6Z0tpdm1zMHpNQXVXTHArSUVhYW1nS21RcUxtOW9YZ0swMmZqRHd5ajVBZWNaSlZQTW9DRVIyXC9BbEZrMklBUlwvb095VVBjVFhYeHc9PSIsIm1hYyI6ImMxOTc0ZmJjOWM2MDA0YmUzYTg4NGUyZTYxM2RmNjE5OTcyNGJiZDk5MzFmYzkwYzc5MWMxZDFjOWU2ZjMxM2UifQ%3D%3D; php_session=eyJpdiI6Ilc4R2dNOTVhZkJBVkJ0SmM5S0lFSlE9PSIsInZhbHVlIjoiMzhaaWVLQTlHOXVkZDIzTjV5ZDk5c0NGOG1PVmdiSlVEbVBpaUNEdzc3bkZcLzVcL0NxSEdxSEZBVlBnSFVEZjNCek9RU3pZSCtTV2pHODBcL1IyNTNtZnc9PSIsIm1hYyI6IjY0ZjFiNTExZDgyYzkwZDdlYmI5YjE2ZTY2MGRiMTI1ZmRjYmJlNTZlODk3OGE0ZWI5ZDIxN2Y0ODE0OGVhZDgifQ%3D%3D"
cookie202011241440="XSRF-TOKEN=eyJpdiI6Ijk0bmxONmorTmhMazNBQlpiRlJ4NlE9PSIsInZhbHVlIjoiSGZsUWtVZ1BTUGNSeWtCeUpLQzdrOEpUUGtnaFViclduWFJiZ2p0dTR5OWgrV0VySnl3ZmJDK2Z6SThITG1NSnNPQnZHMUcxT1wvd0dDZ2ZCZ1hLWVlRPT0iLCJtYWMiOiI4NjJkNzczNWYzYWI2MGI4ZTI0YWQxMzRjYjk1YmQ5ZGMwMmRhZDg3YmYyNDM4MzcxNjEwZTNmNWExOTA5ZDA2In0%3D; php_session=eyJpdiI6IkQzakNIMFpNc1JLcFdkUUVyd1ZmeVE9PSIsInZhbHVlIjoiSWcrZE5XSitHUFFlSDRsNHJpSE1qK2xPcTcwNzBjOTFEU2ZvOU9rTWErclRiQUh4K093OWx0NEROK0l6cERXdVM0Y21mdExKRlZzSVdPOXM5Zk9KS0E9PSIsIm1hYyI6IjQ0MjQ5OTI2MDE0M2U1Y2FlNjgyNDc3YmY2YjMyMjUzYWY5MjQ4NWQ0OGQ0ODQ1NTRlMDE0OWQ2M2UzMDZkMTcifQ%3D%3D"
cookies={'XSRF-TOKEN': 'eyJpdiI6Im95NHJQSStKOUw5UEx2SW5KRWpubnc9PSIsInZhbHVlIjoicjRDQjhKSnFwbkxVd25udVNQV1luUWtkckJBeEVOT1dyZWNZWXBCNnBNWXRpd2lDTWxPZGR3TUlNeXZTSENOYWE3VnB0NCt5em9RNk5vMlwvWkpmblZBPT0iLCJtYWMiOiIwMTViZDc1YzE2NDBhNjJlM2FjOTg5NzY3NmYyYTY1NWJmYjllYWQ2ZTA1ZGZiNjY4NzY2ZWVmOGU0ODcwMmExIn0%3D', 'php_session': 'eyJpdiI6ImF5M1wvOHlXNXRScGQ1aWFFV0xxaGN3PT0iLCJ2YWx1ZSI6Iko2UVlvcWMrVFZ0VHptb25ZOFIxRmtocFl3TzJNajU3bWlLV2ZWQnZXdnlcLzFUMHpHbElHaXcyeWR4YllBQlNLeHRCQ2NCS2Nza2g4bVVqZ29PUXdCdz09IiwibWFjIjoiMGNiZmJiMjc0NjhlN2YzZTJkMTlmZGIzNmQxODViNzMwZDY5YTE4YTUzMmJlOTFjNjcwMzdlMDkxMWY1M2QyMCJ9'}
url = ''.join([host,endpoint])
headers = {"Accept": "application/json, text/javascript, */*; q=0.01",
           "Accept-Encoding": "gzip, deflate",
           "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
           "User-Agent": "Mozilla/5.0 (Linux; Android 9; DUK-AL20 Build/HUAWEIDUK-AL20; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045409 Mobile Safari/537.36 MMWEBID/6669 MicroMessenger/7.0.20.1781(0x2700143F) Process/tools WeChat/arm64 NetType/WIFI Language/zh_CN ABI/arm64",
           "X-Requested-With": "XMLHttpRequest",
           "Host": "wx.sanguosha.com"}
while 1:
    # r = requests.post(url)
    r = requests.post(url,headers=headers,cookies=cookies)
    response = r.json()
    print(response)
    print(r.cookies)
    cookies = requests.utils.dict_from_cookiejar(r.cookies)
    print(cookies)
    time.sleep(3600)

