import datetime
from emailer_live import mailer
from monthly_tally import EOM
import get_shift_patterns
''' calculates shift pattern of 6 nights 3 off for a set period, along with the shidts and hours.worked in every month for that period '''
class Shift_Pattern_Dates:
    @staticmethod
    def pattern_generator_2(sdate, edate, patterns):
        """ Each tuple in patterns represents a part sequence in the shifts for a staff member. It holds the number of days and a shift tag"""
        total_shifts = len(patterns)
        result =''
        startdate = datetime.datetime.strptime(sdate, '%d/%m/%Y')
        enddate = datetime.datetime.strptime(edate,'%d/%m/%Y' )
        monthly_tally = 0
        oneday = datetime.timedelta(days = 1)
        current_month = startdate.month
        while startdate <= enddate:     
            for  block in patterns:
                # of repeats, descrip
                repetitions = block[0]
                tag = block[1]
                for i in range(0, repetitions):
                    result, current_month, monthly_tally = EOM.tally(result, current_month, monthly_tally, startdate)
                    if tag != 'Off':
                        monthly_tally += 1
                    result += startdate.strftime('%A, %B %d, %Y ') + tag +'\n'
                    startdate = startdate + oneday
        return result
                            
c = Shift_Pattern_Dates()
e = mailer()
start_of_period =input ('Start Of Period( dd/mm/yyyy): ')
end_of_period = input ('End Of Period( dd/mm/yyyy): ')
sender ='denis'  #input('Sender: ') 
receivers = 'denis71@gmail.com' #input('Receivers ').split()
tuple_obj = get_shift_patterns.Tuple_Of_Tuples()
pattern = tuple_obj.get_tuples()
#print (pattern)
shifts_and_tally = c.pattern_generator_2(start_of_period, end_of_period, pattern)
print(shifts_and_tally +'\n Emailing Rotas To...')
subject = 'Rota For {} - {}'.format(start_of_period, end_of_period)
e.smtp_mailer(shifts_and_tally,subject, sender, receivers)
# olu97@hotmail.co.uk

