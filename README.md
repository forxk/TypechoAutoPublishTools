
# TypechoAutoPublishTools

Typecho文章自动发布工具，使用 Github Actions 自动更新文章到 Typecho

这个项目可以让你用Markdown写博客，push更新到Github后，Github Actions自动将文章更新到Typecho，并将Typecho站的文章索引更新到Github仓库的README.md，供搜索引擎收录。

参考了 [WordPressXMLRPCTools](https://github.com/zhaoolee/WordPressXMLRPCTools/)，基于Github Actions + Python3.10 + PyTypecho + XMLRPC 实现的文章自动检查及发布

![Static Badge](https://img.shields.io/badge/Python-3.10-blue)
![Static Badge](https://img.shields.io/badge/PyTypecho-2.1.0-blue)
![Static Badge](https://img.shields.io/badge/Typecho-1.2.1-blue)
![Static Badge](https://img.shields.io/badge/XMLRPC-green)

## Features

- 自动检查项目内的所有文章，新文章自动发布，旧文章比对MD5自动更新

- 自动更新文章发布链接到项目仓库，增加google收录

## Quick Start

### 本地运行

1. 下载项目，然后安装 Python 3.10、Pip、Pipenv  

```shell
git clone https://github.com/Thinker-Joe/TypechoAutoPublishTools

pip3 install pipenv
```

2. 安装依赖  

```shell
pipenv install
```

3. 本地运行配置  

复制根目录下的 config.txt 为 local_config.txt ，并按说明修改配置里的地址、用户名、密码

```json
{
    "USERNAME": "填写登录后台的用户名",
    "PASSWORD": "填写登录后台的密码",
    "XMLRPC_PHP": "填写xmlrpc地址信息，如 https://blog.yycdev.com/action/xmlrpc"
}
```

4. 检查更新及发布文章

```shell
pipenv run build
```

命令运行成功后即可在Typecho后台即可看到新发布或更新后的文章

### Github Actions运行

1. 配置 Github Secrets

Settings > Security > Secrets and variables > Actions

在该菜单下添加 PASSWORD、USERNAME、XMLRPC_PHP 这三个配置参数，参数值参考项目里的config.txt

![](https://img.yycdev.com/202403041737177.png)

2. 配置完成后，在 _post 文件夹新建文件并提交保存更新到仓库触发 Github Action 自动运行

![](https://img.yycdev.com/202403041742805.png)

3. Action运行成功后，在Typecho后台即可看到新发布或更新后的文章

### 新建文章

在 _post 目录下新建 后缀为 .md 的markdown文件即可

### 文章格式

```yaml
---
title: 标题
tags: 
- 标签1
- 标签2
categories:
- 分类1
- 分类二
---

正文开始...
```

样例参考: https://github.com/Thinker-Joe/TypechoAutoPublishTools/blob/main/_posts/2020-01-18-blog.md

### 固定链接

固定链接参考了 简书 的文章url形式，域名后加 /p/ , 再加英文文件名，只要不改变英文文件名，文章就有固定的链接

> 例子：_posts 目录下新建一个 2020-01-18-blog.md 文件，同步后的文章url为 https://xxx.com/p/2020-01-18-blog/

同时在Typecho后台也要配置好文章的永久链接设置
> 管理后台>设置>永久链接>自定义文章路径  
> 个性化定义：/p/{slug}.html

![](https://img.yycdev.com/202403041751952.png)

## 感谢

- [WordPressXMLRPCTools](https://github.com/zhaoolee/WordPressXMLRPCTools/)

- [PyTypecho](https://github.com/veoco/PyTypecho)

- [Typecho](https://typecho.org/)

---start---
## 目录(2024年12月19日更新)
[[XiuRen秀人网]第9424期Zoe柚柚写真](https://ilovese.xyz/index.php/p/zlR4ngR0jTK9/)

[[XiuRen秀人网]第9499期初梦瑶写真](https://ilovese.xyz/index.php/p/zPkZ8QAO13rV/)

[[XiuRen秀人网]第9406期杏子写真](https://ilovese.xyz/index.php/p/xot2afDvr3sU/)

[[XiuRen秀人网]第9386期小逗逗写真](https://ilovese.xyz/index.php/p/xeWKeo7cIlrv/)

[[XiuRen秀人网]第9519期杨晨晨写真](https://ilovese.xyz/index.php/p/xaIG80f5cvab/)

[[XiuRen秀人网]第9447期小肉肉咪写真](https://ilovese.xyz/index.php/p/xZBsKh1iq80Q/)

[[XiuRen秀人网]第9411期周妍希写真](https://ilovese.xyz/index.php/p/xMu6q7hvwzs6/)

[[XiuRen秀人网]第9388期糖糖写真](https://ilovese.xyz/index.php/p/wxPSoKeY8QUw/)

[[XiuRen秀人网]第9419期Erikaki写真](https://ilovese.xyz/index.php/p/vlgpRBUkurX0/)

[[XiuRen秀人网]第9463期唐安琪写真](https://ilovese.xyz/index.php/p/vh0rLarGO9Nd/)

[[XiuRen秀人网]第9365期大美妞儿写真](https://ilovese.xyz/index.php/p/vL3cQ8u0TiWh/)

[[XiuRen秀人网]第9505期娜比写真](https://ilovese.xyz/index.php/p/uNe4lY87FNGB/)

[[XiuRen秀人网]第9503期糖糖写真](https://ilovese.xyz/index.php/p/u0ur9H1Ai4wp/)

[[XiuRen秀人网]第9510期白洁写真](https://ilovese.xyz/index.php/p/trPPPl88L2Oz/)

[[XiuRen秀人网]第9493期小逗逗写真](https://ilovese.xyz/index.php/p/t7AwstyEIa1v/)

[[XiuRen秀人网]第9475期绮里嘉写真](https://ilovese.xyz/index.php/p/swQgPK8kbwhX/)

[[XiuRen秀人网]第9491期唐翩翩写真](https://ilovese.xyz/index.php/p/sYJaLlDEUuh8/)

[[XiuRen秀人网]第9393期风景尤美写真](https://ilovese.xyz/index.php/p/ruu1zQnOrHTG/)

[[XiuRen秀人网]第9533期沈思怡写真](https://ilovese.xyz/index.php/p/rD6spITw2aOx/)

[[XiuRen秀人网]第9397期糯美子写真](https://ilovese.xyz/index.php/p/rBGweLWNSF6H/)

[[XiuRen秀人网]第9466期伊丽莎有点白写真](https://ilovese.xyz/index.php/p/qpF6PtktABHC/)

[[XiuRen秀人网]第9486期桃妖夭写真](https://ilovese.xyz/index.php/p/qi36myhqIlGu/)

[[XiuRen秀人网]第9381期玥儿玥写真](https://ilovese.xyz/index.php/p/qL6N4sAeb28r/)

[[XiuRen秀人网]第9410期白洁写真](https://ilovese.xyz/index.php/p/p20lvAGGg0Pi/)

[[XiuRen秀人网]第9428期林星阑写真](https://ilovese.xyz/index.php/p/ozjjH9IOfQlq/)

[[XiuRen秀人网]第9439期余虞酱写真](https://ilovese.xyz/index.php/p/oami0iWYf25Z/)

[[XiuRen秀人网]第9368期初梦瑶写真](https://ilovese.xyz/index.php/p/oFoAag3EtlY4/)

[[XiuRen秀人网]第9487期林星阑写真](https://ilovese.xyz/index.php/p/npGl7GiRgRu6/)

[[XiuRen秀人网]第9382期绮里嘉写真](https://ilovese.xyz/index.php/p/nOwkJFjTe5OQ/)

[[XiuRen秀人网]第9524期桃妖夭写真](https://ilovese.xyz/index.php/p/nKxMtOuKeUee/)

[[XiuRen秀人网]第9532期陈芊儿写真](https://ilovese.xyz/index.php/p/mEQBSHJOnm9i/)

[[XiuRen秀人网]第9448期刘婷婷写真](https://ilovese.xyz/index.php/p/lpmTVHW6MNOY/)

[[XiuRen秀人网]第9436期安然写真](https://ilovese.xyz/index.php/p/lUaeZOftoIjn/)

[[XiuRen秀人网]第9482期徐莉芝写真](https://ilovese.xyz/index.php/p/lSTkqfYXaNac/)

[[XiuRen秀人网]第9536期玥儿玥写真](https://ilovese.xyz/index.php/p/lHmRzMmDBcDd/)

[[XiuRen秀人网]第9476期香澄在东京写真](https://ilovese.xyz/index.php/p/lGd38UND9005/)

[[XiuRen秀人网]第9374期Zoe柚柚写真](https://ilovese.xyz/index.php/p/kxyhGw6owUmM/)

[[XiuRen秀人网]第9453期柚柚小奶瓶写真](https://ilovese.xyz/index.php/p/kTyEBUtTztgo/)

[[XiuRen秀人网]第9492期鱼子酱写真](https://ilovese.xyz/index.php/p/hUeRBIh8chSF/)

[[XiuRen秀人网]第9497期FE写真](https://ilovese.xyz/index.php/p/hQGKswf6KOZZ/)

[[XiuRen秀人网]第9441期Lingyu69写真](https://ilovese.xyz/index.php/p/hGFoK5793VLm/)

[[XiuRen秀人网]第9405期凯竹写真](https://ilovese.xyz/index.php/p/gTb4uSlmjhpq/)

[[XiuRen秀人网]第9404期Lingyu69写真](https://ilovese.xyz/index.php/p/gNGdj51zXvyZ/)

[[XiuRen秀人网]第9479期陈小花写真](https://ilovese.xyz/index.php/p/gE8BvDhybwhr/)

[[XiuRen秀人网]第9465期Zoe柚柚写真](https://ilovese.xyz/index.php/p/eGRHnTc5S9N6/)

[[XiuRen秀人网]第9539期姚若兮写真](https://ilovese.xyz/index.php/p/dgfGFHehSi1y/)

[[XiuRen秀人网]第9470期杨晨晨写真](https://ilovese.xyz/index.php/p/cO1OJdk1mpCx/)

[[XiuRen秀人网]第9414期田冰冰写真](https://ilovese.xyz/index.php/p/blVOdd5QlfF6/)

[[XiuRen秀人网]第9376期小薯条写真](https://ilovese.xyz/index.php/p/bjJZ8MzwXYfJ/)

[[XiuRen秀人网]第9516期潘多拉写真](https://ilovese.xyz/index.php/p/b5qi1TSe4TVw/)

[[XiuRen秀人网]第9364期潘多拉哦写真](https://ilovese.xyz/index.php/p/allfls7DyGVl/)

[[XiuRen秀人网]第9538期唐安琪写真](https://ilovese.xyz/index.php/p/ZgSi97w26KpW/)

[[XiuRen秀人网]第9535期糯美子写真](https://ilovese.xyz/index.php/p/ZJKg5xRw5Cmi/)

[[XiuRen秀人网]第9395期模特合集写真](https://ilovese.xyz/index.php/p/Z789ttR0aBpY/)

[[XiuRen秀人网]第9512期凯竹写真](https://ilovese.xyz/index.php/p/YzdHUgf5szIY/)

[[XiuRen秀人网]第9543期安然写真](https://ilovese.xyz/index.php/p/YvMQdQKubxXq/)

[[XiuRen秀人网]第9422期鱼子酱写真](https://ilovese.xyz/index.php/p/YJz4mpmKcoC5/)

[[XiuRen秀人网]第9474期杏子写真](https://ilovese.xyz/index.php/p/YD5ZUYoJfHDZ/)

[[XiuRen秀人网]第9481期刘婷婷写真](https://ilovese.xyz/index.php/p/XqptCvVBHsnR/)

[[XiuRen秀人网]第9496期沈思怡写真](https://ilovese.xyz/index.php/p/X2q4NRID74ow/)

[[XiuRen秀人网]第9489期小薯条写真](https://ilovese.xyz/index.php/p/Wou35sJqDqZi/)

[[XiuRen秀人网]第9385期唐翩翩写真](https://ilovese.xyz/index.php/p/WfYFCshkPuFQ/)

[[XiuRen秀人网]第9391期诗诗写真](https://ilovese.xyz/index.php/p/WciyvBnaYgFy/)

[[XiuRen秀人网]第9484期Lucky写真](https://ilovese.xyz/index.php/p/WbTEzMaosNQz/)

[[XiuRen秀人网]第9412期徐莉芝写真](https://ilovese.xyz/index.php/p/WY6ctVfJ7jZD/)

[[XiuRen秀人网]第9467期蛋蛋宝写真](https://ilovese.xyz/index.php/p/W27Rd5mcDZIX/)

[[XiuRen秀人网]第9449期徐莉芝写真](https://ilovese.xyz/index.php/p/VdIvmUl5pvz6/)

[[XiuRen秀人网]第9517期模特合集写真](https://ilovese.xyz/index.php/p/VTQe6hs6KDs1/)

[[XiuRen秀人网]第9490期杨晨晨写真](https://ilovese.xyz/index.php/p/UxM50KoVKI2t/)

[[XiuRen秀人网]第9398期娜比写真](https://ilovese.xyz/index.php/p/Ua5FS6jjOoWt/)

[[XiuRen秀人网]第9437期小童颜写真](https://ilovese.xyz/index.php/p/USWjr9QqP2Jf/)

[[XiuRen秀人网]第9457期鱼子酱写真](https://ilovese.xyz/index.php/p/TwgaGdDUA3jA/)

[[XiuRen秀人网]第9502期Zoe柚柚写真](https://ilovese.xyz/index.php/p/TsEbSGwQmSqb/)

[[XiuRen秀人网]第9506期安然写真](https://ilovese.xyz/index.php/p/Tr6w7dmEklV3/)

[[XiuRen秀人网]第9483期陆萱萱写真](https://ilovese.xyz/index.php/p/Tg3GQGU1UHia/)

[[XiuRen秀人网]第9495期曼柔写真](https://ilovese.xyz/index.php/p/TdgRuC9NPYYD/)

[[XiuRen秀人网]第9473期糖糖写真](https://ilovese.xyz/index.php/p/SCpYzj5hf1Jv/)

[[XiuRen秀人网]第9500期唐安琪写真](https://ilovese.xyz/index.php/p/R3mlYSVDJcba/)

[[XiuRen秀人网]第9527期诗诗写真](https://ilovese.xyz/index.php/p/QmMiQaKTgUZz/)

[[XiuRen秀人网]第9390期梦心玥写真](https://ilovese.xyz/index.php/p/QCGePAlrCw7g/)

[[XiuRen秀人网]第9472期方子萱写真](https://ilovese.xyz/index.php/p/PUu2x1PHGttq/)

[[XiuRen秀人网]第9431期养乐多写真](https://ilovese.xyz/index.php/p/PTLyoPXhM81r/)

[[XiuRen秀人网]第9451期Lucky写真](https://ilovese.xyz/index.php/p/POW9IzOfMcmn/)

[[XiuRen秀人网]第9423期小兔纯纯写真](https://ilovese.xyz/index.php/p/PIq2SCznDlbq/)

[[XiuRen秀人网]第9460期奶茹写真](https://ilovese.xyz/index.php/p/OrzGEr7hOoat/)

[[XiuRen秀人网]第9371期艺艺写真](https://ilovese.xyz/index.php/p/OXdRjmqzWO9v/)

[[XiuRen秀人网]第9468期梦心玥写真](https://ilovese.xyz/index.php/p/OSwmyJShRJIr/)

[[XiuRen秀人网]第9427期小蛮妖写真](https://ilovese.xyz/index.php/p/OMeNRsu0BcIe/)

[[XiuRen秀人网]第9471期果果Nikki写真](https://ilovese.xyz/index.php/p/MmFqxh8DyN62/)

[[XiuRen秀人网]第9541期Lingyu69写真](https://ilovese.xyz/index.php/p/KSoPv7u8fhi7/)

[[XiuRen秀人网]第9542期方子萱写真](https://ilovese.xyz/index.php/p/K0OBGR486943/)

[[XiuRen秀人网]第9373期甜妮写真](https://ilovese.xyz/index.php/p/JxUejy99vmeN/)

[[XiuRen秀人网]第9477期美少女写真](https://ilovese.xyz/index.php/p/JoTK0ZuE3X0h/)

[[XiuRen秀人网]第9392期唐安琪写真](https://ilovese.xyz/index.php/p/JfjsYhsXorvU/)

[[XiuRen秀人网]第9452期甜妮写真](https://ilovese.xyz/index.php/p/IWRmhpbUKGLo/)

[[XiuRen秀人网]第9443期娜比写真](https://ilovese.xyz/index.php/p/HYdIlfINPexA/)

[[XiuRen秀人网]第9464期奶芙乔乔写真](https://ilovese.xyz/index.php/p/H65Rv9PFp0bC/)

[[XiuRen秀人网]第9455期玥儿玥写真](https://ilovese.xyz/index.php/p/FYifTrWzqPJS/)

[[XiuRen秀人网]第9507期菲菲吃不胖写真](https://ilovese.xyz/index.php/p/FK2GILeUBS0B/)

[[XiuRen秀人网]第9369期杏子写真](https://ilovese.xyz/index.php/p/ExkwmxvSDbEM/)

[[XiuRen秀人网]第9511期拍黄瓜写真](https://ilovese.xyz/index.php/p/EuOvobkrchNP/)

[[XiuRen秀人网]第9407期尹菲写真](https://ilovese.xyz/index.php/p/EXSTQLsqU3YK/)

[[XiuRen秀人网]第9383期Erikaki写真](https://ilovese.xyz/index.php/p/ELvm4f0HD2n9/)

[[XiuRen秀人网]第9408期拍黄瓜写真](https://ilovese.xyz/index.php/p/EF4VNMEFn63U/)

[[XiuRen秀人网]第9402期Zoe柚柚写真](https://ilovese.xyz/index.php/p/DH3nJCb0INYU/)

[[XiuRen秀人网]第9418期玥儿玥写真](https://ilovese.xyz/index.php/p/CsjlO5EmSuez/)

[[XiuRen秀人网]第9520期徐莉芝写真](https://ilovese.xyz/index.php/p/CDAzDbNN2rCM/)

[[XiuRen秀人网]第9530期小逗逗写真](https://ilovese.xyz/index.php/p/BXgXIVNcAuNd/)

[[XiuRen秀人网]第9429期唐安琪写真](https://ilovese.xyz/index.php/p/BBdtN81vvUhu/)

[[XiuRen秀人网]第9380期林星阑写真](https://ilovese.xyz/index.php/p/AiUexuryTNtx/)

[[XiuRen秀人网]第9435期凯竹写真](https://ilovese.xyz/index.php/p/9ng5NbvcBxAs/)

[[XiuRen秀人网]第9379期软软酱写真](https://ilovese.xyz/index.php/p/9dEJ8p8w5AwE/)

[[XiuRen秀人网]第9485期王雨纯写真](https://ilovese.xyz/index.php/p/9LA1Q5CHURsg/)

[[XiuRen秀人网]第9416期麻布学妹写真](https://ilovese.xyz/index.php/p/7uzsQ6OeQ5Ef/)

[[XiuRen秀人网]第9401期金允珍写真](https://ilovese.xyz/index.php/p/7CKmZtjuj9Vi/)

[[XiuRen秀人网]第9461期沈思怡写真](https://ilovese.xyz/index.php/p/6yzEVjKYdFah/)

[[XiuRen秀人网]第9446期潘多拉写真](https://ilovese.xyz/index.php/p/6x7NjNz4F4lf/)

[[XiuRen秀人网]第9523期心妍小公主写真](https://ilovese.xyz/index.php/p/6SYSaA2Ap95N/)

[[XiuRen秀人网]第9421期杨晨晨写真](https://ilovese.xyz/index.php/p/5rHDJNIRTJKh/)

[[XiuRen秀人网]第9528期林星阑写真](https://ilovese.xyz/index.php/p/5bcNkGmkVbT4/)

[[XiuRen秀人网]第9456期杨晨晨写真](https://ilovese.xyz/index.php/p/5PKUunKOAJfR/)

[[XiuRen秀人网]第9525期妲己写真](https://ilovese.xyz/index.php/p/4v6pMTXE6poC/)

[[XiuRen秀人网]第9526期梦心玥写真](https://ilovese.xyz/index.php/p/4QB4zBg3dWPu/)

[[XiuRen秀人网]第9469期安然写真](https://ilovese.xyz/index.php/p/4IIt5mX0CqVR/)

[[XiuRen秀人网]第9377期陆萱萱写真](https://ilovese.xyz/index.php/p/3pGSkpA3C45E/)

[[XiuRen秀人网]第9384期杨晨晨写真](https://ilovese.xyz/index.php/p/3TZLd39qvKKo/)

[[XiuRen秀人网]第9478期田冰冰写真](https://ilovese.xyz/index.php/p/2w1f5AEazMMK/)

[[XiuRen秀人网]第9426期初梦瑶写真](https://ilovese.xyz/index.php/p/2onYuiREgpqn/)

[[XiuRen秀人网]第9508期奶芙乔乔写真](https://ilovese.xyz/index.php/p/2ZSIx7Erz3eF/)

[[XiuRen秀人网]第9400期果果写真](https://ilovese.xyz/index.php/p/2T8uJvPZGyUI/)

[[XiuRen秀人网]第9370期王伊纯写真](https://ilovese.xyz/index.php/p/1OVI2cFK9Mos/)

[[XiuRen秀人网]第9522期李金金写真](https://ilovese.xyz/index.php/p/13DIPYmXrruk/)

[[XiuRen秀人网]第9409期陈小花写真](https://ilovese.xyz/index.php/p/0y4n8HZyuUyD/)

[[XiuRen秀人网]第9417期妲己写真](https://ilovese.xyz/index.php/p/0wCIazL0wyLc/)

[[XiuRen秀人网]第9389期Lucky写真](https://ilovese.xyz/index.php/p/0ulhi7qXBlpv/)

[[XiuRen秀人网]第9378期菲菲吃不胖写真](https://ilovese.xyz/index.php/p/0jFIx5wmKJl6/)

[[XiuRen秀人网]第9509期方子萱写真](https://ilovese.xyz/index.php/p/0W2OhjpmMnUA/)

---end---