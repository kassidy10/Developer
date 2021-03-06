def add_time( start,duration, day_of_week = False ):
    days_of_week_array = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday' ]
    days_of_week_index = { 'Monday' : 0, 'Tuesday' : 1, 'Wednesday' : 2, 'Thursday' : 3, 'Friday' : 4, 'Saturday' : 5, 'Sunday' : 6 }

    start_tuple = start.partition(':')
    start_hours = int(start_tuple[0])
    start_minutes_tuple = start_tuple[2].partition(' ')
    start_minutes = int(start_minutes_tuple[0])
    am_or_pm = start_minutes_tuple[2]
    am_or_pm_flip = { 'AM' : 'PM', 'PM' : 'AM' } 

    duration_tuple = duration.partition(':') 
    duration_hours = int(duration_tuple[0])
    duration_minutes = int(duration_tuple[2])

    amount_of_days = int( duration_hours / 24 )

    end_minutes = start_minutes + duration_minutes
    if ( end_minutes >= 60 ):
        start_hours += 1
        end_minutes = end_minutes % 60
    
    amount_of_am_pm_flip = int(( start_hours + duration_hours ) / 12 )
    end_hours = ( start_hours + duration_hours ) % 12
    end_minutes = start_minutes if end_minutes > 9 else '0' + str(end_minutes)

    if ( am_or_pm == 'PM' and start_hours + ( duration_hours % 12 ) >= 12 ):
        amount_of_days += 1
        
    am_or_pm = am_or_pm_flip[am_or_pm] if amount_of_am_pm_flip % 2 == 1 else am_or_pm
    returnTime = f'{str(end_hours)}:{str(end_minutes)} {am_or_pm}'
    if ( day_of_week ):
        day_of_week = day_of_week.capitalize()
        index = int(( days_of_week_index[day_of_week]) + amount_of_days) % 7 
        
        new_day = days_of_week_array[index]
        returnTime += f', {new_day} '

    if ( amount_of_days == 1 ):
        return returnTime + f'(next day)'
    elif( amount_of_days > 1 ) :
        return returnTime + f"({str(amount_of_days)} days later)"
    return returnTime

print(add_time('01:00 PM', '03:00', 'Thursday'))
print(add_time('11:46 PM', '10:12','Tuesday' ))
print(add_time('1:00 AM', '51:00','Monday' ))
