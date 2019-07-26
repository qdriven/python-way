# -*-coding: utf-8-*-
import smtplib
from email.mime.text import MIMEText


class email_server:
    def __init__(self, user_email, code):
        # 设置邮件服务地址及默认端口号，这里选择的是outlook邮箱
        self.smtp_server = 'smtp-mail.outlook.com:25'
        # 设置发送来源的邮箱地址
        self.mail_account = 'Your email account'
        self.mail_passwd = 'Your email password'
        self.user_email = user_email
        # 发件箱的后缀
        self.mail_postfix = 'outlook.com'
        # subject代表邮件主题信息
        self.subject = 'Email authentication from AJ Kipper'
        self.form_msg = "This is a mailbox validation from" + "<" + self.mail_account + "@" + self.mail_postfix + ">"
        self.content = 'Hi,thank you for registering the chat room created by AJ Kipper!\nYour email authentication code is ' + code

    def send_email(self):
        global send_status
        # 普通文本邮件
        msg = MIMEText(self.content, _subtype='plain', _charset='utf-8')
        msg['Subject'] = self.subject
        msg['From'] = self.form_msg
        msg['To'] = ";".join(self.user_email)
        try:
            server = smtplib.SMTP()
            server.connect(self.smtp_server)
            # 返回服务器特性
            server.ehlo()
            # 进行TLS安全传输
            server.starttls()
            server.login(self.mail_account, self.mail_passwd)
            server.sendmail(self.form_msg, self.user_email, msg.as_string())
            server.close()
            return True
        except Exception as error:
            print(str(error))
            return False


if __name__ == '__main__':
    email_server()
