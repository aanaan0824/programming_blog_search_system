# coding=utf-8

from genericpath import exists
from bs4 import BeautifulSoup
import requests
import lxml
import os

url = "https://www.cs.tsinghua.edu.cn/"

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

path_str = "html"
path_splitter = '\\'
url_splitter = '/'
path_dir = path_str + path_splitter

css_raw = "css"
css_str = path_dir + css_raw
css_dir = css_str + path_splitter
css_savedir = css_raw + path_splitter

script_raw = "scripts"
script_str = path_dir + script_raw
script_dir = script_str + path_splitter
script_savedir = script_raw + path_splitter

img_raw = "images"
img_str = path_dir + img_raw
img_dir = img_str + path_splitter
img_savedir = img_raw + path_splitter

class Website:
    def __init__(self, url_str = "", file_name = "", save_name = ""):
        self.url_prefix = url_str
        self.file_name = file_name
        self.url = self.url_prefix + self.file_name
        self.child_list = []
        self.dir = path_dir + save_name
        
    def crawl_all(self):
        print("Start to crawl:", self.url)
        print(self.file_name)

        web_data = requests.get(self.url)
        web_data.encoding='utf-8'
        # print(web_data.encoding)
        self.text = web_data.text
        self.data = BeautifulSoup(web_data.content, 'lxml')
        self.css_list = self.data.find_all('link', rel='stylesheet')
        self.script_list = self.data.find_all('script')
        self.img_list = self.data.find_all('img')
        self.img_list += self.data.find_all('input', type='image')
        self.icon_list = self.data.find_all('link', type='image/x-icon')
        self.href_list = self.data.find_all('a')

        for css in self.css_list:
            css_url = css['href']
            file_name = css_url.split('/')[-1]
            #print(file_name)
            if(os.path.exists(css_dir + file_name) == False):
                try:
                    #print(url + css_url)
                    res = requests.get(url + css_url)
                    res.encoding='utf-8'
                    txt = res.text
                    #print(txt)
                    self.text = self.text.replace(css_url, css_savedir + file_name)
                    #print(css_url, css_dir + file_name)
                    with open(css_dir + file_name, 'w', encoding='utf-8') as f:
                        f.write(txt)
                        f.close()
                except Exception:
                    pass
            else:
                self.text = self.text.replace(css_url, css_savedir + file_name)
                #print(css_url, css_dir + file_name)

        for script in self.script_list:
            if script.has_attr('orisrc'):
                script_url = script['orisrc']
            elif script.has_attr('src'):
                script_url = script['src']
            replace_url = script_url
            if (script_url[0] == '/'):
                script_url = script_url[1:]
            file_name = script_url.split('/')[-1]
                #print(file_name)
            if(os.path.exists(script_dir + file_name) == False):
                try:
                    #print(url + script_url)
                    res = requests.get(url + script_url)
                    res.encoding='utf-8'
                    txt = res.text
                    #print(txt)
                    self.text = self.text.replace(replace_url, script_savedir + file_name)
                    #print(script_url, script_savedir + file_name)
                    with open(script_dir + file_name, 'w', encoding='utf-8') as f:
                        f.write(txt)
                        f.close()
                except Exception:
                    pass
            else:
                self.text = self.text.replace(replace_url, script_savedir + file_name)
                #print(script_url, script_savedir + file_name)
        
        for img in self.img_list:
            if img.has_attr('orisrc'):
                img_url = img['orisrc']
            elif img.has_attr('src'):
                img_url = img['src']
            file_name = (img_url.split('/')[-1]).split('?e=')[0]
            #file_name = file_name.
            print(file_name)
            print(url + img_url)
            if(os.path.exists(img_dir + file_name) == False):
                try:
                    #print(url + img_url)
                    res = requests.get(url + img_url)
                    content = res.content
                    #print(content)
                    #print(len(content), img_dir + file_name)
                    self.text = self.text.replace(img_url, img_savedir + file_name)
                    #print(img_url, img_dir + file_name)
                    with open(img_dir + file_name, 'wb') as f:
                        f.write(content)
                        f.close()
                except Exception:
                    pass
            else:
                self.text = self.text.replace(img_url, img_savedir + file_name)
                #print(img_url, img_dir + file_name)
        
        for icon in self.icon_list:
            img_url = icon['href']
            file_name = img_url.split('/')[-1]
            if(os.path.exists(img_dir + file_name) == False):
                try:
                    #print(url + img_url)
                    res = requests.get(url + img_url)
                    content = res.content
                    #print(content)
                    #print(len(content), img_dir + file_name)
                    self.text = self.text.replace(img_url, img_savedir + file_name)
                    #print(img_url, img_dir + file_name)
                    with open(img_dir + file_name, 'wb') as f:
                        f.write(content)
                        f.close()
                except Exception:
                    pass
            else:
                self.text = self.text.replace(img_url, img_savedir + file_name)
                #print(img_url, img_dir + file_name)
        
        for href in self.href_list:
            if href.has_attr('href'):
                href_url = href['href']
                #print(href_url)
                if (href_url.startswith('http')):
                    continue
                file_name = href_url.split('/')[-1]
                self.text = self.text.replace(href_url, file_name)

        print("--------------------------Save", self.file_name)
        with open(self.dir, 'w', encoding='utf-8') as f:
            f.write(self.text)
            f.close()

        
        for href in self.href_list:
            if href.has_attr('href'):
                href_url = href['href']
                #print(href_url)
                if (href_url.startswith('http')):
                    continue
                file_name = href_url.split('/')[-1]
                all_url = self.url_prefix + href_url
                if(os.path.exists(path_dir + file_name) == False):
                    try:
                        prefix_list = all_url.split('/')[:-1]
                        prefix = '/'.join(prefix_list) + '/'
                        new_child = Website(prefix, file_name, file_name)
                        new_child.crawl_all()
                    except Exception:
                        pass


        
        