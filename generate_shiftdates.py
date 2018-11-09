''' calculates shift pattern for a set period, along with the shifts and hours worked in every month for that period '''
import datetime
from emailer_live import mailer
from monthly_tally import EOM
import get_shift_patterns
import globals
from aux_methods import Aux_Methods

class Shift_Pattern_Dates:
    @staticmethod
    def pattern_generator_2(sdate, edate, patterns):
        """ Each tuple in patterns represents a part sequence in the shifts for a staff member. It holds the number of days and a shift tag"""
        total_shifts = len(patterns)
        result =''
        result_for_sql_parameters = []
        sql_params = ();
        startdate = datetime.datetime.strptime(sdate, '%d/%m/%Y')
        enddate = datetime.datetime.strptime(edate,'%d/%m/%Y' )
        monthly_tally = 0
        period_tally = 0
        oneday = datetime.timedelta(days = 1)
        current_month = startdate.month
        while startdate <= enddate:
            for  block in patterns:
                # of repeats, descrip
                repetitions = int(block[-1])
                tag = block[0]
                for i in range(0, repetitions):
                    result, current_month, monthly_tally = EOM.tally(result, current_month, monthly_tally, startdate, period_tally)
                    if tag != 'Off':
                        monthly_tally += 1
                        period_tally += 1
                    result += startdate.strftime('%A, %B %d, %Y ') + tag +'\n'
                    startdate = startdate + oneday
        return result
