import os
import shutil
import urllib.request


def copy_files(src, dest):
    shutil.copytree(os.path.join(os.getcwd(), src), os.path.join(os.getcwd(), dest), dirs_exist_ok=True)


def download_image(url, folder, name, extension):
    full_path = folder + name + extension
    if not os.path.exists(folder):
        os.makedirs(folder)
    urllib.request.urlretrieve(url, full_path)
