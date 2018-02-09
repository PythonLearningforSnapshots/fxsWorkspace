#--encoding=utf-8---
#读取用户管理文件，根据用户设置进行登陆管理
#文件存储格式‘用户名|密码|登陆次数’
#文件路径C:\Users\305012621\AppData\Local\Programs\Python\Python36\workspace\users.txt

#读取用户文件，并存储在列表中
f=open(r'C:\Users\305012621\AppData\Local\Programs\Python\Python36\workspace\users.txt','r',encoding='utf-8')
lines=f.readlines()
f.close()
if f.closed == False:
   print('文件不能正常关闭')
   exit()
#创建用户管理字典user_dict
user_dict={}
for i in range(len(lines)):
   user=(lines[i].strip()).split('|')
   user_dict[user[0]]=[user[1],int(user[2])]
#登陆管理
#counter用于登陆计数
#逻辑是计数不能大于用户登陆限次或者针对用户名错误缺省限次limits
limits=3
counter=0
while True:
    print('please input user:')
    user_name=input()
    if user_name in list(user_dict.keys()):
        print('please input password:')
        user_pwd=input()
        if user_pwd == user_dict[user_name][0]:
           print('login successful')
           break;
        else:
            #密码错误，可登陆次数减1
            user_dict[user_name][1]-=1
            if user_dict[user_name][1]==0:
                print('logon out of limits')
                break
            print('wrong password, please input again, %s have %d chance'%(user_name,user_dict[user_name][1]))            
    else:
        #用户名错，counter计数加1
        counter +=1
        if counter ==limits:
            print('logon out of limits')
            break;
        print('wrong username, please input again, you have %d chance'%(limits-counter))
       
       
       
