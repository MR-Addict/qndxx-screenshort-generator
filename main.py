import os
import json
import shutil
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import urllib.request


def copy_files(src, dest):
    shutil.copytree(os.getcwd()+'/'+src, os.getcwd() + '/' +
                    dest, dirs_exist_ok=True)


def download_image(url, folder, name, extension):
    full_path = folder + name + extension
    if not os.path.exists(folder):
        os.mkdir(folder)
    urllib.request.urlretrieve(url, full_path)


def get_img_title(img_link):
    res = requests.get(img_link)
    soup = BeautifulSoup(res.content, "html.parser")
    img_title = soup.title.text
    return img_title.replace("“青年大学习”", '')


def get_img_links():
    img_links = {"data": []}
    source_url = "http://news.cyol.com/gb/channels/vrGlAKDl"
    res = requests.get(source_url)
    soup = BeautifulSoup(res.content, "html.parser")
    for index, prop in enumerate(soup.select(".movie-list h3 a")):
        if index < 15:
            url = prop['href']
            title = get_img_title(url)
            link = urljoin(url, urlparse(url).path).replace(
                'm.html', 'images/end.jpg').replace(
                'm2.html', 'images/end.jpg')
            img_links["data"].append(
                {"title": title, "link": link, "path": "images/", 'name': f'{title}.jpg'})
            download_image(link, 'pages/images/', title, '.jpg')
    return img_links


if __name__ == '__main__':
    img_link_dic = get_img_links()
    with open('pages/data.json', 'w') as file:
        json.dump(img_link_dic, file, ensure_ascii=True)
    copy_files('pages/', 'public/')
