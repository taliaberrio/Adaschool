#verificar si un año-bisiesto

def es_bisiesto(year):
    if year %4 == 0 and (year %100 != 0 or year  %400 == 0):
        print (f"{year} es bisiesto")
    else: print (f"{year} no es bisiesto")
        
es_bisiesto (2023)