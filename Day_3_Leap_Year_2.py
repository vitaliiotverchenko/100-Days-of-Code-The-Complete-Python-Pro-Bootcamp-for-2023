# Instructions
# Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. 

# This is how you work out whether if a particular year is a leap year.
#       on every year that is evenly divisible by 4 
#           **except** every year that is evenly divisible by 100 
#               **unless** the year is also evenly divisible by 400

# e.g. The year 2000:
# 2000 ÷ 4 = 500 (Leap)
# 2000 ÷ 100 = 20 (Not Leap)
# 2000 ÷ 400 = 5 (Leap!)
# So the year 2000 is a leap year.

# But the year 2100 is not a leap year because:
# 2100 ÷ 4 = 525 (Leap)
# 2100 ÷ 100 = 21 (Not Leap)
# 2100 ÷ 400 = 5.25 (Not Leap)

# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

# Example Input 1
# 2400
# Example Output 1
# Leap year.
# Example Input 2
# 1989
# Example Output 2
# Not leap year.



# Рік вважається високосним, якщо він ділиться на 4. Винятком є ​​роки, які кратні 100 (такі роки є високосними тільки тоді, якщо вони ще діляться на 400).
# Список високосних років на найближчі 100 років: 2020, 2024 2028, 2032, 2036, 2040, 2044, 2048, 2052, 2056, 2060, 2064, 2068, 2072, 2076, 2080, 2084, 2088, 2092, 2096, 2104, 2108, 2112, 2116, 2120
# В даному переліку 2100 рік не буде високосним, адже він кратний 100 і не ділиться на 400.
# Скільки днів у високосному році?
# У високосному році 366 днів.
def check_leap_year(year):
    """
    Check if a given year is a leap year or not.

    Parameters:
    - `year` (int): The year to be checked.

    Returns:
    - (str): "Leap" if the year is a leap year, "Not leap" otherwise.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year=2022, month=2):
  """
  Returns the number of days in a given month for a given year.

  Parameters:
    year (int): The year for which the number of days is calculated. Default is 2022.
    month (int): The month for which the number of days is calculated. Default is 2.

  Returns:
    int: The number of days in the given month for the given year.
  """
  if month < 1 or month > 12:
      return 'Invalid month'
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if check_leap_year(year) and month == 2:
    return 29
  return month_days[month - 1]

    
