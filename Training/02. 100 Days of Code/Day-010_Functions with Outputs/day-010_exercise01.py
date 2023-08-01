# Exercise 1 - Days in Month

def is_leap(input_year):
    if input_year % 4 == 0:
        if input_year % 100 == 0:
            if input_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(num_year, num_month):
    # months days in Year, starting from index 0 is January
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # check if year is leap, and month = 2
    if is_leap(num_year) and num_month == 2:
        return 29

    # check if year is leap, and month except 2
    elif is_leap(num_year):
        return month_days[num_month - 1]

    # check if year is not leap
    else:
        return month_days[num_month - 1]


# do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
