#!/usr/bin/python
# -*- coding: utf-8 -*-
#takes care of the mailing part

import smtplib

def sending(receiver,message):

    sender = 'obi-wan_kenobi@telenet.be'

    s = smtplib.SMTP('mail-out.telenet.be')
    s.sendmail(sender, receiver, message)
    s.quit()
    print ('Successfully sent email')

