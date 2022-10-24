import os
import shutil
import requests
from requests_html import HTMLSession
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import urllib.request


def copy_files(src, dest):
    shutil.copytree(os.getcwd()+'/'+src, os.getcwd() + '/' +
                    dest, dirs_exist_ok=True)


def download_image(url, folder, name, extension):
    full_path = folder + name + extension
    if not os.path.exists(folder):
        os.makedirs(folder)
    urllib.request.urlretrieve(url, full_path)


def get_img_title(img_link):
    res = requests.get(img_link)
    soup = BeautifulSoup(res.content, "html.parser")
    img_title = soup.title.text
    return img_title.replace("“青年大学习”", '')


def get_img_links():
    img_links = []
    source_url = "http://news.cyol.com/gb/channels/vrGlAKDl/index.html"
    session = HTMLSession()
    res = session.get(source_url)
    res.html.render()
    soup = BeautifulSoup(res.html.html, "html.parser")
    for index, prop in enumerate(soup.select(".movie-list h3 a")):
        if index < 15:
            url = prop['href']
            title = get_img_title(url)
            link = urljoin(url, urlparse(url).path).replace(
                'm.html', 'images/end.jpg').replace(
                'm2.html', 'images/end.jpg')
            img_links.append(
                {"title": title, "link": link, "path": "images/", 'name': f'{title}.jpg'})
            download_image(link, 'public/images/', title, '.jpg')
    return img_links


def split_array(array, step):
    return [array[i:i+step] for i in range(0, len(array), step)]


def get_html(html_path):
    with open(html_path, 'r', encoding="utf-8") as file:
        return file.read()


def gen_one_tag(img_path, name, title, link):
    soup = BeautifulSoup('', "html.parser")
    element_tag = soup.new_tag("div", attrs={"class": "img-element"})

    h1_tag = soup.new_tag("h1")
    h1_tag.string = title

    img_tag = soup.new_tag(
        "img", attrs={"data-src": img_path+name, 'onerror': 'img_error(this)', "class": "lazyload"})
    input_tag = soup.new_tag("input", attrs={"type": "hidden", 'value': link})

    buttons_tag = soup.new_tag("div", attrs={"class": "img-buttons"})
    button1_tag = soup.new_tag(
        "button", attrs={'onclick': 'button_copy(this)'})
    button1_tag.string = '复制链接'
    button2_tag = soup.new_tag(
        "button", attrs={'onclick': 'button_download(this)'})
    button2_tag.string = '下载截图'
    buttons_tag.append(button1_tag)
    buttons_tag.append(button2_tag)
    element_tag.append(h1_tag)
    element_tag.append(img_tag)
    element_tag.append(input_tag)
    element_tag.append(buttons_tag)

    return element_tag


def gen_row_tag(elements):
    soup = BeautifulSoup('', "html.parser")
    row_tag = soup.new_tag("div", attrs={"class": "img-row"})
    for ele in elements:
        row_tag.append(gen_one_tag(
            ele['path'], ele['name'], ele['title'], ele['link']))
    return row_tag


def gen_column_tag():
    soup = BeautifulSoup(get_html('pages/index.html'), "html.parser")
    row_column = soup.new_tag("div", attrs={"class": "img-column"})
    for elements in split_array(get_img_links(), 3):
        row_column.append(gen_row_tag(elements))
    soup.html.body.append(row_column)
    return soup.prettify()


if __name__ == '__main__':
    if not os.path.exists('public'):
        os.makedirs('public')
    copy_files('pages/', 'public/')
    with open('public/index.html', "w", encoding="utf-8") as outfile:
        outfile.write(str(gen_column_tag()))
    print("[INFO] Static files generated!")
