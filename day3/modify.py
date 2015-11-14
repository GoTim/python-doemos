#!/usr/bin/env python
#-*- coding:utf-8 -*-

import time
import json
def get_backend(check_info):
    backend_index = []
    with open('haproxy.conf','r') as f:  #打开文件
        li  = []   #创建一个新列表，后续加入
        for i in f.readlines(): #循环列表
            i = i.strip('\n') #取消回车符
            li.append(i) #把读取的文件加入列表中
        for k,v in enumerate(li):#循环列表并指定下标
            if 'backend' in v and 'backend' == v[0:7]:
                backend_index.append(k) #把backend的所在的下标加入到列表中
        for i in backend_index:  #循环backend的下标
            if check_info in li[i] and i != backend_index[-1]: #如果发现info在li列表中的i=循环的下标中并且不是最后一个
                for i in  li[i:backend_index[backend_index.index(i)+1]]:#打印li中i下标所在行和backend_index中的i后面元素所在行
                    print i
                return ''
                #return [for i in li[i:backend_index[backend_index.index(i)+1]]:print i ]
            elif check_info in li[i] and i == backend_index[-1]:  #如果是最后一个打印所有
                return li[i:]  #打印行
        else:
            return '\033[32;1m对比起无法找到您输入的\033[31;1m%s\033[0m\033[32;1m的backend信息\033[0m' % check_info

def add_backend(add_infos):
    add_info = json.loads(add_infos)
    a = 'backend %s\n\t\tserver %s weight %s maxconn %s' % (add_info['backend'],add_info['record']['server'],add_info['record']['weight'],add_info['record']['maxconn'])
    #上面的a是定义，如果没有用户输入的backend，就从字典模板中获取相关的值添加到配置文件中
    b = '\t\tserver %s weight %s maxconn %s' % (add_info['record']['server'],add_info['record']['weight'],add_info['record']['maxconn'])
    #上面的b的定义，如果backend存在直接从字典模板中获取相关的值添加到backend下面的配置文件中
    backend_title = add_info['backend']
    backend_index = []
    li = []   #创建一个新列表，后续加入
    with open('haproxy.conf','r') as f1,open('haproxy.conf.add','w') as f2: #打开文件
        for i in f1.readlines(): #循环列表
            i = i.strip('\n') #取消回车符
            li.append(i) #把读取的文件加入列表中
        for k,v in enumerate(li):#循环列表并指定下标
            if 'backend' in v and 'backend' == v[0:7]:
                backend_index.append(k) #把backend的所在的下标加入到列表中
        write_start = li[0:backend_index[0]-1]  #取出backend开头之前的数据并写入文件！
        for s in write_start:
            f2.write(s)
            f2.write('\n')
        li_backend = li[backend_index[0]:]
        #print li_backend[-1]

        for i in li_backend:
            if backend_title not in i:
                f2.write(i)
                f2.write('\n')
                #print i
                if i  == li_backend[-1]:
                    f2.write('\n')
                    f2.write(a)
                    return '\033[31;1m您添加的backend不存在，以为您创建新的backend\033[0m'
            if backend_title in i:
                f2.write(i)
                f2.write('\n')
                f2.write(b)
                f2.write('\n')
                for m in li_backend[li_backend.index(i)+1:]:
                    f2.write(m)
                    f2.write('\n')
                return '\033[32;1m您添加的backend已存在，为您追加信息server信息\033[0m'

def del_backend(del_info):



if __name__ == '__main__':
    print '''\033[34;1m\
输入1获取ha记录
输入2增加ha记录
输入3删除ha记录\033[0m'''

    while True:
        num = raw_input('\033[32;1m请输入序列号：\033[0m')
        if num == '1':
            read = raw_input('\033[033;1m请输入您要查找的backend：\033[0m')
            print get_backend(read)
        if num == '2':
            read = raw_input('\033[033;1m请输入您要增加的backend：\033[0m')
            print add_backend(read)
        if num == '3':
            read = raw_input('\033[033;1m请输入你要删除的backend：\033[0m')
            print del_backend(read)


#www.oldboy.org