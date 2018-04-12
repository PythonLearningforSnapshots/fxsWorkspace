'''
Usage::
copy files

advanced::
制作一个图形文件浏览器，方便文件拷贝
'''
import time
import os
import re


def multicopy(func):
    '''
    装饰器，用于多文件copy
    :param func:
    :return:
    '''
    def wrapper(f1,f2):
        flist = []
        ret = False
        #组装文件列表
        if os.path.isfile(f1):
            flist.append(f1)
        elif os.path.isdir(f1):
            lsdir = os.listdir(f1)
            for fname in lsdir:
                fname = r'{0}\{1}'.format(f1,fname)
                if os.path.isfile(fname):
                    flist.append(fname)
        elif '*' in f1.split('\\')[-1]:
            rex = f1.split('\\')[-1].replace(r'*',r'[\u4E00-\u9FA5A-Za-z0-9_. ]+')
            lsdir = os.listdir(os.path.dirname(f1))
            for fname in lsdir:
                if re.search(rex,fname):
                    fname = r'{0}\{1}'.format(os.path.dirname(f1), fname)
                    if os.path.isfile(fname):
                        flist.append(fname)
        else:
            print('源文件选择错误:',f1)
            return ret

        for f3 in flist:
            # 组装目标文件
            f4 = f2
            if os.path.isdir(f4):
                f4 = r'{0}\{1}'.format(f4, os.path.basename(f3))
            #判断是否覆盖文件
            if os.path.isfile(f4):
                select = input('{0}是否覆盖已存在文件{1}？(Y，N)'.format(os.path.basename(f3),os.path.basename(f4)))
                if select is 'Y':
                    pass
                else:
                    continue
            ret = func(f3,f4)
        return ret
    return wrapper


def optimize(func):
    '''
    装饰器，用于测试函数性能
    :param func:
    :return:
    '''
    def wrapper(*arg,**kwarg):
        start = time.time()
        func(*arg,**kwarg)
        runtime = time.time() - start
        print(runtime)
    return wrapper


@optimize
@multicopy
def copyfiles(f1, f2):
    '''
    Usage::
    复制文件f1到f2
    Input::
    :param class str f1
    :param class str f2

    Output::
    :return class bool True False

    '''
    try:
        print('copy {0} to {1}...'.format(os.path.basename(f1),f2),end='')
        with open(f1, 'rb') as src, open(f2, 'wb') as dst:
            content = src.read(10000)
            while content:
                dst.write(content)
                content = src.read(10000)
    except Exception as e:
        print(str(e))
        return False
    print('finished')
    return True
