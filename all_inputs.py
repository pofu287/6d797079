from datetime import datetime
import collections
from aux_methods import Aux_Methods
from patterns_and_rota import Shifts
import re
from Regexs import All_regexs
from constraints import Constraints
import generate_shiftdates
import rota_emailer
import globals
import pprint
class Local_aux_methods:

    @staticmethod 
    def sanitize_input(console_input):
        ''' return the following sanitized values : start_period, end_period, the_day, occurs, starts_at, ends_at '''
        regexs_obj = All_regexs()
        aux_obj = Aux_Methods()
        sanitized_input = []
        all_units = re.split('; |, |-|\s',console_input)
        # remove the empty strings left in all_units list as filter leaving some behind
        #print(all_units)
        all_units = [unit for unit in all_units if unit]
        for idx, unit in enumerate(all_units):
            sanitized_input.append(unit)
        #sanitizing the inut returning formatted input as start_period, end_period, day, occurences, starts_at, ends_at, label. Label may not be input so a default label is given
        last_index = len(sanitized_input) - 1
        for i in range (2, last_index):
            if (i < last_index - 1 and regexs_obj.is_day_of_week(sanitized_input[i].upper()) and regexs_obj.is_day_of_week(sanitized_input[i+1].upper()) ):
                occurences = aux_obj.total_days_in_gap(sanitized_input[i].upper(),sanitized_input[i+1].upper())
                sanitized_input[i+1] = str(occurences)
                i += 3
            elif regexs_obj.is_day_of_week(sanitized_input[i].upper()):
                occurences = '1'
                sanitized_input[i+1] = occurences
                i += 2
        #print(sanitized_input)
        return sanitized_input #start_period, end_period, the_day, occurs, starts_at, ends_at
        

class Inputs:
    """ all input is processed here before passing to business logic modules """
    @staticmethod
    def get_the_dates():
        """ returns the start and end datetimes as a tuple or to 2 seperate variable"""
        regexs_obj = All_regexs()
        start_of_period = input('Build Rota From ( dd/mm/yyyy): ')
        end_of_period = input('Build Rota To ( dd/mm/yyyy): ')
        if (regexs_obj.is_correct_date_format(start_of_period) and regexs_obj.is_correct_date_format(end_of_period)):
            print('\u2713')
        else:
            print('\u2717')
        #return start_of_period, end_of_period
        ''' DELETE: hard code some input for dev and testing '''
        return '01/01/2018', '31/12/2018'
    
    @staticmethod
    def set_detailed_shiftpattern():
        ''' from a given start date get the date of the first day in the pattern and generate pattern up to the given end date'''
        local_aux_obj = Local_aux_methods()
        tot = None
        pattern_input = ''
        while True:
            print ('Hard coded input...')
            #'\n01/01/2019 - 31/12/2019, Sat - Sun 07:00 - 19:00 early, Mon - Thu 09:00 - 17:00 no_label, Mon - Tue 11:00 - 18:00 no_label, Thu 14:00 - 22:00 late, Fri 10:00 - 16:00 no_label, Sun 07:00 - 15:00 early, Sun - Sat 12:00 - 19:00 tweleve9'
            pattern_input += '\n01/01/2019 - 31/12/2019, Mon - Fri 09:00 - 17:00 no_label, Mon - Fri 07:00 - 15:00 early, Sat - Sun 07:00 - 19:00 early, Mon - Thu 09:00 - 17:00 no_label, Mon - Tue 11:00 - 18:00 no_label, Thu 14:00 - 22:00 late, Fri 10:00 - 16:00 no_label, Sun 07:00 - 15:00 early, Sun - Sat 12:00 - 19:00 tweleve9'
            cleaned_input = local_aux_obj.sanitize_input(pattern_input)
            # Generate tot from sanitized input
            start_period, end_period = cleaned_input[0], cleaned_input[1]
            for idx, unit in enumerate(cleaned_input):
                print(idx, unit)
            response = input('More ?: ')
            if (response != 'y'):
                return tot
       
    #@staticmethod
    #def set_detailed_shiftpattern_old():
    #    tot = None
    #    repetitions = 1
    #    regexs_obj = All_regexs()
    #    aux_obj = Aux_Methods()
    #    while True:
    #        day_of_shift = input('Day(s): ')
    #        if ('-' in day_of_shift):
    #            day1, day2 = day_of_shift.split('-')
    #            if (regexs_obj.check_day_of_week(day1) and regexs_obj.check_day_of_week(day2)):
    #                consec_occurences = aux_obj.total_days_in_gap(day1,day2)
    #        if (day_of_shift != '' and regexs_obj.check_day_of_week(day_of_shift)):
    #            day_of_shift = day_of_shift[0:3].upper()
    #        else:
    #            print('Incorrect format. Try again. \u2717')
    #            continue
    #        start_time = input("Start Time: ")
    #        if (start_time == '' or not regexs_obj.check_time_format(start_time)):
    #            print('Incorrect format. Try again. \u2717')
    #            continue
    #        shift_length = input('Length Of Shift (Hrs Mins)\n')
    #        try:
    #            hrs_remaining , mins_remaining = shift_length.split()
    #        except ValueError:
    #            hrs_remaining = shift_length
    #            mins_remaining = '0'
    #        if (not regexs_obj.check_time_duration_format(hrs_remaining, mins_remaining)):
    #            print('Incorrect format. Try again. \u2717')
    #            continue
    #        label = input('Label for this shift: ')
    #        consec_occurences = input('How many consecutive occurences of this shift?: ')
    #        if (regexs_obj.check_if_number(consec_occurences)):
    #            consec_occurences = int(consec_occurences)
    #        else:
    #            print('Incorrect format. Try again. \u2717')
    #            continue
    #        for i in range(0, consec_occurences):
    #            tuple = day_of_shift, start_time, hrs_remaining, mins_remaining
    #            day_of_shift = aux_obj.next_day_of_week(day_of_shift)
    #            if tot is None:
    #                tot = (tuple,)
    #            else:
    #                tot = tot + (tuple,)
    #        response = input('More ?: ')
    #        if (response != 'y'):
    #                return tot
            
    @staticmethod
    def set_bulk_shiftpattern():
        ''' examples are 4 on 4 off, 5 days 2 off 5 nights 3 off, week of days followed by week of nights i.e. specific pattern from a start date. No days are specified'''
        aux_obj = Aux_Methods()
        s_obj = Shifts()
        c_obj = Constraints()
        tot = None
        output_file = input('Name of output file: ')
        globals.rotafile_path += output_file + '.txt' 
        while True:
            day_type = input('Select Shift Type:\n(1) Same Day\n(2) Overnight\n(3) Off\n ')
            tally = input('How Many? : ')
            if day_type == '3':
                label = 'Off'
                tuple = label, tally
                tot = tot + (tuple,)
            else:
                label = input('What label do you want displayed? : ')
                s = input('Start at (HH:MM): ')
                e = input('End at (HH:MM):  ')
                tuple = label, s, e, tally
                if tot is None:
                    tot = (tuple,)
                else:
                    tot = tot + (tuple,)
            response = input('More ?: ')
            if (response != 'y'):
                return tot

    @staticmethod
    def build_rota_from_tot(start, end, tot):
        """ Generates the rota from start to end based on the pattern and tags in tot
        """
       
        pattern_obj = generate_shiftdates.Shift_Pattern_Dates()
        shift_dates = pattern_obj.pattern_generator_2(start, end, tot)
        print(shift_dates)
        ''' Write this to a test file'''
        #rotafile_path = 'C:\\NewD\\Data\\3_days_3_nights_3_Off.txt'
        #rotafile_path =
        #'https://www.pythonanywhere.com/user/pofu287/files/home/pofu287/MyData/resultfile.txt'
        with open(globals.rotafile_path, "w") as rotafile:
            rotafile.write(shift_dates)
        return shift_dates
        
    @staticmethod   
    def email_to(start, end,msg,):
        sender = input('Sender: ') 
        receivers = input('Receivers ').split()
        subject = 'Rota For {} - {}'.format(start, end)
        re = rota_emailer.Rota_Emailer()
        fedback = re.email_rotas(start, end, msg,subject, sender, receivers)
        return feedback
     
''' label = input('What Label Do You Want Displayed? : ').capitalize()
            tally = input('How Many Of Them In This Block? : ').capitalize()
            start_time = None 
            start_time = input('Start at (HH:MM): ').capitalize()
            if start_time != '':
                hrs = input ('How Many Complete Hours In shift?: ').capitalize()
                mins = input ('How Many Additional Minutes In Shift?: ').capitalize()
                end_time = aux_obj.add_time_to_time(start_time,hrs,mins)
                print ('So shift ends at %s ' %(end_time)).capitalize()
                tuple = label, start_time, end_time, hrs, mins, tally
                gap_to_next_shift = ('How long to next shift (hh:mm)').capitalize()
                gap_hrs, gap_mins = gap_to_next_shift.split()
                start_time = aux_obj.add_time_to_time(end_time,gap_hrs,gap_mins)
                print ('So next shift starts at %s ' %(start_time)).capitalize()
            else:
                tuple = label, tally
            if tot is None:
                tot = (tuple,)
            else:
                tot = tot + (tuple,) 
            response = input('More ?: ')
            if (response != 'y' ):
                return tot'''


