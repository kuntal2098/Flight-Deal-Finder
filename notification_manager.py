from smtplib import SMTP

class NotificationManager:
    def send_mail(self, l):
        FROM = "<Sender Email>"
        PASS = "<Sender Email's Password>"
        TO = "<Recipient Email>"

        message = ""
        for data in l:
            message += f"Only ₹{data['Current Lowest Price']} to fly from {data['Source']} to {data['Destination']} on {data['Date']}\n\n"
        message = f"Subject:Low Price Alert!\n\n" + message
        message = u''.join(message).encode('utf-8').strip()

        server = SMTP('smtp.gmail.com')
        server.starttls()
        server.login(FROM, PASS)
        server.sendmail(FROM, TO, message)
        server.quit()
        return "Email Sent!"