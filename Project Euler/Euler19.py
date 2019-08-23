"""1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400."""

months = {'Sept':30, 'April': 30, 'June':30, 'Nov':30, 'Jan':31, 'Feb':28, 'Mar':31, 'May':31, 'July':31, 'Aug':31, 'Oct':31, 'Dec':31}
month_order = ['Jan', 'Feb', 'Mar', 'April', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
day_order = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
curr_day = 0
date = ['Jan', 1, 1900]
curr_month = 0
total_sundays = 0
for year in range(1900, 2001):
    for month in range(0,12):
        month_length = months[month_order[month]]
        if month == 1 and year % 4 == 0 and year != 1900:
            month_length += 1
        for day in range(0,month_length):
            if curr_day == 7:
                curr_day = 0
            if curr_day == 6 and day == 0 and year >= 1901:
                total_sundays += 1
                print('day: ' + day_order[curr_day] + ' month: ' + month_order[month] + ', year: ' + str(year))
            curr_day +=1
print(total_sundays)
#171
