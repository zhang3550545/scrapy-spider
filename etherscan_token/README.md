### 项目介绍

#### etherscan_token 项目
ethercscan_token：爬取`https://etherscan.io/tokens`链接中的数据

在spider目录下，每个xxx_spider.py文件爬取的是`https://etherscan.io/tokens`对应的条目。如：`eos_spider.py`抓取的是EOS的token数据。

**如果需要抓取其他，类似EOS的token，需要修改如下地方：**

1. 复制eos_spider.py文件，重命名xxx_spider.py
2. 修改xxx_spider.py中的name，改为xxx
3. 修改url="...a=xxx..."，a的参数，可见`https://etherscan.io/tokens/xxx`的详情页。
4. 修改settings.py文件，添加``MONGODB_COLLECTION_XXX = 'tb_xxx'``
5. 修改pipeitem.py文件，`self.tb_xxx = settings['MONGODB_COLLECTION_xxx']`
6. 在pipeitem文件的`process_item`方法中，添加一个分支，写入数据库。（记住导包）
7. 在Terminal中执行`scrapy crawl xxx`命令，xxx就是xxx_spider.py中的name值


**如果是不想从头开始爬取数据，可以修改spider目录中的每个`xxx_spider.py`文件的page。**


#### deal_data项目

处理mongodb中的数据，生成csv文件。*(直接运行parse_data.py文件就好)*


