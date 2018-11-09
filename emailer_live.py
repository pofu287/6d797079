''' emails message and subject  to a set of recipients from smtp_mailer() method '''
import smtplib
class mailer:
    @staticmethod
    def smtp_mailer(body, subject, me, receivers):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls() 
        msg = 'Subject: {}\n\n{}'.format(subject, body)
        for receiver in receivers:  
            server.login('dsthescheduler@gmail.com','dstheschedulerrr')  
            #server.sendmail(me, receiver, msg)
        return 'Complete!'
        server.quit()
