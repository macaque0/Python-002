学习笔记

* Q1:pipelines.py中open文件是否是多次打开关闭，如何可以打开一次
  ```python
  with open('./doubanmovie.txt', 'a+', encoding='utf-8') as article:
            article.write(output)
  ```
* Q2: 在spider类型如果有start_requests中定义了url,那么start_urls 是不是就没有作用了？
  ```python
  start_urls = ['https://movie.douban.com/top250']

  def start_requests(self):
      for i in range(1):
          url = f'https://movie.douban.com/top250?start={i*25}'
          yield scrapy.Request(url=url,callback=self.parse)
  ```
 * Q3:settings.py中USER_AGENT 为什么不需要写值，而是固定的内容
   ```python
   USER_AGENT = 'myspider (+http://www.yourdomain.com)'
   ```
 * scrapy生成的配置文件中 ITEM_PIPELINES 需要配置,默认是注释掉的，不然pipeline不起作用
