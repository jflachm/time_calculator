def add_time(stime, dtime, day=None):
  time, period = stime.split()
  hour, min = time.split(":")
  dhour, dmin = dtime.split(":")
  new_time = new_min = new_hour = ''

  days_later = 0
  weekdays = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
  
  hour = int(hour)
  min = int(min)
  dhour = int(dhour)
  dmin = int(dmin)

  tot_hour = hour + dhour
  tot_min = min + dmin
  
  if tot_min > 59:
    new_min = tot_min - 60
    tot_hour = tot_hour + 1
  else:
    new_min = int(tot_min)

  if tot_hour > 12:
    while tot_hour > 12:
      tot_hour = tot_hour - 12
      if period == 'AM':
        period = 'PM'
      else:
        period = 'AM'
        days_later = days_later + 1
      
  if tot_hour == 12 and tot_min > 59:
    if period == 'AM':
      period = 'PM'
    else:
      period = 'AM'
      days_later = days_later + 1

  if new_min < 10:
    new_min = '0'+str(new_min)
  else:
    new_min = str(new_min)
  
  new_hour = str(tot_hour)
    
  wd = ''
  if day != None:
    day = day[0].upper()+day[1:].lower()
    for i,weekday in enumerate(weekdays):
        if day == weekdays[i]:
          new_day = ((int(i) + int(days_later)) % 7)
          new_weekday = weekdays[new_day]
          wd = ", " + new_weekday
    
  if days_later == 0:
    new_time = new_hour + ':' + new_min + ' ' + period + wd
  if days_later == 1:
    new_time = new_hour + ':' + new_min + ' ' + period + wd + ' (next day)'
  if days_later > 1:
    new_time = new_hour + ':' + new_min + ' ' + period + wd + ' ' + "(" + str(days_later) + ' days later)'

  return new_time
