# coding:utf-8
import requests
import os
from lxml import html

# open file
fp = open('./test.txt', 'r+')
file_context = fp.read()

xpath_tree = html.fromstring(file_context)
image_list = xpath_tree.xpath('//div[@class="RichText PostIndex-content '
                              'av-paddingSide av-card"]/img/@data-original')

# print('input...')
# image_list = input().split(' ')
# image_list = xpath_tree.xpath('//div[@class="RichText PostIndex-content av-paddingSide av-card"]')
# XPath的序号是从1开始的！！！！
if len(image_list) > 0:
    image_count = 1
    for item in image_list:
        ret = requests.get(item)
        if ret.status_code == 200:
            cur_file_name = '%d.jpg' % image_count
            with open(os.path.join(os.path.curdir, cur_file_name), 'wb') as f:
                f.write(ret.content)
                f.close()
                image_count += 1

fp.close()


# url = 'https://pic3.zhimg.com/41163f7910ac6b9047a0e3419973250e_r.jpg'
# ret = requests.get(url)
# image_count = 1
# if ret.status_code == 200:
#     cur_file_name = '%d.jpg' % image_count
#     with open(os.path.join(os.path.curdir, cur_file_name), 'wb') as f:
#         f.write(ret.content)
#         f.close()
