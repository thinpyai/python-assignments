# In a small town the population is p0 = 1000 at the beginning of a year. 
# The population regularly increases by 2 percent per year and moreover 
# 50 new inhabitants per year come to live in the town. How many years 
# does the town need to see its population greater or equal to p = 1200 
# inhabitants?

# At the end of the first year there will be: 
# 1000 + 1000 * 0.02 + 50 => 1070 inhabitants

# At the end of the 2nd year there will be: 
# 1070 + 1070 * 0.02 + 50 => 1141 inhabitants (** number of inhabitants is an integer **)

# At the end of the 3rd year there will be:
# 1141 + 1141 * 0.02 + 50 => 1213

# It will need 3 entire years.

def nb_year(p0: int, percent: float, aug: int, p: int):
    
    percent = 2 if not percent else percent
    p0 = 1000 if not p0 else p0
    aug = 50 if not aug else aug
    p = 1200 if not p else p
    year = 1
    
    while True:
        p0 += p0 * percent / 100 + aug
        if p0 >= p:
            break
        year +=1
            
    return year

def nb_year_2(p0, percent, aug, p, years = 0):
    if p0 < p:
        return nb_year(p0 + int(p0 * percent / 100) + aug, percent, aug, p, years + 1)
    return years

if __name__ == "__main__":
    # print(nb_year(1500, 5, 100, 5000)) # 15
    # print(nb_year(1500000, 2.5, 10000, 2000000)) # 10
    # print(nb_year(1500000, 0.25, 1000, 2000000)) # 94
    # print(nb_year(1500000, 0, 1000, 2000000)) # 28
    # print(nb_year(0, 0, 0, 0)) # 50
    print(nb_year(1000, 2, 50, 1200)) # 3