from PIL import Image
im=Image.open('test.png')
print(im.format,im.size,im.mode)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########## prepare ##########

# install mysql-connector-python:
# pip3 install mysql-connector-python --allow-external mysql-connector-python

import  pymysql.cursors
from datetime import date, datetime, timedelta
# change root password to yours:
config = {
          'host':'127.0.0.1',
          'port':3306,
          'user':'root',
          'password':'123456',
          'db':'smart_cabinet',
          'charset':'utf8mb4',
          'cursorclass':pymysql.cursors.DictCursor,
          }
connection = pymysql.connect(**config)

# 获取明天的时间
tomorrow = datetime.now().date() + timedelta(days=1)

# 执行sql语句
try:
    with connection.cursor() as cursor:
        # 执行sql语句，插入记录
        sql = 'INSERT INTO user_x (user_id, user_token, user_phone, mac_address, reg_date) VALUES (%s, %s, %s, %s, %s)'
        cursor.execute(sql, ('sicao-004', 'UiaOze4WlTbmS7P5VCHqu2gxyrvtKNjX6YcakAk', '13534199861', 'f0fe6b366999', tomorrow));
    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
    connection.commit()

finally:
    connection.close();
    
