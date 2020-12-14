# -*- coding:utf-8 -*-
import time
import requests
import hashlib

from datetime import datetime


import requests
import json

host = "http://m.api.4399.cn/android/box/v3.0/sign-in.html"
endpoint = "api/clock/do"
cookie20201123="XSRF-TOKEN=eyJpdiI6Ijg4MllkVDBVSEVhOWlcLzdJWWZDYTZBPT0iLCJ2YWx1ZSI6InQ4bzk0bWIxbEtlSmY5cUlmVXVcL1BMaVpLYzdNQjE0SnBJTkFMRU9NTitHRlR1cU8xOUhvZVJOT2tvM05NYjVIQUh3bVJ0Zk1xaVwvdTBLbDZudSs5bWc9PSIsIm1hYyI6IjhlM2NkZDI1NDM2ZGU1MzhjZDdmOWMwYzRmNTVkYzk5NmViOGVjZjU2ZjU5ZjIyNGRmYzRkYjllZTkwODEyY2IifQ%3D%3D; php_session=eyJpdiI6IllsNzYxRFBEM0VaWTZacE5heGxIcEE9PSIsInZhbHVlIjoiZHJNd2ZieWNEYVpaNmNPZ1JpcmE2ZVpVMTZiRTBqRGMxSXFmSFwvdHlGazNuOGU3YTdcL0QxVXZmWk4yblRMakVhSEhNdHZ6Zis4R3pFOEljbzZsQ1wvWmc9PSIsIm1hYyI6IjE0ZTQyMTEyOTM1M2QwZGY3NmQzOTc1MzliMWNhOTE3N2ZiODAyOTdiYmQ3OWM3ZDlmNTI3MDMzMTg5YTEzNzQifQ%3D%3D"
cookie202011232="XSRF-TOKEN=eyJpdiI6IldmS0RhZVZiT0wwQlNiSVBLc09CakE9PSIsInZhbHVlIjoiK25ETm8yZWNWM041TExQZWI0bTdsN2c1OWRZZnkxaXpITVBBR0ZMV3ZPQ0VCQnVzaTVTYno1Z0VJZXAzYXhvWXh5aU15NzI4V29LaGZVNzYrM3ZLZEE9PSIsIm1hYyI6IjMxODc0YTM4Zjg3MDMwNjJmYjcyNzk2ODRmZTY0ODUzNmEwNDZiZWJiNjM1MDY5MTcwMzE5MzkzZjY2OGYzODAifQ%3D%3D; php_session=eyJpdiI6Ino2c3AxNVlRaUhyMG01WjN0UzY3NHc9PSIsInZhbHVlIjoiNks0aFlEMTh5NDZuSmJpR1duclwvVFQxcDFMM25GZm1Sa1J1dExwOEg5aHdIdDZlQkErcVAyYWRsK2NQWUNkS0ZNNjdZcjlOMWxvVGRVa1J3RGN1R2JnPT0iLCJtYWMiOiI3NmU5MmQ5NzZmMjRiZTc0YTE0MjFlNzNmYjViOWIyODA1ZGI5YTk1NzFmOTRmMDVkM2NiZDBjZjhlMzdmMmU5In0%3D"
cookie20201124="XSRF-TOKEN=eyJpdiI6ImtlTlwvb2lDWGJMdG9FdlZZMkI0WU53PT0iLCJ2YWx1ZSI6ImNHMzhZa3lMdGtXa1dLZXZcL1lOcXRtdFN5VG0wb0UxMEdqT2ZZcWs0SHhJbjRvSVF5V0FqQ1dMODE0TzVtbk8zQk9ac0dXYTRaNkw2ZFhaZHB5SGR1QT09IiwibWFjIjoiMjg0ZTVlODQwMDA1NDAwNWRjZTgyNTQ0NDRiYjg1NWYxOTM0YzY3Y2VmMTk2ZTFmYzdhMjVmNjUyYjFjZjI5ZiJ9; php_session=eyJpdiI6InVGV1pVdU9vTVZsMnBnNHlKU09jT0E9PSIsInZhbHVlIjoiQU5wV1VIcGFXMEVTYlZNcVBXTk02YkorRnBscnJpeE9YTytSUnV2Y1lhV3VQRG41VkMzZjdCM1FJcndpblhBamUyVW92UXJlaWxkV1VyUHk2QjVwc3c9PSIsIm1hYyI6IjBhNWY5YTBhNTdlOWE0Yzc4N2ZlOWEzYTMyNWVjYTA1MmRiMGZkMzM5MjBhM2NmZTA5ZWZjMzU4M2RlMTkzMjYifQ%3D%3D"
cookie20201124ydk="XSRF-TOKEN=eyJpdiI6Ik9sWXRLTkdhTFVHYVwvRnB4a0NmcHlRPT0iLCJ2YWx1ZSI6InMxWVhURks4WGl6Z0tpdm1zMHpNQXVXTHArSUVhYW1nS21RcUxtOW9YZ0swMmZqRHd5ajVBZWNaSlZQTW9DRVIyXC9BbEZrMklBUlwvb095VVBjVFhYeHc9PSIsIm1hYyI6ImMxOTc0ZmJjOWM2MDA0YmUzYTg4NGUyZTYxM2RmNjE5OTcyNGJiZDk5MzFmYzkwYzc5MWMxZDFjOWU2ZjMxM2UifQ%3D%3D; php_session=eyJpdiI6Ilc4R2dNOTVhZkJBVkJ0SmM5S0lFSlE9PSIsInZhbHVlIjoiMzhaaWVLQTlHOXVkZDIzTjV5ZDk5c0NGOG1PVmdiSlVEbVBpaUNEdzc3bkZcLzVcL0NxSEdxSEZBVlBnSFVEZjNCek9RU3pZSCtTV2pHODBcL1IyNTNtZnc9PSIsIm1hYyI6IjY0ZjFiNTExZDgyYzkwZDdlYmI5YjE2ZTY2MGRiMTI1ZmRjYmJlNTZlODk3OGE0ZWI5ZDIxN2Y0ODE0OGVhZDgifQ%3D%3D"
cookie202011241440="XSRF-TOKEN=eyJpdiI6Ijk0bmxONmorTmhMazNBQlpiRlJ4NlE9PSIsInZhbHVlIjoiSGZsUWtVZ1BTUGNSeWtCeUpLQzdrOEpUUGtnaFViclduWFJiZ2p0dTR5OWgrV0VySnl3ZmJDK2Z6SThITG1NSnNPQnZHMUcxT1wvd0dDZ2ZCZ1hLWVlRPT0iLCJtYWMiOiI4NjJkNzczNWYzYWI2MGI4ZTI0YWQxMzRjYjk1YmQ5ZGMwMmRhZDg3YmYyNDM4MzcxNjEwZTNmNWExOTA5ZDA2In0%3D; php_session=eyJpdiI6IkQzakNIMFpNc1JLcFdkUUVyd1ZmeVE9PSIsInZhbHVlIjoiSWcrZE5XSitHUFFlSDRsNHJpSE1qK2xPcTcwNzBjOTFEU2ZvOU9rTWErclRiQUh4K093OWx0NEROK0l6cERXdVM0Y21mdExKRlZzSVdPOXM5Zk9KS0E9PSIsIm1hYyI6IjQ0MjQ5OTI2MDE0M2U1Y2FlNjgyNDc3YmY2YjMyMjUzYWY5MjQ4NWQ0OGQ0ODQ1NTRlMDE0OWQ2M2UzMDZkMTcifQ%3D%3D"
cookies={'XSRF-TOKEN': 'eyJpdiI6Im95NHJQSStKOUw5UEx2SW5KRWpubnc9PSIsInZhbHVlIjoicjRDQjhKSnFwbkxVd25udVNQV1luUWtkckJBeEVOT1dyZWNZWXBCNnBNWXRpd2lDTWxPZGR3TUlNeXZTSENOYWE3VnB0NCt5em9RNk5vMlwvWkpmblZBPT0iLCJtYWMiOiIwMTViZDc1YzE2NDBhNjJlM2FjOTg5NzY3NmYyYTY1NWJmYjllYWQ2ZTA1ZGZiNjY4NzY2ZWVmOGU0ODcwMmExIn0%3D', 'php_session': 'eyJpdiI6ImF5M1wvOHlXNXRScGQ1aWFFV0xxaGN3PT0iLCJ2YWx1ZSI6Iko2UVlvcWMrVFZ0VHptb25ZOFIxRmtocFl3TzJNajU3bWlLV2ZWQnZXdnlcLzFUMHpHbElHaXcyeWR4YllBQlNLeHRCQ2NCS2Nza2g4bVVqZ29PUXdCdz09IiwibWFjIjoiMGNiZmJiMjc0NjhlN2YzZTJkMTlmZGIzNmQxODViNzMwZDY5YTE4YTUzMmJlOTFjNjcwMzdlMDkxMWY1M2QyMCJ9'}

headers = {"Accept-Encoding": "gzip",
           "User-Agent": "4399GameCenter/5.8.0.42(android;DUK-AL20;9;720x1204;WIFI;1525.565;wap4399)",
           "Host": "m.api.4399.cn"}
while 1:
    # r = requests.post(url)
    r = requests.post(host,json={"dateline":"1606228696",
                                 "sign":"09c3ab1b7c3a0174f82dfbf07ec5932c",
                                 "packages":'["com.netease.cloudmusic","com.alibaba.android.rimet","com.sohu.inputmethod.sogou","com.taobao.taobao","com.eg.android.AlipayGphone","com.zhihu.android","com.tencent.wemeet.app","com.autonavi.minimap","com.tencent.mm","com.sanguosha.sgsolly.m4399","com.qihoo.cleandroid_cn","us.zoom.videomeetings"]',
                                 "day":"0",
                                 "deviceId":"865968031002613"
                                 },headers=headers)
    response = r.json()
    
    print(response)
    print(r.cookies)
    cookies = requests.utils.dict_from_cookiejar(r.cookies)
    print(cookies)
    time.sleep(3600)

