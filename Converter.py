from datetime import datetime
from forex_python.converter import get_rate
from statistics import mean


class Converter:
    def __init__(self, year, curr):
        self.year = int(year)
        self.date_spread = []
        self.rates = []
        self.orig_curr = str(curr)

    def date_gen(self, year=False):
        if year:
            self.year = year
        for x in range(1,13):
            month_ls = []
            for y in range(1,32):
                try:
                    month_ls.append(datetime(self.year,x,y))
                except ValueError:
                    pass
            self.date_spread.append(month_ls)

    def rate_gen(self, to):
        if not type(to) == str:
            raise TypeError('to must be a string.')
        for x in self.date_spread:
            monthly_rates = []
            for y in x:
                monthly_rates.append(get_rate(self.orig_curr, to, y))
            self.rates.append(monthly_rates)

    def get_monthly_average(self):
        monthly_rate_avg = []
        for x in self.rates:
            monthly_rate_avg.append(mean(x))
        return monthly_rate_avg

    def get_yearly_average(self):
        monthly_rate_avg = []
        for x in self.rates:
            monthly_rate_avg.append(mean(x))
        yearly_avg = mean(monthly_rate_avg)
        return yearly_avg
