from datetime import datetime

ordered_date = 30
ordered_month = datetime.utcnow().month
delivery_date = ordered_date + 5





months_with_31_days = [1,3,5,7,9,11,12]
months_with_30_days = [4,6,8,10]

if ordered_month in months_with_31_days:
   if ordered_date > 27:
        if delivery_date > 31:
            
            add_date =  delivery_date - 31
            delivery_date = 1
            
            for n in range(1,add_date):
                delivery_date += 1
         
        if ordered_month == 12:
            ordered_month = 1
        else:
            delivery_month = ordered_month + 1

if ordered_month in months_with_30_days:
   if ordered_date > 27:
        if delivery_date > 31:
            
            add_date =  delivery_date - 31
            delivery_date = 1
            print(f'add date{add_date}')
            for n in range(1,add_date):
                delivery_date += 1
         
        if ordered_month == 12:
            ordered_month = 1
        else:
            ordered_month = ordered_month + 1
