# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2018/10/9 15:17
# 文件: smtp.py
import smtplib
from email.header import Header
from email.mime.text import MIMEText

class Smtp():

  def sendEmail(self,report_path):
    # 发件人和收件人
    sender = 'redmine@kalamodo.com'
    receiver = 'gurr@kalamodo.com'

    # 所使用的用来发送邮件的SMTP服务器
    smtpserver = 'smtp.kalamodo.com'

    # 发送邮箱的用户名和密码
    username = 'redmine@kalamodo.com'
    password = 'Kalamodo0311'

    # 邮件主题
    mail_title = '【外呼计划2.0UI层自动化测试报告】'

    # 读取html文件内容
    f = open(report_path,'rb')  # HTML文件默认和当前文件在同一路径下，若不在同一路径下，需要指定要发送的HTML文件的路径
    mail_body = f.read()
    f.close()

    # 邮件内容, 格式, 编码
    message = MIMEText(mail_body, 'html','utf-8')
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = Header(mail_title,'utf-8')

    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, message.as_string())
        print("发送邮件成功！！！")
        smtp.quit()
    except smtplib.SMTPException:
        print("发送邮件失败！！！")
