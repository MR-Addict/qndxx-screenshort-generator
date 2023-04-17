import os
import urllib.request


def download_img(url, path, filename):
    full_path = os.path.join(path, filename)
    if not os.path.exists(path):
        os.makedirs(path)
    urllib.request.urlretrieve(url, full_path)
