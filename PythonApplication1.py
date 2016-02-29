import datetime

# store the value in a variable called currentDate
currentDate = datetime.date.today()
print (currentDate)
print (currentDate.year)
print (currentDate.month)

# But what if you want to display the date with a different format?
# * Welcome to one of the things that drives programmer insane!
# * Different countries and different users like different date formats,
#   often the default isn't what you need
# * There is always a way to handle it, but it will take a little time and
#   extra code
print (currentDate.strftime('%y'))
print (currentDate.strftime('%d %b, %Y'))

# strfitme format - google it
# %b is the month abberviation
# %B is the fill month name
# %y is two digit year
# %Y is the full year
# %a is the day of the week abbreviated
# %A is the day of the week
