<h1>青年大学习截图生成器 <img src="https://github.com/MR-Addict/qndxx-screenshort-generator/actions/workflows/pages.yml/badge.svg"/></h1>

## 1. 预览

![Preview](images/preview.png)

> Demo 网址
>
> - [https://mr-addict.github.io/qndxx-screenshort-generator](https://mr-addict.github.io/qndxx-screenshort-generator)

## 2. 说明

本项目受 Github 众多有关青年大学习项目的启发，做这个项目也是觉得好玩。

本项目使用 Python 抓取网页链接，使用`GitHub Action`在每周一的上午 12 点多自动更新，同时会将抓取结果部署在`GitHub Pages`上。

进入项目部署的网址会显示抓取的`最多15张`大学习截图，同时每期的大学习截图下方有两个按钮，复制按钮用于复制原始的大学习截图链接，如果你需要的话；下载按钮用于下载这一期的大学习截图。

> 本项目受到启发的项目
>
> - [https://github.com/UniverseLover/FuckQNDXX](https://github.com/UniverseLover/FuckQNDXX)

## 3. 如何自己部署

第一步，克隆本文档：

```bash
git clone https://github.com/MR-Addict/qndxx-screenshort-generator.git
```

第二步：安装 python 依赖：

```bash
pip install -r requirements.txt
```

第三步：运行 python 脚本：

```bash
python src/main.py
```

这一步会生成一个`public`文件夹，也就是最终的网页文档了。

第四步：搭建 web 服务器

启动 web 服务器：

```bash
python -m http.server 8080 --directory public
```

Happy coding！
