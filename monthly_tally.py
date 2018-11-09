import globals
class EOM:
    def tally(result, current_month, monthly_tally, startdate, period_tally):
        g =globals.mnth_lst
        if current_month != startdate.month:
            mnth_to_summarise = g[current_month -1]
            current_month = startdate.month
            result +='='*80+'\n' + mnth_to_summarise + ':  Shifts = ' + str(monthly_tally)+ ' Hours Total = ' + str(monthly_tally * 12) + ' | Running Tally - Shifts Summed = ' + str(period_tally )+ ' Hours Summed = ' + str(period_tally * 12) + '\n' +'='*80+'\n' 
            monthly_tally = 0
        return result, current_month, monthly_tally
