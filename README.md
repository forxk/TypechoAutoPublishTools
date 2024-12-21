
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
## 目录(2024年12月21日更新)
[[MFStar模范学院]第542期youOvOyou写真](https://ilovese.xyz/index.php/p/zjMV9TZ6/)

[[MFStar模范学院]第527期李颖煊写真](https://ilovese.xyz/index.php/p/zRZGpa3a/)

[[MFStar模范学院]第618期伊诺写真](https://ilovese.xyz/index.php/p/yveiaDUD/)

[[MFStar模范学院]第622期揉揉肉肉写真](https://ilovese.xyz/index.php/p/xPQaFYjd/)

[[MFStar模范学院]第544期徐媛媛写真](https://ilovese.xyz/index.php/p/xJfLHZCv/)

[[MFStar模范学院]第591期汐汐爱吃草莓写真](https://ilovese.xyz/index.php/p/x0xAwepq/)

[[MFStar模范学院]第599期茜茜写真](https://ilovese.xyz/index.php/p/wtrRdg5D/)

[[MFStar模范学院]第476期yoo优优写真](https://ilovese.xyz/index.php/p/wZWa3O9a/)

[[MFStar模范学院]第549期白茹雪写真](https://ilovese.xyz/index.php/p/wYUuX1Mn/)

[[MFStar模范学院]第522期qiqi写真](https://ilovese.xyz/index.php/p/vhWlg2zs/)

[[MFStar模范学院]第628期雪糕写真](https://ilovese.xyz/index.php/p/vfyvrVfX/)

[[MFStar模范学院]第526期一颗甜蛋黄写真](https://ilovese.xyz/index.php/p/vcUqIkva/)

[[MFStar模范学院]第459期母崽崽写真](https://ilovese.xyz/index.php/p/uaw20Wlz/)

[[MFStar模范学院]第534期蔡文钰写真](https://ilovese.xyz/index.php/p/tismFqWc/)

[[MFStar模范学院]第492期芊澄写真](https://ilovese.xyz/index.php/p/ssBdOm92/)

[[MFStar模范学院]第633期董林越写真](https://ilovese.xyz/index.php/p/qX1uaDKT/)

[[MFStar模范学院]第548期小果冻儿写真](https://ilovese.xyz/index.php/p/qV36qLBq/)

[[MFStar模范学院]第528期一颗甜蛋黄写真](https://ilovese.xyz/index.php/p/qF9ifDpN/)

[[MFStar模范学院]第596期樱桃小犊子写真](https://ilovese.xyz/index.php/p/pTQpZhgh/)

[[MFStar模范学院]第613期杨可可写真](https://ilovese.xyz/index.php/p/ovmg3F6y/)

[[MFStar模范学院]第566期露露写真](https://ilovese.xyz/index.php/p/oS7ZV6Nb/)

[[MFStar模范学院]第532期一颗甜蛋黄写真](https://ilovese.xyz/index.php/p/oI5ENx47/)

[[MFStar模范学院]第600期雪糕写真](https://ilovese.xyz/index.php/p/mgOi2O4T/)

[[MFStar模范学院]第463期小波多写真](https://ilovese.xyz/index.php/p/mNvZyYED/)

[[MFStar模范学院]第619期李雅柔写真](https://ilovese.xyz/index.php/p/m3iJhNhU/)

[[MFStar模范学院]第482期人间荒糖写真](https://ilovese.xyz/index.php/p/kzg9SBpl/)

[[MFStar模范学院]第602期汐汐爱吃草莓写真](https://ilovese.xyz/index.php/p/kwG1IXts/)

[[MFStar模范学院]第572期吴思晚写真](https://ilovese.xyz/index.php/p/joImBCPo/)

[[MFStar模范学院]第574期樱桃小犊子写真](https://ilovese.xyz/index.php/p/inZB9TjW/)

[[MFStar模范学院]第623期星萌写真](https://ilovese.xyz/index.php/p/iTCNXSsQ/)

[[MFStar模范学院]第515期奶瓶子写真](https://ilovese.xyz/index.php/p/hzcxZlW9/)

[[MFStar模范学院]第461期薛琪琪写真](https://ilovese.xyz/index.php/p/hapowESD/)

[[MFStar模范学院]第464期安琪Yee写真](https://ilovese.xyz/index.php/p/hXt4SMWo/)

[[MFStar模范学院]第559期韩好甜写真](https://ilovese.xyz/index.php/p/hAEXR5no/)

[[MFStar模范学院]第547期徐媛媛写真](https://ilovese.xyz/index.php/p/h31m1BwY/)

[[MFStar模范学院]第490期水水er写真](https://ilovese.xyz/index.php/p/fy80PJep/)

[[MFStar模范学院]第489期小果冻儿写真](https://ilovese.xyz/index.php/p/fj3CF9iI/)

[[MFStar模范学院]第631期杨可可写真](https://ilovese.xyz/index.php/p/fXNPzlrh/)

[[MFStar模范学院]第481期春药儿写真](https://ilovese.xyz/index.php/p/fLbnBODR/)

[[MFStar模范学院]第511期揉揉肉肉写真](https://ilovese.xyz/index.php/p/f70j7wZx/)

[[MFStar模范学院]第537期王蜜写真](https://ilovese.xyz/index.php/p/eXhszbwa/)

[[MFStar模范学院]第512期墨韩写真](https://ilovese.xyz/index.php/p/eVxI8Wsk/)

[[MFStar模范学院]第529期苏西写真](https://ilovese.xyz/index.php/p/e57Cee4I/)

[[MFStar模范学院]第493期玉兔写真](https://ilovese.xyz/index.php/p/dyDfss61/)

[[MFStar模范学院]第578期Ai西西里写真](https://ilovese.xyz/index.php/p/d4UHevFT/)

[[MFStar模范学院]第551期吴雪瑶写真](https://ilovese.xyz/index.php/p/cy3yG3of/)

[[MFStar模范学院]第582期白茹雪写真](https://ilovese.xyz/index.php/p/cDfpzKsV/)

[[MFStar模范学院]第499期人间荒糖写真](https://ilovese.xyz/index.php/p/bGdzejC4/)

[[MFStar模范学院]第586期加朵写真](https://ilovese.xyz/index.php/p/b86lGhNh/)

[[MFStar模范学院]第518期揉揉肉肉写真](https://ilovese.xyz/index.php/p/b05Qafu4/)

[[MFStar模范学院]第521期墨韩写真](https://ilovese.xyz/index.php/p/aXOckhwr/)

[[MFStar模范学院]第565期小米写真](https://ilovese.xyz/index.php/p/aPA21LyQ/)

[[MFStar模范学院]第487期白茹雪写真](https://ilovese.xyz/index.php/p/aEpqPeP7/)

[[MFStar模范学院]第553期小果冻儿写真](https://ilovese.xyz/index.php/p/Ytp7P0Tt/)

[[MFStar模范学院]第494期婠婠么写真](https://ilovese.xyz/index.php/p/YWVTWgyk/)

[[MFStar模范学院]第612期樱桃小犊子写真](https://ilovese.xyz/index.php/p/YPIW9AQK/)

[[MFStar模范学院]第611期王楚璇写真](https://ilovese.xyz/index.php/p/YOne6vWC/)

[[MFStar模范学院]第583期露露写真](https://ilovese.xyz/index.php/p/XGiVJALn/)

[[MFStar模范学院]第523期一颗甜蛋黄写真](https://ilovese.xyz/index.php/p/XFEIkvA2/)

[[MFStar模范学院]第590期小樱花写真](https://ilovese.xyz/index.php/p/W1ChVh0y/)

[[MFStar模范学院]第479期模特合集写真](https://ilovese.xyz/index.php/p/VtG8YoqC/)

[[MFStar模范学院]第474期人间荒糖写真](https://ilovese.xyz/index.php/p/TjwwTJfo/)

[[MFStar模范学院]第477期星萌写真](https://ilovese.xyz/index.php/p/TX25fWU5/)

[[MFStar模范学院]第539期王蜜写真](https://ilovese.xyz/index.php/p/SAMAEEZg/)

[[MFStar模范学院]第560期吴思晚写真](https://ilovese.xyz/index.php/p/S6hyMVZL/)

[[MFStar模范学院]第536期佳佳崽崽写真](https://ilovese.xyz/index.php/p/RyAGoseV/)

[[MFStar模范学院]第507期模特合集写真](https://ilovese.xyz/index.php/p/Ro7wEHBA/)

[[MFStar模范学院]第486期模特合集写真](https://ilovese.xyz/index.php/p/RA11C3yH/)

[[MFStar模范学院]第541期夏沫沫写真](https://ilovese.xyz/index.php/p/QjD8oljm/)

[[MFStar模范学院]第538期模特合集写真](https://ilovese.xyz/index.php/p/QeMK7Ws4/)

[[MFStar模范学院]第457期水水er写真](https://ilovese.xyz/index.php/p/Qb8G3dSE/)

[[MFStar模范学院]第567期白茹雪写真](https://ilovese.xyz/index.php/p/QY8Nz4gU/)

[[MFStar模范学院]第550期优优写真](https://ilovese.xyz/index.php/p/QSwAwnYt/)

[[MFStar模范学院]第501期NaNa_baby写真](https://ilovese.xyz/index.php/p/QRRzMtxX/)

[[MFStar模范学院]第605期大美妞儿写真](https://ilovese.xyz/index.php/p/QMxCDrLM/)

[[MFStar模范学院]第472期玉兔miki写真](https://ilovese.xyz/index.php/p/QLefacDt/)

[[MFStar模范学院]第594期露露写真](https://ilovese.xyz/index.php/p/QEzMYpAW/)

[[MFStar模范学院]第579期白茹雪写真](https://ilovese.xyz/index.php/p/Q3jtjCj3/)

[[MFStar模范学院]第564期小果冻儿写真](https://ilovese.xyz/index.php/p/PWb7WWZy/)

[[MFStar模范学院]第498期桃香子写真](https://ilovese.xyz/index.php/p/PSzwp88s/)

[[MFStar模范学院]第520期米漫池写真](https://ilovese.xyz/index.php/p/ObrFbahn/)

[[MFStar模范学院]第576期白茹雪写真](https://ilovese.xyz/index.php/p/ORk6Laqb/)

[[MFStar模范学院]第505期白茹雪写真](https://ilovese.xyz/index.php/p/N3hh5W75/)

[[MFStar模范学院]第470期母崽崽写真](https://ilovese.xyz/index.php/p/Mtb60aMx/)

[[MFStar模范学院]第634期温柔的柔写真](https://ilovese.xyz/index.php/p/MhXBZgbM/)

[[MFStar模范学院]第587期露露写真](https://ilovese.xyz/index.php/p/Me6Llkzl/)

[[MFStar模范学院]第467期小果冻儿写真](https://ilovese.xyz/index.php/p/Lj2VzboN/)

[[MFStar模范学院]第514期米漫池写真](https://ilovese.xyz/index.php/p/LCDMOdVK/)

[[MFStar模范学院]第597期星萌写真](https://ilovese.xyz/index.php/p/JyKfyowr/)

[[MFStar模范学院]第471期yoo优优写真](https://ilovese.xyz/index.php/p/JcwnkMYl/)

[[MFStar模范学院]第509期方子萱写真](https://ilovese.xyz/index.php/p/JcVea8vf/)

[[MFStar模范学院]第588期雪雪琪写真](https://ilovese.xyz/index.php/p/J4Y0T3z8/)

[[MFStar模范学院]第621期水塔塔写真](https://ilovese.xyz/index.php/p/Ifmei0h6/)

[[MFStar模范学院]第533期77qiqi写真](https://ilovese.xyz/index.php/p/ILw0D8pV/)

[[MFStar模范学院]第525期李颖煊写真](https://ilovese.xyz/index.php/p/HuqGlExg/)

[[MFStar模范学院]第516期77qiqi写真](https://ilovese.xyz/index.php/p/Hh7YX2xJ/)

[[MFStar模范学院]第508期星萌写真](https://ilovese.xyz/index.php/p/HRlCOULl/)

[[MFStar模范学院]第519期吴雪瑶写真](https://ilovese.xyz/index.php/p/HCROzSI0/)

[[MFStar模范学院]第465期婠婠么写真](https://ilovese.xyz/index.php/p/H13SyzXL/)

[[MFStar模范学院]第568期露露写真](https://ilovese.xyz/index.php/p/G9Fi7C0Z/)

[[MFStar模范学院]第478期人间荒糖写真](https://ilovese.xyz/index.php/p/FnsEuZto/)

[[MFStar模范学院]第557期人间荒糖写真](https://ilovese.xyz/index.php/p/FkN3jo0J/)

[[MFStar模范学院]第589期yoo优优写真](https://ilovese.xyz/index.php/p/FPiuT2Fb/)

[[MFStar模范学院]第458期郑颖姗写真](https://ilovese.xyz/index.php/p/FO1IOBeZ/)

[[MFStar模范学院]第455期水水er写真](https://ilovese.xyz/index.php/p/EcFGOymX/)

[[MFStar模范学院]第595期汐汐爱吃草莓写真](https://ilovese.xyz/index.php/p/DibeZmqt/)

[[MFStar模范学院]第480期薇薇写真](https://ilovese.xyz/index.php/p/DZ7wGYkH/)

[[MFStar模范学院]第485期yoo优优写真](https://ilovese.xyz/index.php/p/C34zqKFQ/)

[[MFStar模范学院]第475期崔灿写真](https://ilovese.xyz/index.php/p/ByMwlc8K/)

[[MFStar模范学院]第466期如歌写真](https://ilovese.xyz/index.php/p/B4J92MxA/)

[[MFStar模范学院]第554期羽仁鹿写真](https://ilovese.xyz/index.php/p/AuSxMYLR/)

[[MFStar模范学院]第609期汐汐爱吃草莓写真](https://ilovese.xyz/index.php/p/9xFeGAcI/)

[[MFStar模范学院]第617期文静儿写真](https://ilovese.xyz/index.php/p/9tKXJso6/)

[[MFStar模范学院]第632期米亚写真](https://ilovese.xyz/index.php/p/9cYOEdi2/)

[[MFStar模范学院]第604期雪糕写真](https://ilovese.xyz/index.php/p/8sZ5clVb/)

[[MFStar模范学院]第540期蔡文钰写真](https://ilovese.xyz/index.php/p/8Hbnv7aA/)

[[MFStar模范学院]第625期柒喜小写真](https://ilovese.xyz/index.php/p/8HLp3ApY/)

[[MFStar模范学院]第558期白茹雪写真](https://ilovese.xyz/index.php/p/7lv0p08Y/)

[[MFStar模范学院]第614期温心怡写真](https://ilovese.xyz/index.php/p/7TxTLORL/)

[[MFStar模范学院]第620期大美妞儿写真](https://ilovese.xyz/index.php/p/7QrV7nMW/)

[[MFStar模范学院]第570期yoo优优写真](https://ilovese.xyz/index.php/p/7GNu4S9K/)

[[MFStar模范学院]第531期苏西写真](https://ilovese.xyz/index.php/p/6hIRsuTN/)

[[MFStar模范学院]第603期加朵写真](https://ilovese.xyz/index.php/p/6NF55k55/)

[[MFStar模范学院]第543期甜筒晓彤写真](https://ilovese.xyz/index.php/p/5xoEOpCH/)

[[MFStar模范学院]第608期茜茜写真](https://ilovese.xyz/index.php/p/5spXs3cs/)

[[MFStar模范学院]第575期露露写真](https://ilovese.xyz/index.php/p/4wWJHnE5/)

[[MFStar模范学院]第483期墨韩写真](https://ilovese.xyz/index.php/p/467gb7tU/)

[[MFStar模范学院]第496期奶瓶子写真](https://ilovese.xyz/index.php/p/45LfBQy6/)

[[MFStar模范学院]第593期雪糕写真](https://ilovese.xyz/index.php/p/3ND4OVyD/)

[[MFStar模范学院]第460期婠婠么写真](https://ilovese.xyz/index.php/p/3DeJMCLp/)

[[MFStar模范学院]第510期吴雪瑶写真](https://ilovese.xyz/index.php/p/2pncqcf8/)

[[MFStar模范学院]第601期樱桃小犊子写真](https://ilovese.xyz/index.php/p/24XH4nS3/)

[[MFStar模范学院]第491期苏雨彤写真](https://ilovese.xyz/index.php/p/1bRxvY7t/)

[[MFStar模范学院]第469期顾乔楠写真](https://ilovese.xyz/index.php/p/1PFdLdfU/)

[[MFStar模范学院]第524期人间荒糖写真](https://ilovese.xyz/index.php/p/1Hnuq7RP/)

[[MFStar模范学院]第513期吴雪瑶写真](https://ilovese.xyz/index.php/p/0nln44qA/)

[[MFStar模范学院]第546期77qiqi写真](https://ilovese.xyz/index.php/p/0Zp64qoC/)

---end---