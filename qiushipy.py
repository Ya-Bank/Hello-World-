import requests,os,re,useragnt_r
url = 'https://www.qiushibaike.com/imgrank/page/%d/'

headers={
    'User-Agent':useragnt_r.get_random_agent()
}
dir_name = './pic'
if not os.path.exists(dir_name):            #如果这个目录不存在就创建这个文件夹
    os.mkdir(dir_name)
for page_num in range(1,14):                 #获取内容到html
    real_url = format(url%page_num)
    html = requests.get(url=real_url,headers=headers).text
# <div class="thumb">
# <a href="/article/123489955" target="_blank">
# <img src="//pic.qiushibaike.com/system/pictures/12348/123489955/medium/X3PXDKE4V73CTF3Q.jpg" alt="糗事#123489955" class="illustration" width="100%" height="auto">
# </a>
# </div>
    str = '<div class="thumb">.*?<img src="(.*?)".*?>'
    url_list = re.findall(str,html,re.S)
    print(len(url_list))
    print(url_list)
    for u in url_list:
        img_name = u.split('/')[-1]
        res = requests.get('http:'+u,headers=headers)
        with open(dir_name + '/' + img_name,'wb') as f:
            f.write(res.content)
            print(img_name,'end...')