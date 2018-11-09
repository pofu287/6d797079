import all_inputs
import globals
def get_shift_patterns():
    return 'num_shifts', 'tag'
 
def generic_shift_dates_with_emailer():
    pass
 
def my_add_fn():
    print( "SUM:%s"%sum(map(int, input("Enter 2 numbers seperated by a space").split())))

def my_quit_fn():
    raise SystemExit

def invalid():
    print ("INVALID CHOICE!")
    
inputs_obj =all_inputs.Inputs()
start=''
end=''
tot=()
rota=''
menu = {
  '1': ('Get Dates ', 1),
  '2': ('Set Bulk Shift Pattern', 2),
  '3': ('Set Detailed Shift Pattern', 3),
  '4': ('Generate Shifts Dates From Pattern', 4),
  '5': ('Email List', 5),
  '6':('Location Cover', 6 ),
  '7': ('Quit', 7)
}
while True:
    for key in sorted(menu.keys()):
        print (key+":" + menu[key][0])
    ans = input("Option: ")
    ans = int(menu.get(ans, None)[1])
    if ans == 1:
        start, end = inputs_obj.get_the_dates()
    elif ans == 2:
        tot = inputs_obj.set_bulk_shiftpattern()
        print (tot)
    elif ans == 3:
        tot = inputs_obj.set_detailed_shiftpattern()
        print (tot)
    elif ans == 4:
        if start != '' and end != '' and len(tot)> 0:
         rota = inputs_obj.build_rota_from_tot(start,end,tot)  
        else: 
            print('Set Time And Pattern!')
    elif ans == 5:
        if is_empty(rota):
            print('Generate a rota')
        else:
            feedback =inputs_obj.email_to(start, end, rota)
            print (feedback)
    elif ans == 7:
        exit()
