#!/usr/bin/env python
#-*- coding: UTF-8 -*- 

import os
import time
import smtplib
from email.mime.text import MIMEText
import sys


mail_host = "smtp.exmail.qq.com:25"
mail_user = "example@xxx.com"
mail_pass = "**********"

def main():
    cmd = "scala /home/zrc/scripts/eat/where_to_eat3.scala /home/zrc/scripts/eat/rest.list"
    fd = os.popen(cmd)
    line = fd.readline()
    fd.close()	
    send_mail(mail_user, mail_host, "今日餐厅 : " + line)
#    send_mail("zhengxin@qingting.fm",mail_host,line)
#    send_mail("wanghao@qingting.fm",mail_host,line)

def send_mail(to_list, subject, content):
    me = mail_user
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = me
    msg['to'] = to_list
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user, mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except Exception,e:
        print str(e)
        return False

if __name__ == '__main__':
    main()
