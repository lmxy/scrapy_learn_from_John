# -*- coding = utf-8 -*-
# @Time : 2022/4/30 22:24
# @Author : yaowei
# @File : move_anime.py
# @Software : PyCharm
import os, shutil

# step 1 get anime fold name
def getAnimeName(dir):
    files = os.listdir(dir)
    anime_folder_names = []

    for i in files:
        root, ext = os.path.splitext(i)
        if ext:
            if '[Erai' in root:
                anime_name = root[12:].split(' - ')[0].strip()
                if anime_name not in anime_folder_names:
                    anime_folder_names.append(anime_name)
                    # print(anime_name)
            elif '[Sub' in root:
                anime_name = root[12:].split(' - ')[0].strip()
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

def animeFiles(dir):
    files = os.listdir(dir)
    anime_files = []

    for i in files:
        if '.mp4' in i or '.mkv' in i:
            anime_files.append(i)
        else:
            pass
    return anime_files

# step 2 Create folder to hold anime files
def createFolders(dir, names):
    for name in names:
        path_folder = os.path.join(dir, name)
        # print(path_folder)
        if not os.path.exists(path_folder):
            os.mkdir(path_folder)
        else:
            pass

# step 3 Get folders name
def getFoldersName(dir):
    folders_list = []
    files = os.listdir(dir)
    # print(files)
    for i in files:
        if '.mp4' in i or '.mkv' in i:
            # print(i)
            pass
        else:
            folders_list.append(i)
    return folders_list

def main():
    dir = 'D:\\anime202204'
    anime_folder_names = getAnimeName(dir)
    createFolders(dir, anime_folder_names)
    folders = getFoldersName(dir)

    # Step 4 Move anime files to relative folder
    anime_files = animeFiles(dir)
    # print(anime_files)
    for folder in folders:
        for i in anime_files:
            if folder in i:
                path_1 = os.path.join(dir, i)
                path_2 = os.path.join(os.path.join(dir, folder), i)
                shutil.move(path_1, path_2)


if __name__ == '__main__':
    main()


# print(anime_folder_names)

