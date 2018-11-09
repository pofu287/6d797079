import re

class All_regexs():
    """checks all inputs against relevant regexs for valid formats"""
      #\b((mon|tue(s)?|wed(nes)?|thur(s)?|fri|sat(ur)?|sun)(day)?)\b
    #regex_mil_time = r'^([01]?\d|2[0-3]):?([0-5]\d)$'# 00:12 0012 1:12 112 etc
    #regex_0_24 = r'^\b2[0-4]\b|\b[0-1]?[0-9]\b$' #0 -23 matched in shift kebgth
    #regex_0_59 = r'^([0-5]\d?)?$'  #r'^\d|[0-5]\d$' #0 - 59 matched in shift kebgth
   # regex_days_of_week = r'\b((mon|tue(s)?|wed(nes)?|thur(s)?|fri|sat(ur)?|sun)(day)?)\b' #r'^((Mon)*|(Tue)*|(Wed)*|(Thu)*|(Fri)*|(Sat)*|(Sun)*)(day)?$' #, re.IGNORECASE
    
    @staticmethod
    def is_day_of_week(days):
        '''TODO: Tighten this regex!!!....day is appended to abbrevaitions given false matches'''
        regex_days_of_week = r'\b((mon|tue(s)?|wed(nes)?|thu(rs)?|fri|sat(ur)?|sun)(day)?)\b'
        match_obj_day= re.match(regex_days_of_week, days, re.RegexFlag.IGNORECASE)
        #re.match( r'^((Mon(day)?)*|(Tue(s)?|(sday)?)*|(Wed(s)?|(nesday)?)*|(Thu(rsday)?|(r)?)*|(Fri(day)?)*|(Sat(urday)?)*|(Sun(day)?)*)?$', line, re.RegexFlag.IGNORECASE)
        if (match_obj_day):
            return True
        return False
    
    @staticmethod
    def is_correct_time_format(mil_time):
        regex_mil_time = r'^([01]?\d|2[0-3]):?([0-5]\d)$'
        match_obj_mil_time = re.match(regex_mil_time, mil_time)
        if (match_obj_mil_time):
            return True
        return False
    
    @staticmethod
    def check_time_duration_format(hrs, mins):
        regex_0_24 = r'^\b2[0-4]\b|\b[0-1]?[0-9]\b$' #0 -23 matched in shift kebgth
        regex_0_59 = r'^([0-5]\d?)?$'  #r'^\d|[0-5]\d$' #0 - 59 matched in shift kebgth
        match_obj_hrs  = re.match(regex_0_24, hrs)
        match_obj_mins = re.match(regex_0_59, mins)
        if (match_obj_hrs and match_obj_mins):
            return True
        return False

    @staticmethod
    def is_number(num):
        regex_num = r'^\d+\d*$'
        match_obj_num = re.match(regex_num, num)
        if(match_obj_num):
            return True
        return False

    @staticmethod
    def is_correct_date_format(date_to_check):
        ''' checks valid date format (/ . - seperators) and fails to match feb 29 in leap years. ref: https://stackoverflow.com/questions/15491894/regex-to-validate-date-format-dd-mm-yyyy'''

        regex_date_format = r'^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[1,3-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$'
        match_obj_date_format = re.match(regex_date_format, date_to_check)
        if (match_obj_date_format):
            return True
        return False







