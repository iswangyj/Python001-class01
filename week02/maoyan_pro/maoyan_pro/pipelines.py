# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymysql
dbInfo = {
    'host' : 'localhost',
    'port' : 3306,
    'user' : 'root',
    'password' : 'root',
    'db' : 'py_study'
}

class MaoyanProPipeline:
    def process_item(self, item, spider):
        title = item['title']
        types = item['types']
        plan_date = item['plan_date']

        conn = pymysql.connect(
            host = dbInfo['host'],
            port = dbInfo['port'],
            user = dbInfo['user'],
            password = dbInfo['password'],
            db = dbInfo['db']
        )
        cur = conn.cursor()
        try:
            values = [title, types, plan_date]
            print(f'values: {values}')
            cur.execute('INSERT INTO  movie (`title`, `types`, `plan_date`) values(%s,%s,%s)' ,values)

            # 关闭游标
            cur.close()
            conn.commit()
        except:
            conn.rollback()
         # 关闭数据库连接
        conn.close()

        return item
