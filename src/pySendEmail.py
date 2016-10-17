'''
Created on Jan 20, 2016

@author: nick
'''
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import sys
from setuptools.package_index import HREF

from email.mime.application import MIMEApplication
from os.path import basename

SERVER_IPADDRESS = "http://10.1.1.82:8080/"
#SERVER_IPADDRESS = "http://127.0.0.1/"

#def sendEmail(to, gmail_user, gmail_pwd):
def sendEmail(to, file):
    gmail_user = "hongshanzhang012@gmail.com"
    gmail_pwd = 'gFromtj01'

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Your file has been processed"
    msg['From'] = gmail_user
    msg['To'] = ",".join(to)

    # Create the body of the message (a plain-text and an HTML version).
    text = "Hi!\nHow are you?\n \n Your file has been processed." + "\n"
    
    
    html = """\
    <html>
      <head></head>
      <body>
        <p>Hi!<br>
           How are you?<br>
           Your file has been processed. <br>
    """
    
    #hard code server address, need a server name
    #href='<a href="http://10.1.1.82:81/delete?email='+to+'&url='+url+'">Click here to stop monitoring this url</a>'
    #encode to utf8
    
    #data1 = to.encode('utf8')  # encoded to UTF-8
    
    html=html+"""
         </br>
         <p>Hongshan zhang</p>
      </body>
    </html>
    """
    
    with open(file, "rb") as fil:
        part = MIMEApplication(
            fil.read(),
            Name=basename(file)
        )
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(file)
        msg.attach(part)    

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    # Send the message via local SMTP server.
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(gmail_user, gmail_pwd)
    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    smtpserver.sendmail(gmail_user, to, msg.as_string())
    smtpserver.close()

