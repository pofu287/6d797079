import datetime

class Shifts:
    def record_shift_times(s_start, s_end,  shift_time_records):
        #records the shift time for each shift generated from pattern and time gal provided. updates the collection of shift_time_records
        unique_key = s_start+' - '+s_end
        fmt ='%H:%M'
        start = datetime.datetime.strptime( s_start, fmt )
        end = datetime.datetime.strptime( s_end, fmt )
        times_tuple =(start,end)
        shift_records ['unique_id'] = times_tuple
        return shift_time_records
       
    def record_shift_datetimes(s_time, e_time, a_date, shift_datetime_records):
         """ records of the start and end datetimes for each shift assigned to the list generated for a given period. updates the collection of shift_datetime_records
         """
         pass
        
       
    def generate_shift_dates(tot, p_start, p_end):
        # returns shifts in a period without any overlap
        pass
    def tot_is_valid(tot):
        #returns true if tot has no overlap
        pass
        
class Pattern:
    
    @staticmethod
    def build_tot():
        # tuple of tuple of shift_ids and number of instances. ((shift1, 6), (shift2,3), (off,3))
        response = ''
        tot = None
        while True:
            tag = input('Shift: ')
            block_size = int(input ('How many?: '))
            tuple = block_size, tag
            if tot is None:
                tot = (tuple,)
            else:
                tot = tot + (tuple,)
            response = input('More ?: ')
            if (response != 'y' ):
                return tot
         
    def overlap_check(s1, e1, date1, s2, e2, date2):
         #return true if any overlap
         pass
         
class Rota:
    
    def assign_rota(shifts_list_obj, staff_ids):
        # return a roster of ids mapped to shift_list_obj
        pass
