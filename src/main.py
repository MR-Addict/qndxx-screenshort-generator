import os
import pytz
from bs4 import BeautifulSoup
from datetime import datetime

from get_img_links import get_img_links
from utils import download_image, copy_files
from render_img_container import render_img_container


if __name__ == '__main__':
    # get dataset
    print("Getting qndxx dataset...")
    img_links = get_img_links()

    # copy assets files
    print("Copying assets files...")
    public_path = os.path.join(os.getcwd(), 'public')
    if not os.path.exists(public_path):
        os.makedirs(public_path)
    copy_files('pages', 'public')

    # render index.html
    print("Rendering index.html...")
    with open(os.path.join(os.getcwd(), "pages/index.html"), 'r', encoding="utf-8") as file:
        raw_html_str = file.read()
    formated_date = datetime.now(pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')

    soup = BeautifulSoup(raw_html_str, "html.parser")
    soup.select_one('header').insert_after(render_img_container(img_links))
    soup.select_one("footer .rendering-time").string = f"Last update:{formated_date}"

    with open(os.path.join(os.getcwd(), 'public/index.html'), "w", encoding="utf-8") as output_html:
        output_html.write(str(soup.prettify()))
