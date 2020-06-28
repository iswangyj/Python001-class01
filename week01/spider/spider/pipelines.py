# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SpiderPipeline:
    def process_item(self, item, spider):
        title = item['title']
        tags = item['tags']
        plan_date = item['plan_date']

        with open('../result/maoyan2.csv', 'a+', encoding='utf-8') as f:
            output = f'{title}\t{tags}\t{plan_date}\n\n'
            f.write(output)
        return item
