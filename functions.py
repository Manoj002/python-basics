current_age = int(input("Enter your age: "));
current_year = int(input("Enter current year: "));

def birth_year(age, year):
    birth_yr = year - age;
    return birth_yr;    ### can return more than 1 variable seperated by commas

print(birth_year(current_age, current_year));
