currency = input(' Please specify your currency: ')
Wage = input('Please specify your hourly wage: ')
Worktime_day = input('Please indicate the hours you work per day : ')
Worktime_Week = input('Please indicate the days you work per week: ')
Daily_wage = int(Worktime_day) * int(Wage)
Workweek = int(Worktime_Week) * Daily_wage
Workmonth = 4 * Workweek
Gross_Wage = Workmonth
Workyear = 12 * Workmonth
Holiday = input('Please indicate your annual leave days: ')
Holiday_allowance = int(Holiday) * Daily_wage
Social_welfare_contribution = Gross_Wage * 0.20
taxes = Gross_Wage * 0.15
net_Holiday_allowance = Holiday_allowance - Social_welfare_contribution - taxes
net_salary = Gross_Wage - Social_welfare_contribution - taxes


print(' Your hourly wage is ' + str(Wage) + currency + '.')
print(' You earn ' + str(Daily_wage) + currency + ' a day.')
print(' In a month you earn a gross wage of ' + str(Workmonth) + currency + ' your net salary is ' + str(net_salary)
      + currency + '.')
print(' In one year you will earn a gross wage of ' + str(Workyear) + currency + ',' + ' your net salary is ' +
      str(Workyear - (net_salary * 12)) + currency + '.')
print(' With ' + str(Holiday) + ' days of working holiday, you get paid before taxes and social welfare contributions '
      + str(Holiday_allowance) + currency + ',' + ' after taxes and social welfare contribution, you get paid '
      + str(net_Holiday_allowance) + currency + ' during your holiday period. ')
print(' Please note, all these details are measured by the average tax rate in Germany and there is no guarantee for '
      'correctness.')

input(' Please press Enter to close')
