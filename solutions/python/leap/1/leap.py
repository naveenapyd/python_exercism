def leap_year(year):
    a = year/4
    if (a.is_integer()):
        return divisible_by_100(year)
    else:
        return False

def divisible_by_100(year):
    a = year/100
    if(a.is_integer()):
        return divisible_by_400(year)
    else:
        return True

def divisible_by_400(year):
    a = year/400
    if(a.is_integer()):
        return True
    else:
        return False
            
        
