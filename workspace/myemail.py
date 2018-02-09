'''
myEmail 测试发送邮件功能，使用标准库smtplib和email
第一步，实现发送邮件
第二步，实现查看邮件

'''


import smtplib
import imaplib
from email.mime.text import MIMEText
from email.utils import formataddr


def sendEmail(message,target_addr='xiaoshi.fu@ge.com',mailbox='163'):
    '''
    注意几点
    1、Python发邮件时报错554, b'DT:SPM 163 smtp8,DMCowAA3ZcnNhnVapvmIFQ--.31696S2 1517651661,please see http://mail.163.com/help/help_spam_16.htm?ip=171.221.64.223&hostid=smtp8&time=1517651661'
    原因是标题是‘test’或者‘测试’
    2、Python发邮件时报错550, b'User has no permission，是因为邮件服务器不接受第三方应用访问邮件服务器
    在使用python发送邮件时相当于自定义客户端根据用户名和密码登录，然后使用SMTP服务发送邮件，
    新注册的163邮箱是默认不开启客户端授权的，因此登录总是被拒绝，解决办法（以163邮箱为例）：
    进入163邮箱-设置-客户端授权密码-开启（授权码是用于登录第三方邮件客户端的专用密码）

    功能
    向指定邮箱发送信息，源信箱和目的信箱都可以指定
    
    参数
    message:邮件信息，类型：string
    target_addr:目标信箱地址，类型：string
    mailbox:源信箱类型，只需要指定有代表性的一部分即可，其余部分将会从文件中读取，类型：string

    返回值
    True
    False
    
    '''
    mail_dt = getMailbox(mailbox)
    assert type(mail_dt) is dict
    
    source_addr = mail_dt['addr']
    pwd = mail_dt['pwd']
    mail_host = mail_dt['smtp']
    user = source_addr.split('@')[0]
    print('send email to',target_addr,'from',source_addr)

    msg = MIMEText(message,'plain','utf-8')
    msg['From'] = formataddr(['伏小石',source_addr])
    msg['To'] = formataddr(['python',target_addr])
    msg['Subject'] = 'python'

    try:
        server = smtplib.SMTP(mail_host)
#        server.connect(mail_host) 
        server.login(user,pwd)
        server.sendmail(source_addr,[target_addr],msg.as_string())
        server.quit()
        return True
    except Exception as e:  
        print(str(e))
        return False


def readEmail(mailbox='163'):
    '''
    '''
    mail_dt = getMailbox(mailbox)
    assert type(mail_dt) is dict

    addr = mail_dt['addr']
    pwd = mail_dt['pwd']
    mail_host = mail_dt['imap']
    user = addr.split('@')[0]

##    try:
##        server = imaplib.IMAP4_SSL(mail_host)
##        server.login(user,pwd)
##        mail_lines = server.readline()
##        server.close()
##        return mail_lines
##    except Exception as e:  
##        print(str(e))
##        return False
    print(addr,pwd,mail_host,user)
    server = imaplib.IMAP4_SSL(mail_host)
    server.login(user,pwd)
    server.select()
    typ, data = server.search(None, 'UNSEEN')
    print(data[0].split())
##    typ, data = server.fetch(b'1', '(RFC822)')
##    print('Message %s\n%s\n' % (b'1', data[0][1]))
    for num in data[0].split():
        typ, data = server.fetch(num, '(RFC822)')
        print('Message %s\n%s\n' % (num, data[0][1]))

    server.close()
    server.logout()
    return True

def getMailbox(mailbox):
    '''
    功能
    从文件中读取源信箱的详细信息，包含邮箱地址，密码，smtp，IMAP，POP3

    参数
    mailbox：源邮箱的一部分特有信息，类型：string

    返回值
    源邮箱信息，包含邮箱地址，密码，smtp，，IMAP，POP3，类型：dict
    '''
    try:
        fp = open(r'C:\Users\305012621\AppData\Local\Programs\Python\Python36\workspace\mailbox.txt','r',encoding='utf-8')
        mail_list = fp.readlines()
        fp.close()
    except Exception as e:
        print(str(e))
        return None
    email_dt = {}
    for mail_info in mail_list:
        if mailbox in mail_info:
            mail_info = mail_info.replace('\n','')
            mail_ls = mail_info.split('|')
            if len(mail_ls) is 5:
                pass
            else:
                return None
            email_dt['addr'] = mail_ls[0]            
            email_dt['pwd'] = mail_ls[1]
            email_dt['smtp'] = mail_ls[2]
            email_dt['imap'] = mail_ls[3]
            email_dt['pop3'] = mail_ls[4]
            return email_dt

    return None

with open(r'C:\Users\305012621\AppData\Local\Programs\Python\Python36\workspace\mailbox.txt') as fp:
    i = 0
    for line in iter(fp.readline, ''):
        i += 1
        print(i,line)
