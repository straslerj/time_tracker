"""
Time tracker that is helpful in a context where one is logging hours in Gitlab

Author: Jake Strasler
"""

from datetime import datetime
import math
import time


def start():
    return time.time()


def end():
    return time.time()


def get_hours(diff):
    return diff / 3600


def get_minutes(full_time, hours_trunc):
    return full_time - hours_trunc


def format_time_gitlab(hrs, minutes):
    print("/spend " + str(hrs) + "h " + minutes + "m " + str(datetime.today().strftime('%Y-%m-%d')))


def determine_hours_needed():
    hours_needed = input("Current hours needed as decimal: ")
    new_hours_needed = float(hours_needed) - (float(hours) + (float(minutes_as_int) / 60))

    print("Hours now needed: " + str(float("{0:.2f}".format(new_hours_needed))))
    return str(float("{0:.2f}".format(new_hours_needed)))


def round_to_minutes(x, base=5):
    return base * round(x/base)


def write_log(hrs, str_min):
    with open('log.txt', 'a') as file:
        file.write("/spend " + str(hrs) + "h " + str_min + "m " +
                   str(datetime.today().strftime('%Y-%m-%d')))


if __name__ == "__main__":
    print("Starting", end="")
    for x in range(0, 3):
        time.sleep(0.3)
        print(" .", end="")
    start = start()

    if input("\nEnter f to end running\n") == 'f':
        # difference = end() - start
        difference = 6941

        difference_as_hours = get_hours(difference)
        hours = math.trunc(difference_as_hours)

        minutes_as_decimal = get_minutes(difference_as_hours, hours)
        minutes_as_int = round_to_minutes(minutes_as_decimal * 60)
        minutes_string = str(math.ceil(minutes_as_int))

        format_time_gitlab(hours, minutes_string)
        hours_todo = determine_hours_needed()

        write_log(hours, minutes_string)
        print("-- Process finished --")
    else:
        print("Invalid input.\n-- Process finished --")
