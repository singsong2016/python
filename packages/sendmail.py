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
    message['From'] = Header("Jsend", 'utf-8')     # 发送者
    message['To'] = Header("Jreceive", 'utf-8')          # 接收者

    # subject = 'mail from python redhat'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print('mail send successfully')
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")