'''
提取和日志相关的模块文件，格式是*.cpp
'''
import os
import re


def fetchmodule(f1,filetype,f2 = 'module.txt'):
    '''

    :param f1:源文件
    :param class list, filetype:文件类型列表
    :param f2:记录和f1相关的模块
    :return: bool True finished False
    '''
    module_dt = {}

    try:
        with open(f1,'r', encoding='utf-8',errors='ignore') as fin, open(f2,'a+', encoding='utf-8') as fout:
            filename = f1.split('\\')[-1]
            for line in fin:
                ret = process(line,filetype)
                if ret:
                    if hash(ret) in module_dt.keys():
                        continue
                    else:
                        module_dt[hash(ret)] = ret
            fout.write(r'{0}: '.format(filename))
            for IDs in module_dt:
                fout.write(r'{0}; '.format(module_dt[IDs]))
            fout.write('\n')
    except Exception as e:
        print(f1)
        print(str(e))
        return False

def process(line,filetype):
    '''

    :param class str, line:
    :param class list, filetype:
    :return: class str, module name; None:寻找失败
    '''
    for pattern in filetype:
        pattern = r'[a-zA-Z0-9]+\.{0}'.format(pattern)
        if re.search(pattern,line):
            return re.search(pattern,line).group(0)
    return None


def searchfiles(path,f2):
    '''

    :param class str, path: 文件路径
    :param class str, f2:记录模块名的文件
    :return:
    '''
    flist = os.listdir(path)
    for f1 in flist:
        #sysError.log,zip文件，gif文件系列不搜寻
        if re.search(r'(sysError)|(.gif)|(.zip)|(saberalyzer)|(.tcpdump)',f1):
            continue
        f1 = '{0}\\{1}'.format(path,f1)
        #只搜寻文件，不搜索目录
        if os.path.isfile(f1):
            fetchmodule(f1,['cpp'],f2)

def main():
    f2 = r'module.txt'
    paths = [r'D:\Document\DEV\Python\Logs_analysis\case\D6K\D6K_III\zhongshan NO6 hp\snap_082407160318-20180122-MonJan22121140CST2018\20180122\log'
    ,r'D:\Document\DEV\Python\Logs_analysis\case\D6K\D6K_III\zhongshan NO6 hp\snap_082407160318-20180122-MonJan22121140CST2018\20180122\syslogs']
    #初始化f2文件
    f = open(f2,'w')
    f.close()
    for path in paths:
        searchfiles(path, f2)

main()

