from calendar import month # brings only month feature
print(month(2026,1))

# from calendar import month
# print(calendar(2021)) This will give error because we only imported month from callendar library

#...........................................................................................................

# Using 'as' while importing libraries
import calendar as c # this import calendar by the name 'c'
print(c.month(2026,1)) # here we will not write calendar.month because we imported calendar as 'c'

from calendar import month as m
print(m(2021,5))