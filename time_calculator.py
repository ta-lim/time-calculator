def add_time(start, duration, day = False):
  hours = int(start.split()[0].split(':')[0])
  minutes = int(start.split()[0].split(':')[1])
  period = start.split()[1]
  add_hours = int(duration.split(':')[0])
  add_minutes = int(duration.split(':')[1])
  next_time = ''
  curr_day = day
  count_day = 0
  day_num = 0  
  days= ['Monday','Tuesday','Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
  minutes = add_minutes + minutes
  if period == 'PM':
      hours += 12
    
  if minutes >= 60:
    minutes = minutes - 60
    hours += add_hours + 1
  else:
    hours = hours + add_hours

  count_day = hours // 24
  
  if hours >= 12 and hours < 24:
    period = "PM"
    if hours > 12:
      hours = hours - 12
  else:
    hours = hours % 24
    period = 'AM'
    if hours == 0:
      hours = 12
    else:
      if hours > 12:
        hours = hours - 12
        period = "PM"
  
  if minutes < 10:
    minutes = '0{}'.format(minutes)
      
  if curr_day == False:
    if count_day == 0:
      next_time = '{}:{} {}'.format(hours,minutes, period)
    elif count_day == 1:
      next_time = '{}:{} {} (next day)'.format(hours,minutes, period)
    elif count_day > 1:
      next_time = '{}:{} {} ({} days later)'.format(hours,minutes, period, count_day)
  else:
    curr_day = curr_day.lower().title()
    key = days.index(curr_day)
    key += count_day
    if key >= 7:
       key %= 7
    curr_day = days[key]
    if count_day == 0:
      next_time = '{}:{} {}, {}'.format(hours,minutes, period, curr_day)
    elif count_day == 1:
      next_time = '{}:{} {}, {} (next day)'.format(hours,minutes, period, curr_day)
    elif count_day > 1:
      next_time = '{}:{} {}, {} ({} days later)'.format(hours,minutes, period, curr_day, count_day)
    
  return next_time