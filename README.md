
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
[[MFStar模范学院]第634期温柔的柔写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第634期温柔的柔写真/)

[[MFStar模范学院]第633期董林越写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第633期董林越写真/)

[[MFStar模范学院]第632期米亚写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第632期米亚写真/)

[[MFStar模范学院]第631期杨可可写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第631期杨可可写真/)

[[MFStar模范学院]第628期雪糕写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第628期雪糕写真/)

[[MFStar模范学院]第625期柒喜小写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第625期柒喜小写真/)

[[MFStar模范学院]第623期星萌写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第623期星萌写真/)

[[MFStar模范学院]第622期揉揉肉肉写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第622期揉揉肉肉写真/)

[[MFStar模范学院]第621期水塔塔写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第621期水塔塔写真/)

[[MFStar模范学院]第620期大美妞儿写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第620期大美妞儿写真/)

[[MFStar模范学院]第619期李雅柔写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第619期李雅柔写真/)

[[MFStar模范学院]第618期伊诺写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第618期伊诺写真/)

[[MFStar模范学院]第617期文静儿写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第617期文静儿写真/)

[[MFStar模范学院]第614期温心怡写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第614期温心怡写真/)

[[MFStar模范学院]第613期杨可可写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第613期杨可可写真/)

[[MFStar模范学院]第612期樱桃小犊子写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第612期樱桃小犊子写真/)

[[MFStar模范学院]第611期王楚璇写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第611期王楚璇写真/)

[[MFStar模范学院]第609期汐汐爱吃草莓写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第609期汐汐爱吃草莓写真/)

[[MFStar模范学院]第608期茜茜写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第608期茜茜写真/)

[[MFStar模范学院]第605期大美妞儿写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第605期大美妞儿写真/)

[[MFStar模范学院]第604期雪糕写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第604期雪糕写真/)

[[MFStar模范学院]第603期加朵写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第603期加朵写真/)

[[MFStar模范学院]第602期汐汐爱吃草莓写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第602期汐汐爱吃草莓写真/)

[[MFStar模范学院]第601期樱桃小犊子写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第601期樱桃小犊子写真/)

[[MFStar模范学院]第600期雪糕写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第600期雪糕写真/)

[[MFStar模范学院]第599期茜茜写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第599期茜茜写真/)

[[MFStar模范学院]第597期星萌写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第597期星萌写真/)

[[MFStar模范学院]第596期樱桃小犊子写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第596期樱桃小犊子写真/)

[[MFStar模范学院]第595期汐汐爱吃草莓写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第595期汐汐爱吃草莓写真/)

[[MFStar模范学院]第594期露露写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第594期露露写真/)

[[MFStar模范学院]第593期雪糕写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第593期雪糕写真/)

[[MFStar模范学院]第591期汐汐爱吃草莓写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第591期汐汐爱吃草莓写真/)

[[MFStar模范学院]第590期小樱花写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第590期小樱花写真/)

[[MFStar模范学院]第589期yoo优优写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第589期yoo优优写真/)

[[MFStar模范学院]第588期雪雪琪写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第588期雪雪琪写真/)

[[MFStar模范学院]第587期露露写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第587期露露写真/)

[[MFStar模范学院]第586期加朵写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第586期加朵写真/)

[[MFStar模范学院]第583期露露写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第583期露露写真/)

[[MFStar模范学院]第582期白茹雪写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第582期白茹雪写真/)

[[MFStar模范学院]第579期白茹雪写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第579期白茹雪写真/)

[[MFStar模范学院]第578期Ai西西里写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第578期Ai西西里写真/)

[[MFStar模范学院]第576期白茹雪写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第576期白茹雪写真/)

[[MFStar模范学院]第575期露露写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第575期露露写真/)

[[MFStar模范学院]第574期樱桃小犊子写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第574期樱桃小犊子写真/)

[[MFStar模范学院]第572期吴思晚写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第572期吴思晚写真/)

[[MFStar模范学院]第570期yoo优优写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第570期yoo优优写真/)

[[MFStar模范学院]第568期露露写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第568期露露写真/)

[[MFStar模范学院]第567期白茹雪写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第567期白茹雪写真/)

[[MFStar模范学院]第566期露露写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第566期露露写真/)

[[MFStar模范学院]第565期小米写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第565期小米写真/)

[[MFStar模范学院]第564期小果冻儿写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第564期小果冻儿写真/)

[[MFStar模范学院]第560期吴思晚写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第560期吴思晚写真/)

[[MFStar模范学院]第559期韩好甜写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第559期韩好甜写真/)

[[MFStar模范学院]第558期白茹雪写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第558期白茹雪写真/)

[[MFStar模范学院]第557期人间荒糖写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第557期人间荒糖写真/)

[[MFStar模范学院]第554期羽仁鹿写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第554期羽仁鹿写真/)

[[MFStar模范学院]第553期小果冻儿写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第553期小果冻儿写真/)

[[MFStar模范学院]第551期吴雪瑶写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第551期吴雪瑶写真/)

[[MFStar模范学院]第550期优优写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第550期优优写真/)

[[MFStar模范学院]第549期白茹雪写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第549期白茹雪写真/)

[[MFStar模范学院]第548期小果冻儿写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第548期小果冻儿写真/)

[[MFStar模范学院]第547期徐媛媛写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第547期徐媛媛写真/)

[[MFStar模范学院]第546期77qiqi写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第546期77qiqi写真/)

[[MFStar模范学院]第544期徐媛媛写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第544期徐媛媛写真/)

[[MFStar模范学院]第543期甜筒晓彤写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第543期甜筒晓彤写真/)

[[MFStar模范学院]第542期youOvOyou写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第542期youOvOyou写真/)

[[MFStar模范学院]第541期夏沫沫写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第541期夏沫沫写真/)

[[MFStar模范学院]第540期蔡文钰写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第540期蔡文钰写真/)

[[MFStar模范学院]第539期王蜜写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第539期王蜜写真/)

[[MFStar模范学院]第538期模特合集写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第538期模特合集写真/)

[[MFStar模范学院]第537期王蜜写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第537期王蜜写真/)

[[MFStar模范学院]第536期佳佳崽崽写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第536期佳佳崽崽写真/)

[[MFStar模范学院]第534期蔡文钰写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第534期蔡文钰写真/)

[[MFStar模范学院]第533期77qiqi写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第533期77qiqi写真/)

[[MFStar模范学院]第532期一颗甜蛋黄写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第532期一颗甜蛋黄写真/)

[[MFStar模范学院]第531期苏西写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第531期苏西写真/)

[[MFStar模范学院]第529期苏西写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第529期苏西写真/)

[[MFStar模范学院]第528期一颗甜蛋黄写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第528期一颗甜蛋黄写真/)

[[MFStar模范学院]第527期李颖煊写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第527期李颖煊写真/)

[[MFStar模范学院]第526期一颗甜蛋黄写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第526期一颗甜蛋黄写真/)

[[MFStar模范学院]第525期李颖煊写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第525期李颖煊写真/)

[[MFStar模范学院]第524期人间荒糖写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第524期人间荒糖写真/)

[[MFStar模范学院]第523期一颗甜蛋黄写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第523期一颗甜蛋黄写真/)

[[MFStar模范学院]第522期qiqi写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第522期qiqi写真/)

[[MFStar模范学院]第521期墨韩写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第521期墨韩写真/)

[[MFStar模范学院]第520期米漫池写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第520期米漫池写真/)

[[MFStar模范学院]第519期吴雪瑶写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第519期吴雪瑶写真/)

[[MFStar模范学院]第518期揉揉肉肉写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第518期揉揉肉肉写真/)

[[MFStar模范学院]第516期77qiqi写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第516期77qiqi写真/)

[[MFStar模范学院]第515期奶瓶子写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第515期奶瓶子写真/)

[[MFStar模范学院]第514期米漫池写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第514期米漫池写真/)

[[MFStar模范学院]第513期吴雪瑶写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第513期吴雪瑶写真/)

[[MFStar模范学院]第512期墨韩写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第512期墨韩写真/)

[[MFStar模范学院]第511期揉揉肉肉写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第511期揉揉肉肉写真/)

[[MFStar模范学院]第510期吴雪瑶写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第510期吴雪瑶写真/)

[[MFStar模范学院]第509期方子萱写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第509期方子萱写真/)

[[MFStar模范学院]第508期星萌写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第508期星萌写真/)

[[MFStar模范学院]第507期模特合集写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第507期模特合集写真/)

[[MFStar模范学院]第505期白茹雪写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第505期白茹雪写真/)

[[MFStar模范学院]第501期NaNa_baby写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第501期NaNa_baby写真/)

[[MFStar模范学院]第499期人间荒糖写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第499期人间荒糖写真/)

[[MFStar模范学院]第498期桃香子写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第498期桃香子写真/)

[[MFStar模范学院]第496期奶瓶子写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第496期奶瓶子写真/)

[[MFStar模范学院]第494期婠婠么写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第494期婠婠么写真/)

[[MFStar模范学院]第493期玉兔写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第493期玉兔写真/)

[[MFStar模范学院]第492期芊澄写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第492期芊澄写真/)

[[MFStar模范学院]第491期苏雨彤写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第491期苏雨彤写真/)

[[MFStar模范学院]第490期水水er写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第490期水水er写真/)

[[MFStar模范学院]第489期小果冻儿写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第489期小果冻儿写真/)

[[MFStar模范学院]第487期白茹雪写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第487期白茹雪写真/)

[[MFStar模范学院]第486期模特合集写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第486期模特合集写真/)

[[MFStar模范学院]第485期yoo优优写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第485期yoo优优写真/)

[[MFStar模范学院]第483期墨韩写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第483期墨韩写真/)

[[MFStar模范学院]第482期人间荒糖写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第482期人间荒糖写真/)

[[MFStar模范学院]第481期春药儿写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第481期春药儿写真/)

[[MFStar模范学院]第480期薇薇写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第480期薇薇写真/)

[[MFStar模范学院]第479期模特合集写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第479期模特合集写真/)

[[MFStar模范学院]第478期人间荒糖写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第478期人间荒糖写真/)

[[MFStar模范学院]第477期星萌写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第477期星萌写真/)

[[MFStar模范学院]第476期yoo优优写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第476期yoo优优写真/)

[[MFStar模范学院]第475期崔灿写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第475期崔灿写真/)

[[MFStar模范学院]第474期人间荒糖写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第474期人间荒糖写真/)

[[MFStar模范学院]第472期玉兔miki写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第472期玉兔miki写真/)

[[MFStar模范学院]第471期yoo优优写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第471期yoo优优写真/)

[[MFStar模范学院]第470期母崽崽写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第470期母崽崽写真/)

[[MFStar模范学院]第469期顾乔楠写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第469期顾乔楠写真/)

[[MFStar模范学院]第467期小果冻儿写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第467期小果冻儿写真/)

[[MFStar模范学院]第466期如歌写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第466期如歌写真/)

[[MFStar模范学院]第465期婠婠么写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第465期婠婠么写真/)

[[MFStar模范学院]第464期安琪Yee写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第464期安琪Yee写真/)

[[MFStar模范学院]第463期小波多写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第463期小波多写真/)

[[MFStar模范学院]第461期薛琪琪写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第461期薛琪琪写真/)

[[MFStar模范学院]第460期婠婠么写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第460期婠婠么写真/)

[[MFStar模范学院]第459期母崽崽写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第459期母崽崽写真/)

[[MFStar模范学院]第458期郑颖姗写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第458期郑颖姗写真/)

[[MFStar模范学院]第457期水水er写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第457期水水er写真/)

[[MFStar模范学院]第455期水水er写真](https://ilovese.xyz/index.php/p/[MFStar模范学院]第455期水水er写真/)

---end---