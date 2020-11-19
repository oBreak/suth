#!/usr/bin/python

import smtplib
import configparser

#SMTP.set_debuglevel(True)

msg = 'Hello world.'

server = smtplib.SMTP('mailserver',25) #port 465 or 587
server.set_debuglevel(True)
server.ehlo()
server.starttls()
server.ehlo()
# server.login('username','password')
try:
    server.sendmail('sender','receiver',msg)
except:
    print('Did not work')
server.close()

