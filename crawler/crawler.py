# coding=utf-8

from website import Website
import website
import os


if not os.path.exists(website.path_str):
    os.mkdir(website.path_str)
if not os.path.exists(website.css_str):
    os.mkdir(website.css_str)
if not os.path.exists(website.script_str):
    os.mkdir(website.script_str)
if not os.path.exists(website.img_str):
    os.mkdir(website.img_str)

index = Website(website.url, "", "index.html")
index.crawl_all()

#index = Website("https://www.cs.tsinghua.edu.cn/info/1088/", "3807.htm", "3807.htm")
#index.crawl_all()

