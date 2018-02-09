''' CALCULATOR
计算+-*/（），浮点运算
自动检查不合法的运算符
自动检查不合法的被操作数
和eval()函数进行比较
'''


def check_brackets(str1):
    ''' remove the brackets in Formula
    # 不合法的括号用法，用正则表达式比较容易
    # （和）数量不一致
    # (),(-),(+),(*),(/),)(
    # )-),)+)，)*)，)/)，即两个右括号之间不能有运算符
    # (*(,(/(，两个右括号之间不能有*/
    # 3(,)3，数字不能和括号直接相邻
    :param str1 is a string
    :return None failed; string
    '''
    brackets_ls = [')(', '()', '(+)', '(-)', '(*)', '(/)', ')+)', ')-)', ')*)', ')/)', '(*(', '(/(']
    assert type(str1) is str
    # 检查（）是否成对，数量一致检查
    if str1.count('(') == str1.count(')'):
        pass
    else:
        print("miss brackets")
        return None
    # 检查非法（）用法
    for br in brackets_ls:
        if br in str1:
            print("wrong brackets:", str1)
            return None
    for i in range(10):
        if '{0}('.format(i) in str1 or '){0}'.format(i) in str1:
            print("wrong brackets:", str1)
            return None
    return str1


def remove_brackets(str1):
    '''
    # 定义第一层递归，去除（），使用partition和rpartition
    # 递归的方法，结束条件就是没有括号了
    :param str1:
    :return:
    '''
    assert type(str1) is str

    # 递归结束条件
    # 检查是否没有（）了
    if str1.count('(') == 0:
        str1 = calculate(str1)
        return str1

    # 提取无括号的算式
    # 从右边寻找（
    t_1 = str1.rpartition('(')
    # 寻找对应（的）
    t_2 = t_1[2].partition(')')
    # 选取（）中的算式
    str1 = t_2[0]
    str1 = calculate(str1)
    assert type(str1) is str
    # 合并去除一层括号的新算式
    str1 = '{0}{1}{2}'.format(t_1[0], str1, t_2[2])
    # 继续去除括号
    str1 = remove_brackets(str1)
    assert type(str1) is str
    return str1


def isdigital(str1):
    '''
    #判断是否是整数
    # 不含冗余的空格和+-

    :param str1:
    :return:
    '''
    if str1[0] in '-+':
        if str1[1:].isdecimal():
            return True
    elif str1.isdecimal():
        return True
    return False


def isfloat(str1):
    '''
    # 判断是否是浮点数
    # 不含冗余+-
    :param str1:
    :return:
    '''
    try:
        float(str1)
        return True
    except:
        return False


def calculate(str1):
    '''
    # 无括号算式计算
    :param str1:
    :return:
    '''
    assert type(str1) is str
    # 简化操作符
    str1 = simple_op(str1)

    # 判断是否存在不合法操作符
    if check_op(str1) is False:
        print('wrong op:', str1)
        return None

    # 递归结束条件，算式为纯数字
    #    if isdigital(str1):
    #        return str(int(str1))
    if isfloat(str1):
        return str(float(str1))

    # 先计算高优先级运算符,结合方式从左至右
    if '*' in str1 or '/' in str1:
        str1 = mul_div(str1)
    elif '+' in str1[1:] or '-' in str1[1:]:
        str1 = add_sub(str1)

    str1 = calculate(str1)
    return str1


def e_find(str1, op='+'):
    '''
    # 增强型e_find功能，消除e+，e-，只寻找+-
    # op='+' or '-',缺省为+
    # 从左边找起
    :param str1: 无括号算式
    :param op:+ or -
    :return:返回算式最靠左的+，-号的位置，int型
    '''
    assert type(str1) is str
    assert type(op) is str
    e_op = 'e{0}'.format(op)
    if op in '+-':
        op_index = str1[1:].find(op)
        eop_index = str1.find(e_op)

        # 消除e+/-影响
        if op_index == eop_index:
            # 把e+/-当作+/-，寻找下一个+/-
            if str1[eop_index + 2:].find(op) >= 0:
                op_index = str1[eop_index + 2:].find(op) + eop_index + 2
            else:
                op_index = -1
        else:
            # 不存在e+/-符号，或者e+/-并不影响该次查询
            op_index += 1
        return op_index
    else:
        return -1


def e_rfind(str1, op='+'):
    '''
    # 增强型e_find功能，消除e+，e-，只寻找+-
    # op='+' or '-',缺省为+
    # 从右边找起
    :param str1:
    :param op:
    :return:
    '''
    assert type(str1) is str
    assert type(op) is str
    e_op = 'e{0}'.format(op)
    if op in '+-':
        op_index = str1[1:].rfind(op)
        eop_index = str1.rfind(e_op)

        if op_index == eop_index:
            # 把e+/-当作+/-，寻找下一个+/-
            if str1[1:eop_index].rfind(op) >= 0:
                op_index = str1[1:eop_index].rfind(op) + 1
            else:
                op_index = -1
        else:
            # 不存在e+/-符号，或者e+/-并不影响该次查询
            op_index += 1
        return op_index
    else:
        return -1


def get_ldig(str1):
    '''
    # 获取操作符左边的数字
    :param str1:
    :return:
    '''
    assert type(str1) is str
    if isfloat(str1):
        return ['', float(str1)]

    '''op_index = []
    ##    op_index.append(str1.rfind('+'))
    ##    op_index.append(str1.rfind('-'))
    op_index.append(e_rfind(str1, '+'))
    op_index.append(e_rfind(str1, '-'))
    op_index.append(str1.rfind('*'))
    op_index.append(str1.rfind('/'))
    pycharm reports:the list creation could be rewritten as a list literal
    '''
    op_index = [-1, -1, -1, -1]
    op_index[0] = e_rfind(str1, '+')
    op_index[1] = e_rfind(str1, '-')
    op_index[2] = str1.rfind('*')
    op_index[3] = str1.rfind('/')
    op_max = max(op_index)

    if isfloat(str1[op_max + 1:]):
        return [str1[:op_max + 1], float(str1[op_max + 1:])]
    else:
        print('wrong digital:', str1)
        return None


def get_rdig(str1):
    '''
    # 获取操作符右边的数字
    :param str1:
    :return:
    '''
    assert type(str1) is str

    if isfloat(str1):
        return [float(str1), '']

    op_index = [-1]
    if e_find(str1, '+') >= 0:
        op_index.append(e_find(str1, '+'))
    if e_find(str1, '-') >= 0:
        op_index.append(e_find(str1, '-'))
    if str1.find('*') > 0:
        op_index.append(str1.find('*'))
    if str1.find('/') > 0:
        op_index.append(str1.find('/'))

    # 判断是否包含非数字字符
    if max(op_index) < 0:
        print('wrong digital:', str1)
        return None

    # 获取最左操作符
    op_min = min(op_index[1:])
    #    if isdigital(str1[:op_min]):
    #        return [int(str1[:op_min]),str1[op_min:]]
    if isfloat(str1[:op_min]):
        return [float(str1[:op_min]), str1[op_min:]]
    else:
        print('wrong digital:', str1)
        return None


def mul_div(str1):
    '''
    # 乘除法的计算，按照先左后右
    # 该算法调用，隐含str1中包含*/算符
    :param str1:
    :return:
    '''
    assert type(str1) is str
    mul_index = str1.find('*')
    div_index = str1.find('/')
    '''
   无需在外定义，是多余的
    num_l1 = []
    num_l2 = []
    '''
    #只有除法
    if mul_index < 0:
        num_l1 = get_ldig(str1[0:div_index])
        num_l2 = get_rdig(str1[div_index + 1:])
        #        ret=int(num_l1[1]/num_l2[0])
        ret = float(num_l1[1] / num_l2[0])
    #只有乘法
    elif div_index < 0:
        num_l1 = get_ldig(str1[0:mul_index])
        num_l2 = get_rdig(str1[mul_index + 1:])
        #        ret=int(num_l1[1]*num_l2[0])
        ret = float(num_l1[1] * num_l2[0])
    #除法比乘法靠左
    elif div_index < mul_index:
        num_l1 = get_ldig(str1[0:div_index])
        num_l2 = get_rdig(str1[div_index + 1:])
        #        ret=int(num_l1[1]/num_l2[0])
        ret = float(num_l1[1] / num_l2[0])
    #乘法比除法靠左
    else:
        num_l1 = get_ldig(str1[0:mul_index])
        num_l2 = get_rdig(str1[mul_index + 1:])
        #        ret=int(num_l1[1]*num_l2[0])
        ret = float(num_l1[1] * num_l2[0])

    str1 = '{0}{1}{2}'.format(num_l1[0], ret, num_l2[1])
    print(str1)
    return str1


def add_sub(str1):
    '''
    # 加减的计算，按照先左后右顺序
    # 该算法调用，隐含str1中不包含*/算符，但包含+-算符
    # 需要考虑科学计数的影响e-,e+
    :param str1:
    :return:
    '''
    assert type(str1) is str

    add_index = e_find(str1, '+')
    sub_index = e_find(str1, '-')

    if add_index < 0:
        num_l1 = get_ldig(str1[0:sub_index])
        num_l2 = get_rdig(str1[sub_index + 1:])
        #        ret=int(num_l1[1]-num_l2[0])
        ret = float(num_l1[1] - num_l2[0])
    elif sub_index < 0:
        num_l1 = get_ldig(str1[0:add_index])
        num_l2 = get_rdig(str1[add_index + 1:])
        #        ret=int(num_l1[1]+num_l2[0])
        ret = float(num_l1[1] + num_l2[0])
    elif sub_index < add_index:
        num_l1 = get_ldig(str1[0:sub_index])
        num_l2 = get_rdig(str1[sub_index + 1:])
        #        ret=int(num_l1[1]-num_l2[0])
        ret = float(num_l1[1] - num_l2[0])
    else:
        num_l1 = get_ldig(str1[0:add_index])
        num_l2 = get_rdig(str1[add_index + 1:])
        #        ret=int(num_l1[1]+num_l2[0])
        ret = float(num_l1[1] + num_l2[0])

    str1 = '{0}{1}{2}'.format(num_l1[0], ret, num_l2[1])
    print(str1)
    return str1


def simple_op(str_op):
    '''
    # 简化+和-形成的冗余符号
    # op代表需要清除的字符串
    使用递归方法完全去除+-的冗余
    :param str_op:
    :return:
    '''
    assert type(str_op) is str

    # 去除字符串中的冗余操作符
    if '++' in str_op:
        str_op = str_op.replace('++', '+')
        str_op = simple_op(str_op)
    elif '--' in str_op:
        str_op = str_op.replace('--', '+')
        str_op = simple_op(str_op)
    elif '+-' in str_op:
        str_op = str_op.replace('+-', '-')
        str_op = simple_op(str_op)
    elif '-+' in str_op:
        str_op = str_op.replace('-+', '-')
        str_op = simple_op(str_op)

    return str_op


def check_op(str1):
    '''
    # 判断是否存在不合法操作符，在无括号的基础上
    # 不合法的算符用法，**,/*,*/,-*,+*,-/,+/,//
    # 在算式头部不能有/*，在算是尾部不能有+-*/
    # 使用的技巧是，把+-号去除，看看是否有不合规*/
    :param str1:
    :return: True;False
    '''
    op_ls1 = ['-/', '+/', '-*', '+*']
    op_ls2 = ['**', '//', '*/', '/*']
    assert type(str1) is str
    # 检查尾部不合法的+-
    if str1[-1] in '+-':
        print('wrong op: ', str1)
        return False

    # 检查不合法的-+和*/组合
    for op in op_ls1:
        if op in str1:
            print('wrong op: ', str1)
            return False
    # 先把+-号去除，使得所有的*/组合暴露出来，例如在头部不合法的*/被+-遮挡
    str1 = str1.replace('+', '')
    str1 = str1.replace('-', '')
    # 尾部和头部*/符号检查
    if str1[0] in '*/' or str1[-1] in '*/':
        print('wrong op: ', str1)
        return False
    # 检查不合法的*/组合
    for op in op_ls2:
        if op in str1:
            print('wrong op: ', str1)
            return False
    return True


def cal(str1):
    '''
    计算入口方法
    :param str1:
    :return:string
    '''
    assert type(str1) is str

    # 去除字符串中的空格
    str1 = str1.replace(' ', '')
    # 对比标准计算器
    print('eval=', eval(str1))
    #去除冗余符号
    str1 = simple_op(str1)
    #检查（）的合法性
    str1 = check_brackets(str1)
    assert type(str1) is str
    str1 = remove_brackets(str1)
    assert type(str1) is str
    return str1
