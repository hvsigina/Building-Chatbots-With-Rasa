import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Class to handle mailing part of the chatbot
class Mail:
    def __init__(self, from_, passwd):
        self.from_ = from_
        self.passwd = passwd

        self.s = smtplib.SMTP('smtp.gmail.com', 587)
        print('server joined ')
        self.s.starttls()
        self.login()
        print(self.s.noop())

    def login(self):
        self.s.login(self.from_, self.passwd)
        print('logged in')

    def send(self, to, message):
        self.rcvr = to
        self.last_message = message

        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Top 10 restaurants result"
        msg['From'] = self.from_
        msg['To'] = self.rcvr

        # Create the body of the message (a plain-text and an HTML version).
        text = "Hi!\nHow are you?\nHere is the result of top 10 restaurant  you wanted:\n"
        # html = """\
        # <html>
        #   <head></head>
        #   <body>
        #     <p>Hi!<br>
        #         How are you?<br>
        #         Here is the result of top 10 restaurant  you wanted:</p><br>
        #     <li>abra</li>
        #     <li>ka</li>
        #     <li>dabra</li>
        #     <li>wingar</li>
        #     <li>dium</li>
        #     <li>leviousa</li>
            
        #     Thanks <br>
        #     <img height="32" width="32" src="https://upload.wikimedia.org/wikipedia/en/6/64/Zomato_logo_%28white-on-red%29.png">
        #   </body>
        # </html>
        # """
        html = message

        # Record the MIME types of both parts - text/plain and text/html.
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        msg.attach(part1)
        msg.attach(part2)

        # Send the message via local SMTP server.
        # sendmail function takes 3 arguments: sender's address, recipient's address
        # and message to send - here it is sent as one string.
        self.s.sendmail(self.from_, self.rcvr, msg.as_string())
        self.s.quit()
        print('quitted')

if __name__ == "__main__":
    sender = 'bossmain@gmail.com'
    to = 'boss@gmail.com'

    obj = Mail(sender, 'bossisboss')
    msg = "Hi there this is zomato man   "
    obj.send(to, msg)