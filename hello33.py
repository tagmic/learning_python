#python常用模块
#datetime
from datetime import datetime
now=datetime.now()
print(now)
#datetime是模块，该模块里面有一个datetime类来提供当前的时间
#获取指定某个日期和时间
dt=datetime(2015,4,5,12,30)
print(dt)
#datetime转str
print(now.strftime('%a,%b%d%h:%m'))
#collections集合模块tuple.dict.list等
#base64
import base64
print(base64.b64encode(b'binary\x00string'))
#########################比较多，用到再查###############
