
# Reference here:
# https://mimic.mit.edu/docs/iv/modules/hosp/patients/
class Patient():
    
    def __init__(self, id, age, year, year_group, dod):
        self.id = id
        self.age = age
        self.year = year
        self.year_group = year_group
        self.dod = dod
