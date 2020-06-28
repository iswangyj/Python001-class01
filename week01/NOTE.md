## 学习总结
1. 本周学习两种爬取数据的方式
* 第三方库requests、bs4以及pandas相结合爬取并保存数据
* Scrapy框架爬取数据
2. 顺利完成学习以及作业
3. python掌握程度比较生疏，接下来完成课程的基础下将进一步学习并熟悉python常用方法和第三方库

## Scrpay使用步骤
1. 安装scrapy
```shell
pip install scrapy
```

2. 创建scrapy项目
```shell
# spider是项目名
scrapy startproject spider
```

3. 生成爬虫
```shell
# spider为项目名
cd spider
# douban为爬虫名 
# douban.com为爬虫限制地址
scrapy genspider douban douban.com
```

4. 编写爬虫逻辑
5. pipeline中编写保存相关代码
6. 启动爬虫
```shell
# douban为爬虫名
scrapy crawl douban
```
> 此命令需要在scrapy.cfg文件所在位置使用


