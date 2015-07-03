# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText
fp = open("test.txt", 'rb')
msg = MIMEText(fp.read())
fp.close()
msg['Subject'] = 'The contents of abc'
msg['From'] = 'something.anything@students.iiit.ac.in'
msg['To'] = 'something.something@students.iiit.ac.in'
s = smtplib.SMTP('students.iiit.ac.in')
s.sendmail('something.something@students.iiit.ac.in', ['something.anything@students.iiit.ac.in'], msg.as_string())
s.quit()