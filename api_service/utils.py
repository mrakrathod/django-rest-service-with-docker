import itertools

def convert_day_to_year(number_of_days):
    DAYS_IN_WEEK = 7

    year = int(number_of_days / 365)
    week = int((number_of_days % 365) / DAYS_IN_WEEK)
    days = int((number_of_days % 365) % DAYS_IN_WEEK)

    return "Average age record is {year} year {week} week and {days} days".format(
        year=year,
        week=week,
        days=days
    )


def lower_and_upper_variations(string):
    return list(set(map(''.join, itertools.product(*zip(string.upper(), string.lower())))))
