import os
import time
import shutil


def filter_condition(dir_name):
    if dir_name.startswith('酒店爆操山东174CM极品性感外围女') or dir_name.startswith('醉酒美女同事送她回家') or \
        dir_name.startswith('酒店无套暴力狂操96年大一嫩妹完整版') or dir_name.startswith('HD-SDの疑似大陸野模商旅援交') or \
            dir_name.startswith('逃课带着超漂亮的上海交大师妹到宾') or dir_name.startswith('48.六星级酒店干我的气质短发富婆')\
        or dir_name.startswith('47.偏远山区禽兽二叔 来寄宿的侄') or dir_name.startswith('白嫩清純藝校校花酒店援交自拍大神信')\
        or dir_name.startswith('新交的18岁大一清纯小女友带去酒店一顿猛干，') or dir_name.startswith('14 康先生系列之91大屌网')\
        or dir_name.startswith('某地舞蹈系毕业的97年极品女神级模特家中') or dir_name.startswith('露脸常哥酒店约炮非常会叫床让人受不了的山东极品少妇高清')\
        or dir_name.startswith('太漂亮了，床上功夫又好，这侄子太幸福了，淫荡'):
        return True
    return False


movie_path = '/Users/JasonYang/Downloads/thunder'
dest_path = '/Users/JasonYang/Downloads/thunder/破脑骨入肺'
# 获取指定目录下的所有子目录
all_dir_list = os.listdir(movie_path)
for dir_item in all_dir_list:
    cur_full_path = os.path.join(movie_path, dir_item)
    if os.path.isdir(cur_full_path):
        # 目录名过滤
        if not filter_condition(dir_item):
            # 获取当前目录创建时间，用于过滤
            cur_path_ctime = os.stat(cur_full_path).st_birthtime
            time_compare_str = '2017/05/29 12:00:00'
            time_compare_t = time.mktime(time.strptime(time_compare_str, '%Y/%m/%d %H:%M:%S'))
            if cur_path_ctime > time_compare_t and not dir_item.startswith('剧集'):
                # 遍历该目录下所有文件，排除种子文件
                sub_gen = os.walk(cur_full_path)
                for root, sub_dir, files in sub_gen:
                    for file_item in files:
                        if not file_item.endswith('torrent') and not file_item.endswith('DS_Store'):
                            shutil.move(os.path.join(root, file_item), dest_path)




