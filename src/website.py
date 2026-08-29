import os
from os.path import isfile
import shutil


def copy_static():
    if os.path.exists("./public/"):
        shutil.rmtree("./public/")
    os.mkdir("./public/")

    if os.path.exists("./static/"):
        recursive_copy("./static/", "./public/")
        # for file in os.listdir("./static/"):
        #     file_path = os.path.join("./static/", file)
        #     if os.path.isfile(file_path):
        #         shutil.copy(file_path, "./public/")


def recursive_copy(current_dir: str, dest_dir: str):
    print("current_dir:", current_dir)
    contents = os.listdir(current_dir)
    print("contents:", contents)
    for content in contents:
        if os.path.isfile(os.path.join(current_dir, content)):
            print("file_content", content)
            file_path = os.path.join(current_dir, content)
            shutil.copy(file_path, dest_dir)
        else:
            next_dir = os.path.join(current_dir, content)
            next_dest_dir = os.path.join(dest_dir, content)
            os.mkdir(next_dest_dir)
            recursive_copy(next_dir, next_dest_dir)
