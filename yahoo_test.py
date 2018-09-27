import pandas as pd
import datetime
import pandas_datareader.data as web
import fix_yahoo_finance as fy

import smtplib
from email.mime.text import MIMEText
from apscheduler.schedulers.blocking import BlockingScheduler
import pandas_datareader as pdr

def job():
    stocks = ['AMZN', 'NVDA', 'SHOP', 'DBX', 'GRUB']

    mes = ""
    for str in stocks:

        df = pdr.DataReader(str, data_source='yahoo', start=datetime.date.today())
        df = df[['Open', 'High', 'Low', 'Close']]
        df.head()
        value = unicode(df['Close'][0])

        mes += "The price for '" + str + "'is " + value + ".\n"

    print mes

    mail_host = "smtp.163.com"
    mail_user = "sdulx628@163.com"
    mail_pass = "lanXI52694"
    receiver = '774127995@qq.com'

    message = MIMEText(mes, 'plain', 'utf-8')
    message['From'] = 'Financial Aid'+'<'+mail_user+'>'
    message['To'] = receiver
    message['Subject'] = 'New Stock price'
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)
        smtpObj.login(mail_user,mail_pass)
        print('login successful')
        smtpObj.sendmail(mail_user, receiver, message.as_string())
        smtpObj.quit()
        print("Sent Successfully")
    except smtplib.SMTPException:
        print("Error: Can not send")


scheduler = BlockingScheduler()
scheduler.add_job(job, 'cron', day_of_week='1-5', hour=9, minute=30)
scheduler.add_job(job, 'cron', day_of_week='1-5', hour=10, minute=00)
scheduler.add_job(job, 'cron', day_of_week='1-5', hour=11, minute=00)
scheduler.add_job(job, 'cron', day_of_week='1-5', hour=12, minute=00)
scheduler.add_job(job, 'cron', day_of_week='1-5', hour=13, minute=00)
scheduler.add_job(job, 'cron', day_of_week='1-5', hour=14, minute=00)
scheduler.add_job(job, 'cron', day_of_week='1-5', hour=15, minute=00)
scheduler.add_job(job, 'cron', day_of_week='1-5', hour=16, minute=00)

scheduler.start()
