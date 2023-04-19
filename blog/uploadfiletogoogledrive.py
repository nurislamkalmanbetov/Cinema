# import smtplib

# # from django.conf import settings
# # можно запустить отдельно убрав джанго сеттингс и прописать логин и пароль отдельно smpt_username и тд

# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart


# # Настраиваем подкл к СМТП серверу 
# smtp_server = 'smtp.gmail.com'
# smtp_post = 587
# smtp_username = 'kalmanbetovnurislam19@gmail.com' #settings.GMAIL_USER
# smtp_password =  'Belford312' #settings.GMAIL_PASSWORD
# smtp_do__tls = True 

# #создаем обьект плдключение к серверу 
# server = smtplib.SMTP(smtp_server, smtp_post)
# server.starttls()
# server.login(smtp_username, smtp_password)

# #Создаем объект сообщения 
# msg = MIMEMultipart()
# # msg['From'] = smtp_username 
# msg['To'] = 'alexandrkim.297@gmail.com'
# msg['Subgject'] = 'Тема сообщения'
# body = 'Текст сообщения в формате plain text'
# msg.attach(MIMEText(body, 'plain'))

# # Отправляем сообщение
# server.send_message(msg)
# server.quit 

# _ 

from google.ouath2 import service_account
from googleapiclient.http import MediaIoBaseDownload,



import os 

SCOPES = ['']


























