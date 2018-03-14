1. 开启redis

```
 redis-server
```

2. 在Slave端分别启动爬虫，不分先后：

```
scrapy runspider myspider.py
```

3. 在Master端的redis-cli里push一个start_urls

```
lpush redis58spider:start_urls http://sh.58.com/chuzu/
```