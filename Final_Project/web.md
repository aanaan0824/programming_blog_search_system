## 第二部分 web应用建立说明（项目文档）

#### 一、数据库建立

本次大作业数据库使用Django自带的模型models搭建，依赖于本地的mysql数据库。主要包含两个类BlogInfo与comment，对应博客和博客的评论。两者之间使用ForeignKey进行连接，具体内容如下：

<img src="C:\Users\AQ\AppData\Roaming\Typora\typora-user-images\image-20220910172453325.png" alt="image-20220910172453325" style="zoom:67%;" />

上半段为博客的作者、浏览等相关信息，下半段则是博客标签的判定。

由于爬虫数据存储为json格式，因此读入到数据库中时经历了一段转换过程，这段过程的代码及其实现附于爬虫文档reptile.ipynb中，此处不多赘述。

#### 二、网站页面搭建

首先，本网站运用了bootstrap框架进行渲染，另外加入了bootstrap官方example css作为辅助。实际风格如图所示：

<img src="C:\Users\AQ\AppData\Roaming\Typora\typora-user-images\image-20220910172956151.png" alt="image-20220910172956151" style="zoom: 33%;" />

共设置四个模板，分别对应博客正文页、博客首页、博客列表页与搜索结果页。博客列表页承担了全部博客列表与博客分类列表两项功能。

<img src="C:\Users\AQ\AppData\Roaming\Typora\typora-user-images\image-20220910173035502.png" alt="image-20220910173035502" style="zoom:67%;" />

博客首页已于上文展示，因此将另外三个模板页面展示如下：

###### 搜索结果页：

<img src="C:\Users\AQ\AppData\Roaming\Typora\typora-user-images\image-20220910173604559.png" alt="image-20220910173604559" style="zoom: 33%;" />

包含跳转、分页、显示搜索结果与搜索性能等功能。

###### 博客正文页：

<img src="C:\Users\AQ\AppData\Roaming\Typora\typora-user-images\image-20220910173716019.png" alt="image-20220910173716019" style="zoom:33%;" />

左侧为正文，右侧为博客作者相关信息与导航栏。

<img src="C:\Users\AQ\AppData\Roaming\Typora\typora-user-images\image-20220910173841571.png" alt="image-20220910173841571" style="zoom:33%;" />

页面末尾设有评论区，可用于评论。

###### 分类列表页：

<img src="C:\Users\AQ\AppData\Roaming\Typora\typora-user-images\image-20220910173947717.png" alt="image-20220910173947717" style="zoom:67%;" />

鼠标放在页面上方导航栏，可看到吧不同标签下的博客数量。点击进入列表页：

<img src="C:\Users\AQ\AppData\Roaming\Typora\typora-user-images\image-20220910174057397.png" alt="image-20220910174057397" style="zoom:33%;" />

形式和首页较为相似。

#### 三、关于页面链接

本app的view.py文件如图所示：

<img src="C:\Users\AQ\AppData\Roaming\Typora\typora-user-images\image-20220910175219769.png" alt="image-20220910175219769" style="zoom: 67%;" />

由于一开始不够熟悉，分类页设了太多函数，但其实不用这么多……不过既然写都写了那就这样吧。

<img src="C:\Users\AQ\AppData\Roaming\Typora\typora-user-images\image-20220910175319744.png" alt="image-20220910175319744" style="zoom:50%;" />

urls.py如图所示，均设置了name方便链接重定向。

#### 四、关于搜索

比较简单的filter结构：（先筛标签再筛内容）所以有点慢……

<img src="C:\Users\AQ\AppData\Roaming\Typora\typora-user-images\image-20220910175434187.png" alt="image-20220910175434187" style="zoom: 67%;" />

![image-20220910175521409](C:\Users\AQ\AppData\Roaming\Typora\typora-user-images\image-20220910175521409.png)