'''
测试文件分析格式，即，如何把文件分列
'''
import re


def formatfile(f1,filetype,col,f2 = 'log.key'):
    '''
    usage::

    Ipput::
    :param f1:
    :param split:
    :return:
    '''
    try:
        with open(f1,'r', encoding='utf-8') as f_in, open(f2,'w', encoding='utf-8') as f_out:
            for line in f_in:
                f_out.write(keyprocess(line,filetype,col))
    except Exception as e:
        print(str(e))
        return False
    return True


def keyprocess(line,filetype,col):
    '''
    usage::
    根据文件类型，提取文件的关键字

    input::
    :param class str, line: 一行文字
    :param class str, filetype: 文件类型
    :param class int, col: 关键字所在列

    output::
    :return: calss str, keywords
    '''
    if filetype == 'CSV':
        key_ls = line.split(',')
    elif 'KSV' in filetype:
        key_ls = line.split(filetype.split('_')[1])
    else:
        return None
    # 排除文件中不符合规则的行
    if len(key_ls) < col:
        return '\n'

    # 检验关键字是否含有文件结尾符'\n'
    if key_ls[col - 1][-1] == '\n':
        return key_ls[col - 1]
    else:
        return '{0}{1}'.format(key_ls[col - 1], '\n')


def main():
    ret = formatfile(r'D:\Document\DEV\Python\Logs_analysis\case\D6K\D6K_III\zhongshan NO6 hp\snap_082407160318-20180122-MonJan22121140CST2018\20180122\log\VIEWER-CONTROLLER.log.1',
               'KSV_INFO',2)
    return ret

main()