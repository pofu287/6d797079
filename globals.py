import datetime
mnth_lst = ['January', 'Feburary', 'March', 'April', 'May', 'June', 'July', 
              'August', 'September', 'October', 'November', 'December']
day_lst = ['Monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'mon', 'tue', 
              'wed', 'thu', 'thur', 'fri', 'sat', 'sun']
rotafile_path = 'C:\\NewD\\Data\\'
rota_table_rows = list()
def get_delta(start_time, end_time):
    #Times are formatted as HH:MM
    fmt ='%HH:%MM'
    tdelta =datetime.datetime.strptime( end_time, fmt )- datetime.datetime.strptime(start_time,fmt)
    return tdelta
