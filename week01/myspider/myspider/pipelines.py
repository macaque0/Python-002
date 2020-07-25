# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas


class MyspiderPipeline:
    # 写入次数
    counter = 0
    def process_item(self, item, spider):
        data = []
        data.append(item.values())
        df = pandas.DataFrame(data=data, columns=["名称", "类型", "上映时间"])
        # 不是第一次写入就追加
        mode = 'a' if MyspiderPipeline.counter > 0 else 'w'
        # 只有第一次写入时加header
        header = False if MyspiderPipeline.counter > 0 else True
        # windows 用gbk
        df.to_csv('./maoyan2.csv', mode=mode, header=header, index=False, encoding='gbk')
        MyspiderPipeline.counter+=1
        return item
