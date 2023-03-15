import os
from bs4 import BeautifulSoup


def render_img_element(img_path, name, title, link):
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


def render_img_container(img_links):
    # render image container
    soup = BeautifulSoup('', "html.parser")
    img_container = soup.new_tag("ul", attrs={"class": "img-container"})

    for item in img_links:
        img_container.append(render_img_element(item['path'], item['name'], item['title'], item['link']))

    return img_container
