from datetime import date

# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """


    
    def __init__(self):
        self.args = ("That day does not exist.",)


WEEKDAY = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6,
}

ORDER = {
    "first": 0,
    "second": 1,
    "third": 2,
    "fourth": 3,
    "fifth": 4,
    "last": -1,
}


def meetup(year, month, week, day_of_week):
    day = 1
    dates_list = []  # collect all matching weekdays for that month

    # loop through all days of the month
    while True:
        try:
            current_day = date(year, month, day)
        except ValueError:
            break  # stop once days exceed the month

        if current_day.weekday() == WEEKDAY[day_of_week]:
            dates_list.append(current_day)

        day += 1

    # handle first/second/third/fourth/fifth/last
    if week in ORDER:
        i = ORDER[week]
        try:
            return dates_list[i]
        except IndexError:
            raise MeetupDayException()

    # handle "teenth" (days 13–19)
    elif week == "teenth":
        for d in dates_list:
            if 13 <= d.day <= 19:
                return d
        raise MeetupDayException()

    # invalid input
    else:
        raise MeetupDayException()
