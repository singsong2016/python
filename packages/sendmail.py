import smtplib
from email.mime.text import MIMEText
from email.header import Header

    # 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "jdcmail@qq.com"  # 用户名
mail_pass = "qrcwxfalvknicbee"  # 口令
sender = 'jdcmail@qq.com'
receivers = ['jdcmail@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱


def sendmail(subject, content):
    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(content, 'plain', 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP_SSL()      # smtplib.SMTP() 25 port server blocked  SSL 465 OK
        smtpObj.connect(mail_host, 465)    
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print('mail send successfully')
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")
