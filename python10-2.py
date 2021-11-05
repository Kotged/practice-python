import numpy as np

years = np.arange(1900, 2020+1, 1)
def leap_year(years):

    a=set(filter(lambda x: x%400==0, years))
    b=set(filter(lambda x: x%100==0, set(years)-a))
    c=set(filter(lambda x: x%4==0, set(years)-a-b))
    d=set(filter(lambda x: x, set(years)-a-b-c))
   
    return sorted(list(a|c))

print(leap_year(years))
