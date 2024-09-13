from asyncore import read
from http import server
import pandas

# excel_data_df = pandas.read_excel('./Book2.xlsx', sheet_name='Sheet1')

# # print whole sheet data
# print(excel_data_df)

# import pandas as pd
# import numpy as np
# cols = [3]
# df = pandas.read_excel('./Book2.xlsx',sheet_name='Sheet1', usecols=cols)
# print(df)
# import csv

# with open ('new.csv', 'r') as csv_file:
#   csv_reader = csv.reader(csv_file)

#   for line in csv_reader:
#     print(line[0])

import csv, smtplib
from email.message import EmailMessage

server = smtplib.SMTP('mail.baba-book.com', 465)
server.starttls()
server.login('aamir@baba-book.com', 'haider0007')
subject = "This email is for checking"

msg = '''
Hello\n
This is checking email from aamir
'''


sender = 'aamir@baba-book.com'

with open ('new1.csv', 'r') as csv_file:
  csv_reader = csv.reader(csv_file)

  for line in csv_reader:
    # print(line[0])
    email = EmailMessage()
    email['From']=sender
    email['To']=line[0]
    email['Subject']=subject
    email.set_content(msg)
    server.send_message(email)
    print(f'Sent to {line[0]}')
server.close()
