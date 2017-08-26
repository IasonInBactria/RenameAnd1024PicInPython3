import os
import time
import shutil


def filter_condition(dir_name):
    if dir_name.startswith('国际酒店公关部领班 真是太漂亮了仔细听对白') or dir_name.startswith('性感美女太漂亮了操的时间太长,美女一直') or \
             dir_name.startswith('明显不会抽烟的微拍美眉厕所装酷菊花痒了')\
        or dir_name.startswith('珍稀资源某纤体美容机构内部培') or dir_name.startswith('10.Fluff And Fold')\
            or dir_name.startswith('大鸡巴哥会所嫖妓系列颜射把妹子的眼影都搞掉色') or dir_name.startswith('BBC地平线'):
        return True
    return False


movie_path = '/Users/JasonYang/Downloads/thunder'
dest_path = '/Users/JasonYang/Downloads/thunder/new_pngphy'
# 获取指定目录下的所有子目录
all_dir_list = os.listdir(movie_path)
for dir_item in all_dir_list:
    cur_full_path = os.path.join(movie_path, dir_item)
    if os.path.isdir(cur_full_path):
        # 目录名过滤
        if not filter_condition(dir_item):
            # 获取当前目录创建时间，用于过滤
            cur_path_ctime = os.stat(cur_full_path).st_birthtime
            time_compare_str = '2017/08/02 15:00:00'
            time_compare_t = time.mktime(time.strptime(time_compare_str, '%Y/%m/%d %H:%M:%S'))
            if cur_path_ctime > time_compare_t:
                # 遍历该目录下所有文件，排除种子文件
                sub_gen = os.walk(cur_full_path)
                for root, sub_dir, files in sub_gen:
                    for file_item in files:
                        if not file_item.endswith('torrent') and not file_item.endswith('DS_Store') \
                                and not file_item.startswith('.'):
                            shutil.move(os.path.join(root, file_item), dest_path)




