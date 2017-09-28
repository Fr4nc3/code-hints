import urllib.request
import urllib.error

# The source of US_NAVAL_OBSERVATORY_MASTER_CLOCK_TIME_URL is on the monitor
US_NAVAL_OBSERVATORY_MASTER_CLOCK_TIME_URL = \
    'http://tycho.usno.navy.mil/timer.html'
r = urllib.request.urlopen(US_NAVAL_OBSERVATORY_MASTER_CLOCK_TIME_URL)
print(r.read())  # all
print()

# The source of A_VERY_SIMPLE_WEBSITE is on the monitor
A_VERY_SIMPLE_WEBSITE = \
    'https://docs.google.com/document/d/1hfeaD5dkfN-vdDeu7nd0H7zDS53gUYZvj76e1rI3CiU/edit'
s = urllib.request.urlopen(A_VERY_SIMPLE_WEBSITE)
print(s.read())  # all