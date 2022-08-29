import time as t

'''
localtime() method used to
get the object containing
the local time.
'''
Time = t.localtime()
print(Time)
'''
strftime() method used to
create a string representing
the current time.
'''
current_time = t.strftime("%H:%M:%S", Time)
print(current_time)
