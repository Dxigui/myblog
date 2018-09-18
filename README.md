## 注意
> 此项目在提交时忽略了 settings.py 文件和 migrations 文件夹中部分信息  

> migrations 文件夹中的是数据库迁移文件  

> settings.py 文件替换成 online_settings.py  

> 其中 SECRET_KEY/DATABASES/DISQUS_API_KEY 需要自行配置  

## 关于本站  
* 本站是基于 Django 1.11 版本开发
* 后端为 Python 3.5.2
* 数据库为 MySQL 5.7
* 网站部署为 Nginx + gunicorn
* 前端模板出自 [zerenwu](https://github.com/zmrenwu)
* 其他库请查看 requirements.txt 文件
* 这是我的个人博客网站,主要发布一些技术文章和日常博文

## 功能
1. 已完成  
  * 使用 Django 自带的后台管理系统
  * 对文章进行分类和归档,以及给文章添加标签
  * 基于 Haystack + Whoosh + Jieba 的全文搜索,并支持中文
  * 支持 RSS 订阅
  * 支持友情链接
2. TODO
  * 用户登录验证模块
  * 评论模块
  * 网站扩展

## 声明
网站源码对所有人开源,如果直接使用只需要注明出处.如果发现源码有错误欢迎指出.
