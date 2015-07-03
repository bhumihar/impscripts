#!/usr/bin/python

import smtplib

sender = 'aman.rai@students.iiit.ac.in'
receivers = ['animesh.pathak@students.iiit.ac.in']

message = """From: """ + sender + """
To:""" + receivers[0] + """
Subject: SMTP e-mail test

This is a test e-mail message. """
# print message
try:
	smtpObj = smtplib.SMTP('students.iiit.ac.in')
	smtpObj.sendmail(sender, receivers, message)         
	print "Successfully sent email"
except SMTPException:
	print "Error: unable to send email"