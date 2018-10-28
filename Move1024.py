import os
import time
import shutil


def filter_condition(dir_name):
    if dir_name.startswith('超极品性感女神援交性爱视频流出') or dir_name.startswith('國產妹紙都愛大雞雞（露脸） 内射长沙偶遇的小骚货露脸国语') or \
             dir_name.startswith('豪哥酒店操極品黑絲模特女友無水印高清第壹部') or dir_name.startswith('酒店偷拍極品美女與男友幹炮流出 花内')\
        or dir_name.startswith('内裤哥稀有视频之大战美女长靴姐姐完整版 快点射吧') or dir_name.startswith('[首发] 91系列哥11月最新剧情大片-偷奸女友家休息的闺蜜')\
            or dir_name.startswith('胖哥情人节约炮丰满良家少妇酒店激情') or dir_name.startswith('喷血推荐91混血哥木瓜奶E奶小孙俪完整版 好久没有干过少妇了') or \
            dir_name.startswith('普通话对白背着女友操她的闺蜜 骚女已') or dir_name.startswith('和公司秘书一起出差时特意要了一间大单间,洗完澡后趁机'):
        return True
    return False


movie_path = '/Volumes/新加卷/pngphy'
dest_path = '/Volumes/新加卷/pngphy/pn_out'
# 获取指定目录下的所有子目录
all_dir_list = os.listdir(movie_path)
for dir_item in all_dir_list:
    cur_full_path = os.path.join(movie_path, dir_item)
    if os.path.isdir(cur_full_path):
        # 目录名过滤
        if not filter_condition(dir_item):
            # 获取当前目录创建时间，用于过滤
            cur_path_ctime = os.stat(cur_full_path).st_birthtime
            time_compare_str = '2018/02/01 14:00:00'
            time_compare_t = time.mktime(time.strptime(time_compare_str, '%Y/%m/%d %H:%M:%S'))
            if cur_path_ctime > time_compare_t:
                # 遍历该目录下所有文件，排除种子文件
                sub_gen = os.walk(cur_full_path)
                for root, sub_dir, files in sub_gen:
                    for file_item in files:
                        if not file_item.endswith('torrent') and not file_item.endswith('DS_Store') \
                                and not file_item.startswith('.'):
                            if os.path.exists(dest_path):
                                os.mkdir(dest_path)
                            shutil.move(os.path.join(root, file_item), dest_path)




