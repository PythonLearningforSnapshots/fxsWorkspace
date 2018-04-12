'''

'''

def catchexception(line):
#    print(line)
    try:
        line.encode('UTF-8')
    except Exception as e:
        print(line)
        print(str(e))
        return True
    return False

def readlog(f1,f2):
    rows = 0
    line = ''
    try:
        with open(f1,'r',encoding='gbk') as fin, open(f2,'a+') as fout:
             for line in fin:
                rows += 1
                if catchexception(line):
                    fout.write(r'lines NO.{0}: {1}'.format(rows,line))
    except Exception as e:
        print(rows)
        print(line)
        print(f1)
        print(str(e))
        return False


def readlog1(f1,f2):
    rows = 0
    line = ''
    preline =''
    try:
        with open(f1,'r',encoding='gbk') as fin, open(f2,'a+') as fout:
            line = fin.readline()
            while line:
                try:
                    rows +=1
                    preline = line
                    line = fin.readline()
                except Exception as e:
                    print(rows-1,end=':')
                    print(preline)
                    print(rows, end=':')
                    print(line)
                    fout.write(r'lines NO.{0}: {1}'.format(rows, line))
                    print(f1)
                    print(str(e))
                    continue
    except Exception as e:
        print(str(e))
        return False
    return True

def main():
    f1 = r'D:\Document\DEV\Python\Logs_analysis\case\D6K\D6K_III\zhongshan NO6 hp\snap_082407160318-20180122-MonJan22121140CST2018\20180122\log\XRDataMgr.0.log'
    f2 = r'encodeEX'
#    f1 = r'C:\users\305012621\Desktop\test'
    # 初始化f2文件
    f = open(f2, 'w')
    f.close()
    readlog1(f1, f2)

main()