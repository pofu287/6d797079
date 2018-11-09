from globals import get_delta 
class Tuple_Of_Tuples:
    @staticmethod
    def get_tuples():
        response = ''
        s_name =''
        off_day =''
        tod = None
        while True:
            #s_off = input('Off Day? : ')
            s_start = input('Shift Start: ')
            if s_start !='Off':
                s_end = input('Shift End: ')
                s_length = get_delta(s_start, s_end)
                s_name= input('Optional Shift Name: ')
                block_size = int(input ('How many?: '))
                if s_name =='':
                    s_details = (s_start, s_end, s_length)
                else:
                    s_details = (s_start, s_end, s_length, s_name)
            else:
                block_size = input('How Many Off?: ')
                s_details = ('Off', block_size)
            if tod is None:
                tod = (s_details,)
            else:
                tod = tod + (s_details,)
            response = input('More ?: ')
            if (response != 'y' ):
            #break
                return tod
   
        
