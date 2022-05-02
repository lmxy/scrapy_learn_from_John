# -*- coding = utf-8 -*-
# @Time : 2022/4/30 22:24
# @Author : yaowei
# @File : move_anime.py
# @Software : PyCharm
import shutil
from pathlib import Path


# step 1 get anime fold name
def getAnimeName(p):
    anime_folder_names = []

    for file in p.iterdir():

        if file.is_file():
            # print(file)
            root = file.name
            if '[Erai' in root:
                anime_name = root[12:].split(' - ')[0].strip()
                if anime_name not in anime_folder_names:
                    anime_folder_names.append(anime_name)
                    # print(anime_name)
            elif '[Sub' in root:
                anime_name = root[12:].split(' - ')[0].strip()
                print(anime_name)
                if anime_name not in anime_folder_names:
                    anime_folder_names.append(anime_name)
                    # print(anime_name)
            elif '[Ohys-Raws]' in root:
                anime_name = root[12:].split(' - ')[0].strip()
                if anime_name not in anime_folder_names:
                    anime_folder_names.append(anime_name)
                    # print(anime_name)
            elif '[Pikari' in root:
                anime_name = root[16:].split('(')[0].strip()
                # print(anime_name)
                if anime_name not in anime_folder_names:
                    anime_folder_names.append(anime_name)
            elif '[Nekomoe' in root:
                anime_name = root.split('[')[2][:-1].strip()
                # print(anime_name)
                if anime_name not in anime_folder_names:
                    anime_folder_names.append(anime_name)

    return anime_folder_names

# step 2 Create folder to hold anime files
def createFolders(p, names):
    for name in names:
        path_folder = p / name
        # print(path_folder)
        if not path_folder.exists():
            path_folder.mkdir()
        else:
            pass

# step 3 Get folders name
def main():
    dir = 'D:\\anime202204'
    p = Path(dir)
    anime_files = [f.name for f in p.iterdir() if f.is_file()]
    c_folders_list = getAnimeName(p)
    createFolders(p, c_folders_list)
    anime_folders = [f.name for f in p.iterdir() if f.is_dir()]

    # Step 4 Move anime files to relative folder
    for folder in anime_folders:
        for i in anime_files:
            if folder.upper() in i.upper():
                path_1 = p / i
                path_2 = p / folder / i
                shutil.move(path_1, path_2)

# When match, upper will match with lower!!!
if __name__ == '__main__':
    main()

