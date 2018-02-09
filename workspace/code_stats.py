#代码有效行数统计
#code_stats
#对于注释块主要是'''和"""，缺省认为其遵循正常的规则，一个放在开头，另一个放在结尾

def code_stats(file_dir):
    '''
    文件读取和存储的效率比较低，看看能否优化
    '''
    assert type(file_dir) is str
    f = open(file_dir,'r+',encoding='utf-8')
    code_ls = f.readlines()
    row = len(code_ls)
    blanks = 0
    codes = 0
    block = find_block(code_ls)
    comments = 0
    for i in range(0,len(code_ls)):        
        if block[i] is 1:
            comments += 1
            continue
        if isComment_line(code_ls[i]):
            comments += 1
            continue
        if isBlank_line(code_ls[i]):
            blanks += 1
            continue
        codes += 1
    print('''-Total Rows:{0}
          +Comments Rows:{1}
          +Blanks Rows:{2}
          +Code Rows:{3}'''.format(row,comments,blanks,codes))
    f.close()
    
    
def isComment_line(str1):
    str1.lstrip()
    if str1[0] == '#':
        return True
    return False


def isBlank_line(str1):
    str1.lstrip()
    if str1[0] == '\n':
        return True
    return False


def find_block(ls):
    enter_block = -1
    #有两种类型的注释，1代表‘型，2代表“型
    block_type = 1
    block = [0]*len(ls)
    for i in range(0,len(ls)):
        isBlock, block_type = isComment_block(ls[i], enter_block, block_type)
        if enter_block > 0:
            block[i] = 1
        elif isBlock:
            block[i] = 1
        if isBlock:
            enter_block *= -1
        
    return block

    
def isComment_block(str1, enter_block, block_type):
    block_1 = "'"*3
    block_2 = '"'*3
    str1 = str1.strip()
    str1 = str1.replace('\n','')
    isBlock = False
    if enter_block >0:
        if block_type ==1:
            if block_1 in str1:
                if str1.rfind(block_1) == (len(str1)-3):
                    isBlock = True
        else:
            if block_2 in str1:
                if str1.rfind(block_2) == (len(str1)-3):
                    isBlock = True
    else:
        if block_1 in str1:
            if str1.find(block_1) == 0:
                isBlock = True
                block_type = 1
        if block_2 in str1:
            if str1.find(block_2) == 0:
                isBlock = True
                block_type = 2
    return isBlock, block_type
