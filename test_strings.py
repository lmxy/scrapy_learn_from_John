# -*- coding = utf-8 -*-
# @Time : 2022/5/1 15:36
# @Author : yaowei
# @File : test_strings.py
# @Software : PyCharm
import os,shutil
from pathlib import Path
name = 'Komi-san wa, Komyushou Desu. Part 2'

dir = 'D:\\anime202204'
p = Path(dir)

anime_folder_names = [f.name for f in Path(dir).iterdir() if f.is_dir()]

print(len(anime_folder_names))
print(anime_folder_names)

