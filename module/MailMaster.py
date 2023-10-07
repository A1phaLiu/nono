#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send_mail(receivers, subject, content):
    # 第三方 SMTP 服务
    mail_host="smtp.qq.com"  #设置服务器
    mail_user="risee"    #用户名
    mail_pass="vnifkbvwqqkxdfdh"   #口令 
    
    
    sender = 'risee@qq.com'
    # receivers = ['risee@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = Header("risee@qq.com")
    message['To'] =  Header("risee@qq.com")
    
    # subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')

    
    try:
        smtpObj = smtplib.SMTP() 
        # smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
        smtpObj = smtplib.SMTP_SSL(mail_host)
        smtpObj.login(mail_user,mail_pass)  
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit() 
        print ("邮件发送成功")
    except smtplib.SMTPException:
        print ("Error: 无法发送邮件")

if __name__ == '__main__':
    subject = 'Hello, there is nono'
    content = 'Hi, this is just a test email.'
    send_mail(['risee@qq.com'], subject, content)