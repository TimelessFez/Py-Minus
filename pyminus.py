# Imports
from datetime import datetime, time
from time import sleep
import os # Needed for clearing screen each second
import sys # For exiting program (cleanly)

def dateDiffInSeconds(date1, date2):
  # [(Target date&time) - (Current date&time)]
  timedelta = date2 - date1
  return timedelta.days * 24 * 3600 + timedelta.seconds

def daysHoursMinutesSecondsFromSeconds(seconds):
	minutes, seconds = divmod(seconds, 60)
	hours, minutes = divmod(minutes, 60)
	days, hours = divmod(hours, 24)
	return (days, hours, minutes, seconds)

# Ask user for the target date & time, to count down to
print("\nThe clock will be displayed in the following format: ")
print("YYYY-MM-DD %H:%M:%S\n")
print("Please enter a target date and time for the countdown.")

year = int(input("\nEnter the year (YYYY): "))
month = int(input("\nEnter the month (MM): "))
day = int(input("\nEnter the day (DD): "))
hour = int(input("\nEnter the hour (24-hr format)(hh): "))
minute = int(input("\nEnter the minute (mm): "))
second = int(input("\nEnter the second (ss): "))

req = datetime(year, month, day, hour, minute, second)
now = datetime.now()

while req>now:
    # Clear terminal screen upon launching applet
    os.system('cls||clear')
    print("%dd %dh %dm %ds" % daysHoursMinutesSecondsFromSeconds(dateDiffInSeconds(now, req)))
    sleep(1)

    now = datetime.now()

# Let the user know that the countdown has finished
print("Done")
# Exit program cleanly
sys.exit()
