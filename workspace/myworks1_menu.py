#作业
#菜单数据结构，用字典
menu={'m1':{'m1_1':['m1_1_1','m1_1_2','m1_1_3'],
            'm1_2':['m1_2_1','m1_2_2','m1_2_3'],
            'm1_3':['m1_3_1','m1_3_2','m1_3_3']
            },
      'm2':{'m2_1':['m2_1_1','m2_1_2','m2_1_3'],
            'm2_2':['m2_2_1','m2_2_2','m2_2_3'],
            'm2_3':['m2_3_1','m2_3_2','m2_3_3']
            },
      'm3':{'m3_1':['m3_1_1','m3_1_2','m3_1_3'],
            'm3_2':['m3_2_1','m3_2_2','m3_2_3'],
            'm3_3':['m3_3_1','m3_3_2','m3_3_3']
            }
      }

###不用函数的实现方法
##while True:
##    #判断是否进入下级菜单标志
##    next_L=False
##    #一级菜单选择
##    menu_L1=list(menu.keys())
##    print('please select items:\n',
##          '0:',menu_L1[0],'\n',
##          '1:',menu_L1[1],'\n',
##          '2:',menu_L1[2])
##          
##    select_L1=input()
##    
##    for m1 in range(3):
##        if select_L1==str(m1) or select_L1==menu_L1[m1]:
##            select_L1=menu_L1[m1]
##            next_L=True
##            break
##    #判断是否进入二级菜单
##    if next_L==False:
##        print('please re-select')
##        continue
##    menu_L2=list(menu[select_L1].keys())
##    
##    print('please select items:\n',
##          '0:',menu_L2[0],'\n',
##          '1:',menu_L2[1],'\n',
##          '2:',menu_L2[2])
##          
##    select_L2=input()
##    next_L=False
##    for m2 in range(3):
##        if select_L2==str(m2) or select_L2==menu_L2[m2]:
##            select_L2=menu_L2[m2]
##            next_L=True
##            break    
##    #判断是否进入三级菜单
##    if next_L==False:
##        print('please re-select')
##        continue
##    menu_L3=menu[select_L1][select_L2]
##
##    print('please select items:\n',
##          '0:',menu_L3[0],'\n',
##          '1:',menu_L3[1],'\n',
##          '2:',menu_L3[2])
##          
##    select_L3=input()
##    next_L=False
##    for m3 in range(3):
##        if select_L3==str(m3) or select_L3==menu_L3[m3]:
##            select_L3=menu_L3[m3]
##            next_L=True
##            break 
##     #判断是否正确选择三级菜单
##    if next_L==False:
##        print('please re-select')
##        continue
##    print('your selection is %s -->%s-->%s'%(select_L1,select_L2,select_L3))
##    break
###使用函数的实现方法
##def menu_select(menu):
##    #数据类型检查
##    if isinstance(menu, (list))==False:
##        return [False,'wrong menu']
##    #
##    print('please select items:\n')
##    for i in range(len(menu)):
##        print('%d:'%i,menu[i])
##    select=input()
##    for i in range(len(menu)):
##        if select==str(i) or select==menu[i]:
##            return [True,menu[i]]
##    return [False,'wrong selection']
###主程序
##while True:
##    select=[ [0 for i in range(3)] for i in range(3)]
##    #一级菜单选择
##    menu_L1=list(menu.keys())
##    select[0]= menu_select(menu_L1)              
##    if select[0][0]==False:
##        if select[0][1]=='wrong menu':
##            print('wrong data type')
##            break
##        print('please re-select')
##        continue
##    menu_L2=list(menu[select[0][1]].keys())
##    select[1]= menu_select(menu_L2)              
##    if select[1][0]==False:
##        if select[1][1]=='wrong menu':
##            print('wrong data type')
##            break
##        print('please re-select')
##        continue               
##    menu_L3=menu[select[0][1]][select[1][1]]
##    select[2]= menu_select(menu_L3)              
##    if select[2][0]==False:
##        if select[2][1]=='wrong menu':
##            print('wrong data type')
##            break
##        print('please re-select')
##        continue
##    print('your selection is %s -->%s-->%s'%(select[0][1],select[1][1],select[2][1]))
##    break

#使用函数的实现方法二，强制选择
###输入参数menu为list数据类型，且其元素为字符串
##def menu_select2(menu):
##    while True:
##        print('please select items:\n')
##        for i in range(len(menu)):
##            print('%d:'%i,menu[i])
##        select=input()
##        for i in range(len(menu)):
##            if select==str(i) or select==menu[i]:
##                return menu[i]
##        print('wrong selection')
##
###主程序
##while True:
##    select=[0 for i in range(3)]
##    #一级菜单选择
##    select[0]= menu_select2(list(menu.keys()))              
##    #二级菜单选择
##    select[1]= menu_select2(list(menu[select[0]].keys()))              
##    #三级菜单选择   
##    select[2]= menu_select2(menu[select[0]][select[1]])              
##    
##    print('your selection is %s -->%s-->%s'%(select[0],select[1],select[2]))
##    break    
