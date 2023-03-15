
from qndxx import qndxx


def get_img_links():
    img_links = []

    courses = qndxx()
    for item in courses:
        title = item["title"]
        link = item["screenshot"]
        img_links.append({"title": title, "link": link, "path": "images/", 'name': f'{title}.jpg'})
    return img_links
