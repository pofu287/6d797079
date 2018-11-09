from emailer_live import mailer
class Rota_Emailer:
    @staticmethod
    def email_rotas(start_of_period,     end_of_period, shifts_and_tally, subject, sender, receivers):
        e = mailer()
        #input('Receivers ').split()
        #subject = 'Rota For {} - {}'.format(start_of_period, end_of_period)
        e.smtp_mailer(shifts_and_tally, subject, sender, receivers)
        feedback = 'Email Sent To :' +  ''.join(receivers)
        return feedback
        
