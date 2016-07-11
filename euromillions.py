# Choose the euromillions numbers

import random
from versturen import sending
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#-------------------------------------------------------------------------------------------------------------
def generate_numbers():
    my_list1 = []                              
    my_list2 = []

    while len(my_list1) < 5:                    
        new_number = random.randrange(50)+1    
        if not new_number in my_list1:          
            my_list1.append(new_number)         

    while len(my_list2) < 2:
        new_stars = random.randrange(11)+1
        if not new_stars in my_list2:
            my_list2.append(new_stars)

    winners = sorted(my_list1)
    stars = sorted(my_list2)  
    print ('nummers: ',winners)
    print ('sterren: ',stars)
    
    mailcontact(winners,stars)


#-------------------------------------------------------------------------------------------------------------
def mailcontact(
    # Create the body of the message
    nummers,
    sterren
    ):

    receiver = ['xxx@gmail.com','xxx@gmail.com']
    
    # Create message container - the correct MIME type is multipart/alternative.
    subject = 'Uw Euromillions geluksnummers'  
    sender = 'obi-wan_kenobi@telenet.be'
      
    msgRoot = MIMEMultipart('related')  
    msgRoot['Subject'] = subject
    msgRoot['From'] = sender

    html = \
            """\
            <html>
              <head></head>
              <body>
                <p>Lucky one,<br><br>
                   Hierbij de Euromillions nummers voor vrijdag.<br><br>
                   Winnende nummers: {nummers} <br>Winnende sterren: {sterren}
                </p>
               </body>
            </html>
            """.format(**locals())  

    msgText = MIMEText(html,'html')
      
    msgRoot.attach(msgText)  
    msg = msgRoot.as_string().encode('utf-8')

    # Send the message via SMTP server.
    sending(receiver,msg)


#-------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    generate_numbers()
