#!/usr/bin/python3
import smtplib

sender = 'jnlemayian@gmail.com'
receivers = ['lemayiannakolah@gmail.com']
message = """
From: From Lemayian <jnlemayian@gmail.com>

To: To James <lemayiannakolah@gmail.com>

Subject: SMTP e-mail test

This is a test e-mail message.
"""
try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message)
    print ("Successfully sent email")
except smtplib.SMTPException:
    print ("Error: unable to send email")
