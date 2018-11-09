from datetime import datetime, timedelta

class Aux_Methods():
    @staticmethod
    def convert_to_dt_old(s, e, bool_overnight):
         # create datetimes with any date  and one day later
         s_hr, s_min = s.split(':')
         e_hr, e_min = e.split(':')
         s_dt =datetime (year=1934, month = 1, day = 1, hour = int(s_hr), minute=int(e_min))
         if bool_overnight:
             e_dt = datetime(year=1900, month = 1, day= 2, hour = int(e_hr), minute = int(e_min)) 
         else:
             e_dt = datetime(year=1900, month = 1, day= 1, hour = int(e_hr), minute = int(e_min))                   
         return s_dt, e_dt
         
    @staticmethod 
    def convert_to_dt(s, e, s_day, e_day):
         s_hr, s_min = s.split(':')
         e_hr, e_min = e.split(':')
         s_dt =datetime (year=1900, month = 1, day = s_day, hour = int(s_hr), minute=int(e_min))
         e_dt = datetime(year=1900, month = 1, day= e_day, hour = int(e_hr), minute = int(e_min))                 
         return s_dt, e_dt
         
    @staticmethod
    def formatted_string_as_dt(time_str, yr, mnth, the_day):
     #takes a time as hh:mm and returns a dt for given year month and day
        hr, the_min = time_str.split(':')
        dt = datetime(year = yr, month = mnth, day = the_day, hour = int(hr), minute = int(the_min))
        return dt
     
    @staticmethod
    def add_time_to_time(hhmm,hrs,mins):
        '''String in the format HH:MM has hrs and mins added to it and hh:mm extracted'''
        t_hr, t_min = hhmm.split(':')
        t_datetime = datetime(year = 1970, month = 1, day = 1, hour = int(t_hr), minute = int(t_min))
        shiftdelta = timedelta(hours = int(hrs), minutes = int(mins))
        return format(t_datetime + shiftdelta, '%H:%M')

    @staticmethod
    def add_time_to_datetime(dt,hrs,mins):
        '''String in the format HH:MM has hrs and mins added to it and date (%b %d)extracted'''
        delta = timedelta(hours = int(hrs), minutes = int(mins))
        return format(dt + delta, '%b %d')

    @staticmethod
    def next_day_of_week(day_name):
        weekDays = ["SUN", "MON", "TUE","WED","THU","FRI","SAT"]
        day_index = weekDays.index(day_name)
        if (day_index == len(weekDays) -1):
            return weekDays[0]
        return weekDays[day_index + 1]

    @staticmethod
    def total_days_in_gap(day1, day2):
        weekDays = ["SUN", "MON", "TUE","WED","THU","FRI","SAT"]
        day1_index = weekDays.index(day1)
        day2_index = weekDays.index(day2)
        if (day1_index == 6 and day2_index ==0):
            return 2
        return abs(day1_index - day2_index) + 1
