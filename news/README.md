
**创建Mysql的表的字段**

```
CREATE TABLE tb_google_news(
    id INT AUTO_INCREMENT,
    title VARCHAR(50),
    image_url VARCHAR(200),
    action_url VARCHAR(200),
    source VARCHAR(30),
    PRIMARY KEY(id)
)ENGINE=INNODB DEFAULT CHARSET=utf8;
```
