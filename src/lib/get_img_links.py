import math
import requests
from urllib.parse import urljoin


def fetchOnePage(page):
    url = f'https://qczj.h5yunban.com/qczj-youth-learning/cgi-bin/common-api/course/list?pageNum={page}'
    res = requests.get(url)
    result = res.json()["result"]

    courses = []
    pagedInfo = result['pagedInfo']
    pagedInfo['total'] = int(pagedInfo["total"])
    list = result["list"]

    for course in list[::-1]:
        title = course["title"]
        screenshot = urljoin(course['uri'], 'images/end.jpg')
        courses.append({"title": title, "screenshot": screenshot})
    return ({"pagedInfo": pagedInfo, "courses": courses})


def qndxx():
    data = fetchOnePage(1)
    pageSize = data["pagedInfo"]["pageSize"]
    totalCourses = data["pagedInfo"]["total"]
    totalPages = math.ceil(totalCourses / pageSize)

    courses = []
    onePage = fetchOnePage(totalPages)
    courses.extend(onePage["courses"])
    if len(onePage["courses"]) < 9:
        anotherPage = fetchOnePage(totalPages-1)
        courses.extend(anotherPage["courses"])

    return courses[:9]


def get_img_links():
    img_links = []

    courses = qndxx()
    for item in courses:
        title = item["title"]
        link = item["screenshot"]
        img_links.append({"title": title, "link": link, "path": "images/", 'name': f'{title}.jpg'})
    return img_links
