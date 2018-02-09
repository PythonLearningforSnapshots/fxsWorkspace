#cart
#购物车
top_menu=['购物','购物车','结账','离开']

#货品列表，可变，字典表示，为安全，存储于文件中
stock={'香皂':[12,10],'苹果':[3,20],'维生素C':[20,10]}
#存货格式：货品名，价格，数量
stock_ls=[]
#Trading Information，为安全，存储于文件中
#每行格式为：时间，收入,卖出的货品名，价格，数量，客户姓名
trad_ls=[]
#customer记录客户购物和现金信息
#cart记录客户购物车货品
#cash是当前客人总共现金，初始为100
customer={'cart':{},'cash':100,'id':'fxs','pwd':'fxs'}


#主程序
def main():
    init_stock()
    init_customer()
    while(True):
        print('welcome to Xiaoshi\'s Store')
        for i in range(0,len(top_menu)):
            print('{0}:{1}'.format(i,top_menu[i]))
        select=input('please input items NO:')
        if select=='0':
            shopping()
        elif select=='1':
            viewcart()
        elif select=='2':
            checkout()
        elif select=='3':
            goodby()
            break
        else:
            print('wrong selection')
            continue
    return


#购物子程序
def shopping():
    goods_ls=list(stock.keys())
    while(True):
        for i in range(0,len(goods_ls)):
            print('{0}:{1} price:${2} quantity:{3}'.format(i,goods_ls[i],stock[goods_ls[i]][0],stock[goods_ls[i]][1]))

        print('e:exit')

        goods_NO=input('input goods NO:')
        if goods_NO is 'e':
            break
        try:
            int(goods_NO)
            goods_NO=int(goods_NO)
        except:
            print('wrong NO,please select again')
            continue
        #判断货品序号是否正确，注len的用法
        if goods_NO >= len(goods_ls) or goods_NO <0:
            print('wrong NO,please select again')
            continue
        
        goods_qt=input('input goods quantity:')
        if goods_qt is 'e':
            break
        try:
            int(goods_qt)
            goods_qt=int(goods_qt)
        except:
            print('wrong quantity,please select again')
            continue
        #判断选择的货品数量是否合理，不能小于0，不能大于杂货店存货
        if goods_qt > stock[goods_ls[goods_NO]][1] or goods_qt <0:
            print('wrong quantity,please select again')
            continue
        update_cart(goods_ls[goods_NO],goods_qt)


#购物车操作子程序
def viewcart():
    cart_ls=list(customer['cart'].keys())
    if len(cart_ls)==0:
        return
    while True:
        total_price=0
        for i in range(0,len(cart_ls)):
            print('{0}  price:${1}  Quantity:{2}'.format(cart_ls[i],
                                                       customer['cart'][cart_ls[i]][0],
                                                       customer['cart'][cart_ls[i]][1]))
            #计算货物金额
            total_price+=customer['cart'][cart_ls[i]][0]*customer['cart'][cart_ls[i]][1]

        print('Totl price is ${0}, your cash is ${1}'.format(total_price,customer['cash']))

        print('0:increase items')
        print('1:decrease items')
        print('e:exit')
        select =input('your choice:')
        if select is 'e':
            return
        elif select is '0':
            increase_item(cart_ls)
            continue
        elif select is '1':
            decrease_item(cart_ls)
            continue
        else:
            print('wrong select')
            continue


#增加购物车货品
def increase_item(cart_ls):
    for i in range(0,len(cart_ls)):
        print('{0}:{1}  price:${2}  Quantity:{3} stock: {4}'.format(i,cart_ls[i],
                                                   customer['cart'][cart_ls[i]][0],
                                                   customer['cart'][cart_ls[i]][1],
                                                   stock[cart_ls[i]][1]))
    items=input('increase format is ''item No,item quantity'':')
    if ',' in items:
        pass
    else:
        print('wrong format:{0}'.format(items))
        return
    ls=items.split(',')
    if len(ls)>2:
        print('wrong format:{0}'.format(items))
        return
    try:
        item_No=int(ls[0])
        item_qt=int(ls[1])
    except:
        print('wrong format:{0}'.format(items))
        return
    if item_No >= len(cart_ls) or item_No <0:
        print('wrong NO: {0}'.format(item_No))
        return
    #判断增加的数量是否合理，不能小于0，不能多于杂货店货品数量
    if item_qt<0 or item_qt>stock[cart_ls[item_No]][1]:
        print('out of stock: {0}'.format(item_qt))
        return
    #更新购物车
    update_cart(cart_ls[item_No],item_qt)


#减少购物车货品
def decrease_item(cart_ls):
    for i in range(0,len(cart_ls)):
        print('{0}:{1}  price:${2}  Quantity:{3}  stock: {4}'.format(i,cart_ls[i],
                                                   customer['cart'][cart_ls[i]][0],
                                                   customer['cart'][cart_ls[i]][1],
                                                   stock[cart_ls[i]][1]))
    items=input('decrease format is ''item No,item quantity'':')
    if ',' in items:
        pass
    else:
        print('wrong format')
        return
    ls=items.split(',')
    if len(ls)>2:
        print('wrong format:{0}'.format(items))
        return
    try:
        item_No=int(ls[0])
        item_qt=int(ls[1])
    except:
        print('wrong format:{0}'.format(items))
        return
    #检查货品编号是否正确
    if item_No >= len(cart_ls) or item_No <0:
        print('wrong NO: {0}'.format(item_No))
        return
    #判断减少的数量是否合理，不能小于0，不能多于购物车货品数量
    if item_qt<0 or item_qt>customer['cart'][cart_ls[item_No]][1]:
        print('out of cart: {0}'.format(item_qt))
        return
    #更新购物车
    update_cart(cart_ls[item_No],-item_qt)
    pass


#结账子程序
def checkout():
    cart_ls=list(customer['cart'].keys())
    if len(cart_ls)==0:
        return
    
    total_price=0
    for i in range(0,len(cart_ls)):
        print('{0}  price:{1}  Quantity:{2}'.format(cart_ls[i],
                                                   customer['cart'][cart_ls[i]][0],
                                                   customer['cart'][cart_ls[i]][1]))
        #计算货物金额
        total_price+=customer['cart'][cart_ls[i]][0]*customer['cart'][cart_ls[i]][1]

    print('Totl price is ${0}, your cash is ${1}'.format(total_price,customer['cash']))

    print('c:check out')
    print('e:exit')
    select =input('your choice:')
    if select is 'e':
        return
    elif select is 'c':
        if total_price > customer['cash']:
            print('Insufficient balance, please re-select goods')
            return
        update_stock()
        return
    else:
        print('wrong select')


#离开子程序
def goodby():
    #把购物车货品放回货架
    for goods in customer['cart']:
        stock[goods][1]+=customer['cart'][goods][1]
    #客户信息处理，可以写入文件
    customer['cart'].clear()
    pass


#更新购物车和货柜
def update_cart(goods_Name,Qt=0):
    #更新购物车
    if goods_Name in customer['cart']:
        pass
    else:
        customer['cart'].setdefault(goods_Name,[stock[goods_Name][0],0])
        
    customer['cart'][goods_Name][1]+=Qt
    #更新货架
    stock[goods_Name][1]-=Qt


#更新杂货店的货品文件
def update_stock():
    
    #销售记录改变
    #文件写入
    #stock和实时销售记录
    #...

    #客户记录改变
    for goods in customer['cart']:
        customer['cash']-=customer['cart'][goods][0]*customer['cart'][goods][1]
    customer['cart'].clear()


#读取杂货店的货品文件，初始化杂货店    
def init_stock():
#   print(stock)
#    stock={'香皂':[12,10]}
    print('init..............')
#    print(stock)
    #从文件读取列表


#
def init_customer():
    pass


main()
