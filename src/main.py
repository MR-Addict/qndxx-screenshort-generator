import os
from bs4 import BeautifulSoup

from qndxx import qndxx
from utils import download_image, copy_files


def get_img_links():
    img_links = []

    courses = qndxx()
    for item in courses:
        title = item["title"]
        link = item["imgEndUri"]
        img_links.append({"title": title, "link": link, "path": "images/", 'name': f'{title}.jpg'})
        download_image(link, 'public/images/', title, '.jpg')
    return img_links


def gen_one_element(img_path, name, title, link):
    soup = BeautifulSoup('', "html.parser")
    element_tag = soup.new_tag("li", attrs={"class": "img-element"})

    h1_tag = soup.new_tag("h1")
    h1_tag.string = title

    img_tag = soup.new_tag(
        "img", attrs={"data-src": img_path+name, "alt": "image", 'onerror': 'img_error(this)', "class": "lazyload"})
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


def gen_img_container():
    with open(os.path.join(os.getcwd(), "pages/index.html"), 'r', encoding="utf-8") as file:
        raw_html_str = file.read()
        soup = BeautifulSoup(raw_html_str, "html.parser")

    img_container = soup.new_tag("ul", attrs={"class": "img-container"})
    for item in get_img_links():
        img_container.append(gen_one_element(item['path'], item['name'], item['title'], item['link']))
    soup.html.body.append(img_container)
    return soup.prettify()


if __name__ == '__main__':
    # copy public files
    public_path = os.path.join(os.getcwd(), 'public')
    if not os.path.exists(public_path):
        os.makedirs(public_path)
    copy_files('pages', 'public')

    # generate static files
    with open(os.path.join(os.getcwd(), 'public/index.html'), "w", encoding="utf-8") as outfile:
        img_container_str = str(gen_img_container())
        outfile.write(img_container_str)
        print("[INFO] Static files generated!")
